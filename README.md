# BeatSyndicat Manual

BeatSyndicat is a Python-based project scaffold for an autonomous creative intelligence workstation. It is organized around stack-oriented directories for platform configuration, models, plugins, knowledge, media, and agent runtime state.

## Project overview

The repository is structured to support a layered runtime:

- Platform stack: config, manifests, logs, exports, renders
- Plugin stack: creative and rendering plugins
- AI model stack: model registry and checkpoints
- Database stack: local telemetry and knowledge storage
- Knowledge stack: semantic graph, styles, motion, and story data
- ClipPool stack: media and ratio-based pools
- Agent swarm: autonomous runtime agents

The main entrypoints are:

- `main.py` — command-line entry point
- `bootstrap.py` — environment and stack bootstrap
- `verify.py` — integrity verification
- `setup.sh` / `setup.ps1` — environment bootstrap helpers

## Quick start

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python bootstrap.py --root .
python verify.py --root .
python main.py --agent all --once
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python bootstrap.py --root .
python verify.py --root .
python main.py --agent all --once
```

### One-command setup helpers

```bash
bash setup.sh
```

```powershell
.\setup.ps1
```

## Supported commands

### Project bootstrap

```bash
python main.py --bootstrap
```

This invokes the stack manager to initialize the project structure and bootstrap runtime state.

### Integrity verification

```bash
python main.py --verify
```

This validates the project layout and required runtime paths.

### Single-cycle execution

```bash
python main.py --once
```

This runs a one-time agent cycle using the active config.

### Explicit agent run

```bash
python main.py --agent all --once
```

You can use `--agent` to target a specific agent or runtime mode.

## Repository structure

```text
beatsyndicat/
├── README.md
├── main.py
├── bootstrap.py
├── verify.py
├── setup.sh
├── setup.ps1
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.yaml
│   ├── defaults.json
│   └── goal_metrics.yaml
├── manifests/
│   ├── core.yaml
│   ├── ai.yaml
│   └── models.yaml
├── agents/
│   ├── __init__.py
│   └── base/
├── core/
│   ├── __init__.py
│   └── stack_manager.py
├── docs/
│   ├── BOOTSTRAP.md
│   └── TROUBLESHOOTING.md
├── database/
├── cache/
├── knowledge/
├── models/
├── logs/
├── output/
├── exports/
├── renders/
├── plugins/
├── clippool/
└── manifests/
```

## Configuration

The project relies on YAML and JSON configuration files under `config/` and stack definitions under `manifests/`.

Core config files:

- `config/settings.yaml` — runtime settings
- `config/defaults.json` — default values
- `config/goal_metrics.yaml` — project goals and thresholds

Manifest files:

- `manifests/core.yaml` — core stack definition
- `manifests/ai.yaml` — AI model configuration
- `manifests/models.yaml` — model registry metadata

## Development notes

- Python 3.10+ is the target runtime.
- Dependencies are managed through `requirements.txt`.
- Virtual environments are recommended for local work.
- The bootstrap scripts ensure base directories exist before running the project.

## Troubleshooting

If bootstrap or verification fails:

1. Confirm Python 3.10+ is installed.
2. Recreate the venv and reinstall requirements.
3. Run:

```bash
python bootstrap.py --root .
python verify.py --root .
```

4. Check the project directories under the repository root.
5. Review logs and configuration values in `config/` and `manifests/`.

## License and status

This project is a local automation scaffold and runtime template for a creative AI stack. It is intended to be extended with custom agents, models, pipeline logic, and project-specific workflows.

For day-to-day use, start with the setup commands above, then move into bootstrap + verify + agent cycle execution.
