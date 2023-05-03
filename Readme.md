# Taxonomy-Stats-Analysis
- An analysis of various statistics based on stats  from a raw fastq file, Kraken2 report and Bracken report as inputs.
- A python script- [Tax_Stats.py](https://gist.github.com/snehacodes15/2aa54187225b01f86c57d1b0c9264ad5) is run to get the- 1) Number of reads from a raw fastq file, 2) followed by calculating the no of classifed reads (under root) from a Kraken2 report, 3) Number of  unclassified reads in Kraken2 report, 4) Number of classified reads (under root) in Bracken report and finally 5) Number of unlassified reads in Bracken report (Kraken2 classified reads- Bracken classified reads). 

## The usage of the python script 
`usage- python3 tax_stats.py --file1 </path/to/kraken_report> --file2 </path/to/bracken report> --file3 </path/to/fastq file>`

## Kraken2 brief-

 Kraken2 is a k-mer based taxonomic classification system, which assigns taxonomic labes to DNA sequences. It functions based on exact k-mer matches- the classifier matches each k-mer within a query sequence to the lowest common ancestor (LCA) of all genomes containing the given k-mer. Kraken2 actually stores minimizers (l-mers) of each k-mer. The length of each l-mer must be ≤ the k-mer length. Each k-mer is treated by Kraken 2 as if its LCA is the same as its minimizer's LCA. Only minimizers of the k-mers in the query sequences are used as database queries. Similarly, only minimizers of the k-mers in the reference sequences in the database's genomic library are stored in the database. All k-mers are considered to have the same LCA as their minimizer's database LCA value.


## Brief explanation about the various fields in Kraken2 and Bracken report

- phanta_kraken2.report




