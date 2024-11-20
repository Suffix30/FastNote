#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

if [ -z "$1" ]; then
    echo "Usage: $0 <script.py>"
    exit 1
fi

python3 "$1"