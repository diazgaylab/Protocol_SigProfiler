from SigProfilerAssignment import Analyzer as Analyze

Analyze.decompose_fit("LUAD_res/SBS/LUAD_US.SBS288.all", 
					  "LUAD_US_optimized_decomposition", 
					  signatures = "LUAD_US_extraction/SBS288/Suggested_Solution/SBS288_De-Novo_Solution/Signatures/SBS288_De-Novo_Signatures.txt", 
					  genome_build = "GRCh37", 
					  exclude_signature_subgroups = ["MMR_deficiency_signatures","POL_deficiency_signatures","HR_deficiency_signatures", "UV_signatures"])
