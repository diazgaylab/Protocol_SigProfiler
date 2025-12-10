from SigProfilerClusters import SigProfilerClusters as sigCl

sigCl.analysis("LUAD_US", 
			   "GRCh37", 
			   "96", 
			   ["96"], 
			   "LUAD_res/", 
			   subClassify=True)
