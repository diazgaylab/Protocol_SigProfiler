from SigProfilerAssignment import Analyzer as Analyze

Analyze.cosmic_fit("LUAD_res/SBS/LUAD_US.SBS288.all", 
				   "LUAD_de_novo_decomposition", 
				   input_type = "matrix", 
				   context_type= "288", 
				   signature_database = "LUAD_US_extraction/SBS288/Suggested_Solution/SBS288_De-Novo_Solution/Signatures/SBS288_De-Novo_Signatures.txt", 
				   genome_build = "GRCh37", 
				   export_probabilities_per_mutation = False, 
				   collapse_to_SBS96 = False)

