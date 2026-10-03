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


async def run_once() -> dict:
    agent = BaseAgent(config_path="config/settings.yaml")
    return agent.run_cycle()


def main() -> None:
    parser = argparse.ArgumentParser(description="BeatSyndicat command line entry point")
    parser.add_argument("--agent", default="all", help="Agent name or mode")
    parser.add_argument("--once", action="store_true", help="Run one cycle")
    parser.add_argument("--config", default="config/settings.yaml", help="Config path")
    args = parser.parse_args()

    if args.once:
        result = asyncio.run(run_once())
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print(f"BeatSyndicat bootstrap mode: {args.agent}")
    print("Use --once for a single-cycle run, or run the project from your environment.")


if __name__ == "__main__":
    main()
