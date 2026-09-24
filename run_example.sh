#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

for script in step5.py step8_288.py step8_1536.py step10.py step11.py step12.py step13.py step14.py step17.py; do
	echo "==> $script"
	conda run --name sigprofiler --no-capture-output python "$script"
done
