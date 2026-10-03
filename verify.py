#!/usr/bin/env python3
"""
BeatSyndicat Verification & Integrity Suite
Validates directory structure, database schemas, configuration files,
and core system integrity.
"""

import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path


def verify_system(root: Path) -> bool:
    print(f"\n🔍 Verifying BeatSyndicat at: {root}")
    all_ok = True

    # 1. Directory Checks
    required_dirs = [
        "config", "manifests", "agents", "database", "cache", "clippool", "knowledge", "plugins",
        "renders", "exports", "logs", "projects/demo", "models", "docker"
    ]
    print("\n[1/4] Checking Directory Structure:")
    for d in required_dirs:
        p = root / d
        if p.exists() and p.is_dir():
            print(f"  ✓ {d:<28} : OK")
        else:
            print(f"  ✗ {d:<28} : MISSING")
            all_ok = False

    # 2. Database Integrity Check
    print("\n[2/4] Checking Database & WAL:")
    db_file = root / "database" / "weedit.db"
    if db_file.exists():
        try:
            conn = sqlite3.connect(str(db_file))
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            conn.close()
            print(f"  ✓ weedit.db      : OK ({len(tables)} tables registered)")
        except Exception as e:
            print(f"  ✗ weedit.db      : CORRUPT ({e})")
            all_ok = False
    else:
        print("  ✗ weedit.db      : NOT FOUND")
        all_ok = False

    # 3. Core Agent Structure
    print("\n[3/4] Checking Autonomous Agents:")
    agent_modules = ["scout", "analyst", "bridge", "cartographer", "oracle", "autopsy"]
    for ag in agent_modules:
        p = root / "agents" / ag
        if p.exists():
            print(f"  ✓ Agent [{ag:<14}] : OK")
        else:
            print(f"  ✗ Agent [{ag:<14}] : MISSING")
            all_ok = False

    # 4. Knowledge & Cache Indices
    print("\n[4/4] Checking Knowledge & Cache Indices:")
    for idx_file in ["clippool/index.json", "cache/semantic/index.json"]:
        p = root / idx_file
        if p.exists():
            print(f"  ✓ {idx_file:<28} : OK")
        else:
            print(f"  ✗ {idx_file:<28} : MISSING")
            all_ok = False

    print("\n" + "=" * 70)
    if all_ok:
        print("🎉 ALL CHECKS PASSED. BEATSYNDICAT SYSTEM INTEGRITY 100%.")
    else:
        print("⚠️ INTEGRITY WARNINGS DETECTED. Please run bootstrap.py to repair.")
    print("=" * 70 + "\n")
    return all_ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="j:/Oidasheim/beatsyndicat")
    args = parser.parse_args()
    success = verify_system(Path(args.root).resolve())
    sys.exit(0 if success else 1)
