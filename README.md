# VCF to TSV converter

This program converts a VCF file to a TSV file, with each INFO field tag and FORMAT field tag as a separate column.

## Installation

To install the program, you need Python 3 and the `pyvcf` package. You can install the package using pip:

pip install pyvcf


## Usage

To convert a VCF file to a TSV file, run the `vcf2tsv.py` script with the path to the input VCF file and the path to the output TSV file as arguments:

python vcf2tsv.py input.vcf output.tsv


You can also run the script without arguments to see the command line help:

python vcf2tsv.py --help


The output TSV file will have the following columns:

- CHROM
- POS
- ID
- REF
- ALT
- QUAL
- FILTER

For each INFO field tag in the input VCF file, there will be an additional column with the tag name as the header.

For each FORMAT field tag in the input VCF file, there will be an additional column for each sample in the VCF file, with the sample name and tag name separated by an underscore as the header.

## Command line arguments

- `vcf_file`: The path to the input VCF file.
- `tsv_file`: The path to the output TSV file.
