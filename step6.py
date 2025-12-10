from SigProfilerSimulator import SigProfilerSimulator as sigSim

sigSim.SigProfilerSimulator("LUAD_US", 
							"LUAD_res", 
							"GRCh37", 
							contexts = ["288"], 
							simulations = 100, 
							chrom_based=True)
