# This script can only be run with real data; it cannot be run with the synthetic
# example data provided in this repository, which is a simulated null background.

from SigProfilerSimulator import SigProfilerSimulator as sigSim

sigSim.SigProfilerSimulator("LUAD_US", 
							"LUAD_res", 
							"GRCh37", 
							contexts = ["288"], 
							simulations = 100, 
							chrom_based=True)
