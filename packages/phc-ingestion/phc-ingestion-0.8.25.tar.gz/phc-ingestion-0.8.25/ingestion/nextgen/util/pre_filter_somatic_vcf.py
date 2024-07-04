from logging import Logger

from ingestion.shared_util.open_maybe_gzipped import open_maybe_gzipped


def build_variant_key_from_vcf_line(line: str) -> str:
    split_line = line.strip().split("\t")
    chrom, pos, ref, alt = split_line[0], split_line[1], split_line[3], split_line[4]
    return f"{chrom}:{pos}:{ref}:{alt}"


def pre_filter_somatic_vcf(
    somatic_vcf_file: str,
    somatic_vcf_snv_file: str,
    somatic_vcf_indel_file: str,
    working_dir: str,
    log: Logger,
) -> str:
    """
    Removes all variants from the `somatic_vcf_file` that are not
    also in the `somatic_vcf_snv_file` or `somatic_vcf_indel_file`.
    """
    log.info("Pre-filtering somatic VCF file")

    valid_variant_keys = set()
    with open_maybe_gzipped(somatic_vcf_snv_file, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            valid_variant_keys.add(build_variant_key_from_vcf_line(line))
    with open_maybe_gzipped(somatic_vcf_indel_file, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            valid_variant_keys.add(build_variant_key_from_vcf_line(line))

    log.info(f"Found {len(valid_variant_keys)} valid variants")

    output_vcf_path = f"{working_dir}/filtered_somatic.vcf.gz"
    with (
        open_maybe_gzipped(somatic_vcf_file, "rt") as f,
        open_maybe_gzipped(output_vcf_path, "wt") as w,
    ):
        for line in f:
            if line.startswith("#"):
                w.write(line)
            else:
                if build_variant_key_from_vcf_line(line) in valid_variant_keys:
                    w.write(line)

    log.info(f"Successfully pre-filtered somatic VCF file to {output_vcf_path}")
    return output_vcf_path
