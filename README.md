# Protocol_SigProfiler

Runnable example for **"Profiling signatures of mutational processes using the SigProfiler suite"**
(Nature Protocols). It reproduces the analysis workflow described in the paper on a synthetic
dataset, so that the commands can be executed without obtaining the original PCAWG data.

## What this example covers

The protocol supports single-base substitutions (SBS), doublet-base substitutions (DBS), small
insertions and deletions (ID), copy-number alterations (CN) and structural variants (SV). Like any
protocol, it illustrates the workflow with one representative worked example rather than with every
supported combination. **This example uses SBS.**

| Protocol part | Steps | In this example |
|---|---|---|
| 1. Variant calling from BAM files | 1–4 | No — starts from pre-called mutations |
| 2. Mutation categorization | 5 | **Yes** |
| 2. Simulation and clustered mutations | 6, 7 | No — see *Steps that need real data* |
| 3. De novo signature extraction | 8, 9 | **Yes** (SBS-288 and SBS-1536) |
| 4. Decomposition into reference signatures | 10, 11 | **Yes** |
| 5. Assignment to samples and to mutations | 12, 13, 14 | **Yes** |
| 6. Topographical characterization | 15, 16 | No — see *Steps that need real data* |
| 7. Plotting | 17 | **Yes** |

### Steps that need real data

`step6.py`, `step7.py`, `step15.py` and `step16.py` are included for reference but are **not part of
the runnable example**, and `run_example.sh` does not call them.

SigProfilerClusters and SigProfilerTopography both compare the observed genomic distribution of
mutations against a simulated null background. A dataset produced by SigProfilerSimulator *is* that
null background, so it cannot demonstrate either method: there is no clustering to detect and no
departure from the background to measure. These branches need real somatic mutation data that
retains its native spatial distribution — for example, the PCAWG lung adenocarcinoma cohort from
which the synthetic data here were derived.

## Requirements

- Linux or macOS, with [Conda](https://conda.io) or Mamba
- ~30 CPU cores. The extraction steps are the reason this is not a laptop workload (see *Run time*)
- ~15 GB of free disk: the GRCh37 reference installed by `step5.py` takes ~6 GB inside the
  environment, and the outputs take a few GB more
- Network access on first run, to download the reference genome and the COSMIC catalogue

## Quick start

```bash
./setup.sh          # create the 'sigprofiler' Conda environment and install the suite
./run_example.sh    # run the example, from the repository root
```

`run_example.sh` runs every step through `conda run`, so it does not need an activated environment
and works from a batch job on a cluster. It stops at the first error.

To run a single step instead:

```bash
conda run --name sigprofiler --no-capture-output python step5.py
```

Scripts use paths relative to the repository root, so run them from there. `run_example.sh` changes
into the repository root itself.

## Input data

| File | Contents |
|---|---|
| `somatic_mutation_folder/LUAD_sim_data.maf` | 1,338,192 SBS mutations across 37 samples, in MAF format with genomic coordinates (104 MB) |
| `refitting_example.txt` | SBS-96 matrix for 2 samples (588 and 567 mutations), used by `step13.py` |

Both were generated with SigProfilerSimulator from the 37 PCAWG lung adenocarcinomas analysed in the
paper, simulating in the SBS-6144 context. Because the simulator randomises the genomic positions of
the mutations while preserving their mutational profile, the SBS-96 and SBS-1536 matrices derived
from this dataset are identical to those of the original tumours, and SBS-288 differs by 6
mutations out of 1,338,192.

The files contain SBS records only: no indels, and only a small number of derived DBS events across
the whole cohort.

## What the example produces

Every directory below is created by the run and is excluded from version control.

```
LUAD_res/                                   step5   mutational matrices (SBS, DBS) + GRCh37 install
LUAD_US_extraction_288/                     step8   de novo extraction, SBS-288 context
LUAD_US_extraction_1536/                    step8   de novo extraction, SBS-1536 context
LUAD_US_decomposition/                      step10  naive decomposition into COSMIC signatures
LUAD_US_optimized_decomposition/            step11  decomposition excluding signature subgroups
LUAD_de_novo_decomposition/                 step12  de novo signatures assigned to samples
LUAD_cosmic_refitting/                      step13  full COSMIC catalogue refitted to 2 samples
LUAD_decomposed_assignment_to_mutations/    step14  per-mutation signature probabilities
LUAD_plots/                                 step17  SBS-96 and SBS-288 profile plots
```

`step14.py` also creates `somatic_mutation_folder/input/` and `somatic_mutation_folder/output/`.
These are intermediate files, not results; delete them before re-running if you want a clean start.

Reference results for the main steps are archived in `expected_output.zip`.

## Run time

Measured on the 37-sample dataset, as reported in the paper:

| Steps | Time |
|---|---|
| 5 — matrix generation | < 10 min |
| 8 — extraction, SBS-288 | ~2 h on 30 CPU, ~2 h on one A100 GPU |
| 8 — extraction, SBS-1536 | ~12 h on 30 CPU, ~5 h on one A100 GPU |
| 10, 11 — decomposition | ~1 h |
| 12, 13, 14 — assignment | < 10 min |
| 17 — plotting | < 10 min |

The extraction steps dominate. Both use `cpu=30, gpu=False`; set `gpu=True` in `step8_288.py` and
`step8_1536.py` to use a GPU.

## Comparing your results with the archived output

De novo extraction uses stochastic NMF optimisation, so exact values will not reproduce. Signature
counts, extracted profiles and assigned exposures should be very close; per-signature stability
scores and the last decimal places of activities will differ between runs. Treat a different
*number* of selected signatures as a result worth investigating, and small numerical differences as
expected.

## Relationship to the figures in the paper

**The figures in the paper come from the original PCAWG tumours, not from this example.** The
synthetic dataset demonstrates that the workflow runs; it does not reproduce the published results.

Three things are worth knowing before you compare:

- Signature extraction and assignment do reproduce the original results: the SBS-96 and SBS-1536
  matrices derived from this dataset are identical to those of the original tumours, and SBS-288
  differs by six mutations out of 1,338,192.
- Figure 4b shows a **manually selected** six-signature solution for SBS-1536; the automatic
  suggestion is four signatures, here and with the original data alike. Step 9 of the protocol
  explains that choice.
- Figure 2 shows clustered mutations from the original tumours and cannot be reproduced from this
  example at all, for the reason given under *Steps that need real data*.

## Troubleshooting

**`conda: command not found`** — Conda is not on `PATH`. Install Miniconda, or load the module that
provides it on your cluster.

**A step cannot find its input** — the scripts use relative paths. Run them from the repository
root, or use `run_example.sh`, which changes into it.

**Results differ from `expected_output.zip`** — see *Comparing your results with the archived
output*. Check the package versions first: different SigProfiler releases default to different
COSMIC catalogue versions.

**A rerun behaves differently from the first run** — delete the generated directories listed under
*What the example produces*, including `somatic_mutation_folder/input/` and
`somatic_mutation_folder/output/`.
