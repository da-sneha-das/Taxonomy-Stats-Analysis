# Taxonomy-Stats-Analysis
An analysis of various statistics based on stats  from a raw fastq file, Kraken2 report and Bracken report

#usage- python3 tax_stats.py --file1 </path/to/kraken_report> --file2 </path/to/bracken report> --file3 </path/to/fastq file>


import argparse 
import pandas as pd
parser = argparse.ArgumentParser(prog ='tax_stats.py', description='Python script to calculate the number of reads from a fastq file, no of Kraken2 classified and unclassified reads and no of Bracken classified and unclassified reads.')
parser.add_argument('--file1',  help='phanta_kraken2.report as input file')  
parser.add_argument('--file2', help = 'phanta_bracken_species.report')
parser.add_argument('--file3', help ='takes a fastq file as input')
args = parser.parse_args()
#Kraken2-report
df = pd.read_csv(args.file1, sep='\t', header=None)

#kraken2_report -> total reads classified under root
root_check = df.iloc[1,3]
if root_check =="R":
    df.at[0,'kraken2_reads']= df.iloc[1,1]
	
#kraken2_report -> total reads unclassified by kraken2
unclassified_check = df.iloc[0,3]
if unclassified_check =="U":
    df.at[0,'unclassified_Kraken2_reads']= df.iloc[0,2]    

#Bracken_report
df2 = pd.read_csv(args.file2, sep='\t', header=None)

#Bracken_report -> total reads classified by Bracken
root_classified_check = df2.iloc[0,3]
if  root_classified_check=="R":
    df2.at[0,'Bracken_classified_reads']= df2.iloc[0,1]

new_df = pd.concat([df['kraken2_reads'],df['unclassified_Kraken2_reads'],df2['Bracken_classified_reads']],axis=1)

#Calculating Bracken unclassified reads-
#Formula = No of reads classified by Kraken2-no of reads classified by Bracken
new_df.at[0,'Bracken_unclassified_reads'] = new_df['kraken2_reads'][0]-new_df['Bracken_classified_reads'][0]

#Calculating the no of reads in a fastq file
with open(args.file3, 'r') as fp:
        x = len(fp.readlines())
        fastq_reads = x/4
new_df.at[0,'Fastq_reads'] = fastq_reads
new_df.to_csv(r'C:\Users\sneha\OneDrive\Desktop\jagan_nb06\Tax_reads_stats.csv')
