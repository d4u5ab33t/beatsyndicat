#!/usr/bin/env python3
"""Compatibility bootstrap wrapper for BeatSyndicat."""

import argparse
import json
from pathlib import Path

from core.stack_manager import StackManager


def main() -> None:
    parser = argparse.ArgumentParser(description="WE.ED.IT / BeatSyndicat bootstrap")
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument("--config", default="config/settings.yaml", help="Configuration path")
    parser.add_argument("--quick", action="store_true", help="Skip optional heavy setup")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manager = StackManager(root, config_path=root / args.config)
    result = manager.update_all(quick_mode=args.quick)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
