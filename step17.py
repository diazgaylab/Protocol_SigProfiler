import sigProfilerPlotting as sigPlt

sigPlt.plotSBS("LUAD_res/SBS/LUAD_US.SBS96.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "96",
			   percentage = False)

sigPlt.plotSBS("LUAD_res/SBS/LUAD_US.SBS288.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "288",
			   percentage = False)
