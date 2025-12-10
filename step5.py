######### Genome version installation
from SigProfilerMatrixGenerator import install as genInstall
genInstall.install('GRCh37')

######### Matrix generation
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen
matGen.SigProfilerMatrixGeneratorFunc("LUAD_US", 
									  "GRCh37", 
									  "somatic_mutation_folder", 
									  output_directory = "LUAD_res")

