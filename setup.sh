#!/usr/bin/env bash

set -euo pipefail

conda create --name sigprofiler -y python=3.10 pip
conda run --name sigprofiler --no-capture-output pip install SigProfilerMatrixGenerator SigProfilerSimulator SigProfilerClusters SigProfilerExtractor SigProfilerAssignment SigProfilerTopography SigProfilerPlotting
