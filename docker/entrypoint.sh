#!/bin/bash --login

set -euo pipefail
/src/bin/main -N 100 -K 2 -T 100 -p "$@"