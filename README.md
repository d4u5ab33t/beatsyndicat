# BeatSyndicat project configuration
project:
  name: beatsyndicat
  version: 10.0.0
  release: Genesis
  root: .
  timezone: UTC
  sacred_drop: "13:28"
  sacred_gap: "04:20"
  enabled: true
  active_stacks:
    - platform
    - plugin
    - ai_models
    - database
    - knowledge
    - clippool
    - agent_swarm

paths:
  root: .
  config: config
  manifests: manifests
  agents: agents
  packages: packages
  cache: cache
  database: database
  logs: logs
  output: output
  exports: exports
  renders: renders
  models: models
  plugins: plugins
  knowledge: knowledge
  clippool: clippool

runtime:
  python_version: "3.10+"
  env_file: .env
  log_level: INFO

bootstrap:
  create_virtualenv: true
  install_requirements: true
  run_verify: true

platforms:
  default: local
  allowed:
    - local
    - linux
    - windows
    - wsl

stack_manifest:
  platform:
    description: Core runtime, config, logs, and metadata
    directories:
      - config
      - manifests
      - logs
      - renders
      - exports
      - projects/demo
  plugin:
    description: Creative plugin library
    directories:
      - plugins/vision
      - plugins/story
      - plugins/music
      - plugins/physics
      - plugins/render
      - plugins/training
      - plugins/export
      - plugins/quality
      - plugins/style
  ai_models:
    description: AI model registry and checkpoints
    directories:
      - models/clip
      - models/siglip
      - models/dinov2
      - models/yolo
      - models/sam2
      - models/whisper
      - models/scenedetect
      - models/beatsync
      - models/cutclaw
  database:
    description: Local telemetry and knowledge DB
    directories:
      - database
  knowledge:
    description: Semantic graph, stories, style and motion knowledge
    directories:
      - knowledge/knowledge
      - knowledge/semantic
      - knowledge/story
      - knowledge/style
      - knowledge/motion
      - knowledge/color
  clippool:
    description: Multi-ratio media pool
    directories:
      - clippool/16_9
      - clippool/9_16
      - clippool/1_1
      - clippool/new
  agent_swarm:
    description: Autonomous agent runtime and telemetry
    directories:
      - agents/scout
      - agents/analyst
      - agents/bridge
      - agents/cartographer
      - agents/oracle
      - agents/autopsy
