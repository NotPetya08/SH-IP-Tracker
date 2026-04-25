#!/bin/bash
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
$SCRIPT_PATH/venv/bin/python3 $SCRIPT_PATH/tracker.py
