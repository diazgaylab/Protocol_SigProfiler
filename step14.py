from SigProfilerAssignment import Analyzer as Analyze

Analyze.cosmic_fit("somatic_mutation_folder", 
				   "LUAD_decomposed_assignment_to_mutations", 
				   input_type = "vcf", 
				   context_type= "288", 
				   signature_database = "LUAD_US_optimized_decomposition/Decompose_Solution/Signatures/Decompose_Solution_Signatures.txt", 
				   genome_build = "GRCh37",
				   export_probabilities_per_mutation = True,
                   collapse_to_SBS96 = False)
