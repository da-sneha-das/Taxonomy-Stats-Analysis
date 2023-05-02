# Taxonomy-Stats-Analysis
- An analysis of various statistics based on stats  from a raw fastq file, Kraken2 report and Bracken report as inputs.
- A python script- tax_stats.py is run to get the- 1) Number of reads from a raw fastq file, 2) followed by calculating the no of classifed reads (under root) from a Kraken2 report, 3) Number of  unclassified reads in Kraken2 report, 4) Number of classified reads (under root) in Bracken report and finally 5) Number of unlassified reads in Bracken report (Kraken2 classified reads- Bracken classified reads). 

## The usage of the python script 
`usage- python3 tax_stats.py --file1 </path/to/kraken_report> --file2 </path/to/bracken report> --file3 </path/to/fastq file>`

## Brief explanation about the various fields in Kraken2 and Bracken report



