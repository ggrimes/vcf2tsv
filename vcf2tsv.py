#!/usr/bin/env python
import vcf

def main(vcf_path, tsv_path):
    # Extract the INFO and FORMAT field tags and write them as additional columns to the header row
    with open(vcf_path, 'r') as vcf_file:
        vcf_reader = vcf.Reader(vcf_file)
        info_tags = set()
        format_tags = set()
        for record in vcf_reader:
            info_tags.update(record.INFO.keys())
            for sample in record.samples:
                format_tags.update(sample.data._fields)

    # Open the VCF file and TSV file
    with open(vcf_path, 'r') as vcf_file, open(tsv_path, 'w') as tsv_file:
        vcf_reader = vcf.Reader(vcf_file)

        # Write the header row to the TSV file
        tsv_file.write("CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER")

        for tag in sorted(info_tags):
            tsv_file.write(f"\t{tag}")

        for sample in vcf_reader.samples:
            for tag in sorted(format_tags):
                tsv_file.write(f"\t{sample}_{tag}")

        # Write each variant record to the TSV file
        for record in vcf_reader:
            tsv_file.write(f"\n{record.CHROM}\t{record.POS}\t{record.ID}\t{record.REF}\t{','.join(map(str, record.ALT))}\t{record.QUAL}\t{record.FILTER}")
            for tag in sorted(info_tags):
                if tag in record.INFO:
                    tsv_file.write(f"\t{record.INFO[tag]}")
                else:
                    tsv_file.write("\t")

            for sample in record.samples:
                sample_dict = sample.data._asdict()
                for tag in sorted(format_tags):
                    if tag in sample_dict:
                        tsv_file.write(f"\t{sample_dict[tag]}")
                    else:
                        tsv_file.write("\t")
                        
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert a VCF file to a TSV file.')
    parser.add_argument('vcf_file', metavar='vcf_file', type=str, help='input VCF file path')
    parser.add_argument('tsv_file', metavar='tsv_file', type=str, help='output TSV file path')
    args = parser.parse_args()

    main(args.vcf_file, args.tsv_file)
