from SigProfilerAssignment import Analyzer as Analyze

Analyze.cosmic_fit("refitting_example.txt",
				   "LUAD_cosmic_refitting",
				   input_type = "matrix",
				   context_type = "96",
				   genome_build = "GRCh37",
				   export_probabilities_per_mutation = False,
				   collapse_to_SBS96 = False)
