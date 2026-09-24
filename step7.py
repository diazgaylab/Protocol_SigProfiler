# This script can only be run with real data; it cannot be run with the synthetic
# example data provided in this repository, which is a simulated null background.

from SigProfilerClusters import SigProfilerClusters as sigCl

sigCl.analysis("LUAD_US", 
			   "GRCh37", 
			   "96", 
			   ["96"], 
			   "LUAD_res/", 
			   subClassify=True)
