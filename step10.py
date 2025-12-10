from SigProfilerAssignment import Analyzer as Analyze

Analyze.decompose_fit("LUAD_res/SBS/LUAD_US.SBS288.all", 
					  "LUAD_US_decomposition", 
					  signatures = "LUAD_US_extraction/SBS288/Suggested_Solution/SBS288_De-Novo_Solution/Signatures/SBS288_De-Novo_Signatures.txt", 
					  genome_build = "GRCh37")
