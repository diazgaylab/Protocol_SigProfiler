from SigProfilerExtractor import sigpro as sig

if __name__ == "__main__":
	sig.sigProfilerExtractor("matrix", "LUAD_US_extraction_288", "LUAD_res/SBS/LUAD_US.SBS288.all", reference_genome="GRCh37", minimum_signatures=1, maximum_signatures=10, nmf_replicates=100, cpu=30, gpu=False)
