# ffmpeg-live-transcoder-docker

Dockerized RTMP to HLS ABR transcoding pipeline.

## Overview
This repository is a small but legitimate FFmpeg-focused MVP. It uses local `ffmpeg` / `ffprobe` binaries, keeps defaults conservative, and avoids destructive behavior.

## Features
- Purpose-built CLI/service for this repository's use-case
- Safe-by-default workflow and explicit outputs
- Minimal codebase that is easy to extend
- Uses FFmpeg/ffprobe via subprocess or exec wrappers

## Requirements
- FFmpeg and ffprobe in `PATH`
- Python 3.11+

## Setup
```bash
cd ffmpeg-live-transcoder-docker
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Usage Examples
```bash
python3 app.py --help
```

## Configuration
- Prefer CLI flags for one-off runs
- Some repos include `config.example.json` for future extension
- Review paths and outputs before long-running jobs

## Output Notes
- Outputs are only written to the files/directories you specify
- Logs go to stdout/stderr unless the tool documents otherwise

## Limitations
- MVP-sized implementation, not a full media platform
- Assumes local FFmpeg availability
- Some advanced workflows are intentionally simplified

## Safety Notes
- Test against sample media first
- Prefer dry-run mode when available
- Validate input URLs and destination paths before long jobs
