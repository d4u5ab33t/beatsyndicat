#!/usr/bin/env python3
"""Entry point for BeatSyndicat."""

import argparse
import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from agents import BaseAgent
from core.stack_manager import StackManager, verify_project


async def run_once() -> dict:
    config_path = ROOT / "config" / "settings.yaml"
    agent = BaseAgent(config_path=str(config_path))
    return agent.run_cycle()


def main() -> None:
    parser = argparse.ArgumentParser(description="BeatSyndicat command line entry point")
    parser.add_argument("--agent", default="all", help="Agent name or mode")
    parser.add_argument("--once", action="store_true", help="Run one cycle")
    parser.add_argument("--config", default="config/settings.yaml", help="Config path")
    parser.add_argument("--bootstrap", action="store_true", help="Run full stack bootstrap")
    parser.add_argument("--verify", action="store_true", help="Verify project integrity")
    parser.add_argument("--root", default=".", help="Project root path")
    args = parser.parse_args()

    root_path = (ROOT / args.root).resolve() if not Path(args.root).is_absolute() else Path(args.root).resolve()

    if args.bootstrap:
        manager = StackManager(root_path, config_path=ROOT / args.config)
        result = manager.update_all()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if args.verify:
        success = verify_project(root_path, config_path=ROOT / args.config)
        raise SystemExit(0 if success else 1)

    if args.once:
        result = asyncio.run(run_once())
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print(f"BeatSyndicat bootstrap mode: {args.agent}")
    print("Use --once for a single-cycle run, --bootstrap to initialize the stack, or --verify to validate the project.")


if __name__ == "__main__":
    main()
