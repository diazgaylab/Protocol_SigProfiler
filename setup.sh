#!/usr/bin/env bash

conda create --name sigprofiler -y python=3.10  pip 
conda activate sigprofiler
pip install SigProfilerMatrixGenerator SigProfilerSimulator SigProfilerClusters SigProfilerExtractor SigProfilerAssignment SigProfilerTopography SigProfilerPlotting

