# beatsyndicat

A Python-based autonomous creative intelligence and cultural intelligence workstation.

## Quick start

- Windows PowerShell: `.\setup.ps1`
- Linux/macOS: `bash setup.sh`
- Direct bootstrap: `python bootstrap.py --root .`
- Verify integrity: `python verify.py --root .`
- Single cycle: `python main.py --agent all --once`

## Stack architecture

This project is organized around the following runtime stacks:

- Platform stack
- Plugin stack
- AI model stack
- Database stack
- Knowledge stack
- ClipPool stack
- Agent swarm stack

The orchestration logic is centralized in `core/stack_manager.py` and the runtime entry point is `main.py`.

## Core commands

```bash
python main.py --bootstrap
python main.py --verify
python main.py --once
```

## Notes

The repository is intentionally structured to keep configuration under `config/`, manifests under `manifests/`, and stack-related runtime state under `models/`, `plugins/`, `knowledge/`, `clippool/`, and `database/`.
