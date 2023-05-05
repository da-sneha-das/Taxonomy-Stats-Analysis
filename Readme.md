# Taxonomy-Stats-Analysis
- An analysis of various statistics based on stats  from a raw fastq file, Kraken2 report and Bracken report as inputs.
- A python script- [Tax_Stats.py](https://gist.github.com/snehacodes15/2aa54187225b01f86c57d1b0c9264ad5) is run to get the- 1) Number of reads from a raw fastq file, 2) followed by calculating the no of classifed reads (under root) from a Kraken2 report, 3) Number of  unclassified reads in Kraken2 report, 4) Number of classified reads (under root) in Bracken report and finally 5) Number of unlassified reads in Bracken report (Kraken2 classified reads- Bracken classified reads). 

## The usage of the python script 
`usage- python3 tax_stats.py --file1 </path/to/kraken_report> --file2 </path/to/bracken report> --file3 </path/to/fastq file>`

## Kraken2 brief-

 Kraken2 is a k-mer based taxonomic classification system, which assigns taxonomic labels to DNA sequences. It functions based on exact k-mer matches- the classifier matches each k-mer within a query sequence to the lowest common ancestor (LCA) of all genomes containing the given k-mer. Kraken2 actually stores minimizers (l-mers) of each k-mer. The length of each l-mer must be ≤ the k-mer length. Each k-mer is treated by Kraken 2 as if its LCA is the same as its minimizer's LCA. Only minimizers of the k-mers in the query sequences are used as database queries. Similarly, only minimizers of the k-mers in the reference sequences in the database's genomic library are stored in the database. All k-mers are considered to have the same LCA as their minimizer's database LCA value. By default, the values of 
 and are 35 and 31 respectively.


## Brief explanation about the various fields in Kraken2 and Bracken report

- phanta_kraken2.report

![Screenshot 2023-05-05 150954](https://user-images.githubusercontent.com/129862776/236425422-31f2a040-931a-4f9b-8ba8-89d2c4368f19.jpg)

- The above is an example of standard Kraken2 sample report format. It is tab-delimited with one line per taxon.
- The fields of the output, from left to right-
1. Percentage of the fragments covered by the claded rooted at this taxon (Reads)
2. Number of fragments covered by the clade rooted at this taxon
3. Number of fragments assigned directly to this taxon
4. A rank code, indicating (U)nclassified, (R)oot, (D)omain, (K)ingdom, (P)hylum, (C)lass, (O)rder, (F)amily, (G)enus, or (S)pecies. Taxa that are not at any of these 10 ranks have a rank code that is formed by using the rank code of the closest ancestor rank with a number indicating the distance from that rank. E.g., "G2" is a rank code indicating a taxon is between genus and species and the grandparent taxon is at the genus rank.
5. NCBI taxonomic ID number
6. Indented scientific name
-By default, taxa with no reads assigned to (or under) them will not have any output produced.

## Braken 
- Bracken is a companion program to Kraken 1, KrakenUniq, or Kraken 2 While Kraken classifies reads to multiple levels in the taxonomic tree, Bracken allows estimation of abundance at a single level using those classifications (e.g. Bracken can estimate abundance of species within a sample).
- Unclassified reads will not be included in the report.
