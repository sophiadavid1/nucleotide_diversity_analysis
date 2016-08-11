This repository includes scripts used in the publication:

David S, Rusniok C, Mentasti M, Gomez-Valero L, Harris SR, Lechat P, Lees J, Ginevra C, Glaser P, Ma L, Bouchier C, Underwood A, Jarraud S, Harrison TG, Parkhill J, Buchrieser C. Multiple major disease-associated clones of Legionella pneumophila have emerged recently and independently.

A combination of R and Python scripts were used to test whether any core genes belonging to Legionella pneumophila have a higher than expected nucleotide similarity amongst five strains of interest with respect to a collection of 24 strains representative of the species diversity. This is given the phylogenetic relatedness of the five strains and the overall conservation of each gene across the species.


The scripts below have been developed and tested in a local system. A user-friendly all-in-one version of these scripts available for outside use is in development.


-----


Step 1:

Calculate the nucleotide diversity (pi) value for each individual core gene alignment of the five strains of interest. The directory in which the script is run should contain all core gene alignments comprising only the five strains with the file endings ".fasta".

Rscript step1_calculate_pi_values_for_five_STs_of_interest.R

This creates a file called "Nucleotide_diversity_five_STs_of_interest.txt".


Step 2:

Adjust the previously calculated nucleotide diversity values by dividing each value by the median value for all core genes. This script uses the output file created in step 1 and should be run in the same directory as this file.

python step2_adjust_pi_values_five_strains.py

This creates a file called "Adjusted_nucleotide_diversity_values_five_STs_of_interest.txt".


Step 3:

Calculate the nucleotide diversity values for each core gene and for all possible combinations of five strains within the set of species representatives. Given 24 strains (including the five strains of interest), a total of 42504 possible combinations exist. The input to the script is the individual core gene alignment containing the sequence for all species representatives. This script runs on each gene alignment separately and thus must be parallelised (e.g. with a bash loop). 

Rscript step3_get_permutations_of_core_genes.R [gene alignment]

This creates a file ending in ".permutations.txt" for each core gene.


Step 4:

Process the "*permutations.txt" files. This script runs on each "*permutations.txt" file separately and thus must be parallelised.

python step4_make_table_row_for_each_gene.py [*permutations.txt file]

This creates an individual tab-limited row of text for each gene containing the pi values for all possible combinations of five strains. Each file is created inside a directory called "Permutation_row_files". All files are then concatenated with a bash command to create a large table (with the number of lines equal to the number of core genes).


Step 5:

Create a header row for the table which labels each column with the particular strain combination.

python step5_make_title_row_for_table.py

This is merged with the large table created in step 4 using a bash command.


Step 6:

Calculate the median nucleotide diversity per gene for all possible combinations of five strains from the set of species representatives. This script uses the table generated in step 5.

python step6_get_median_for_each_combo.py

This creates a file "Median_pi_values_for_all_combos.tab".


Step 7:

Adjust all nucleotide diversity values by dividing each value by the median value of all core genes for the particular strain combination, as obtained in step 6. This script runs on each *permutations.txt file separately and thus must be parallelised.

python step7_adjust_all_pi_values.py [*permutations.txt file]

This creates a file ending in "permutations_over_median_pi.tab" for each core gene contained within the directory "Permutation_over_median_pi_files".


Step 8:

Compare the adjusted pi values for the five strains of interest with those generated from testing all possible combinations of five strains from the set of species representatives, and derive p-values. This script runs on each *permutations_over_median_pi.tab file separately and thus must be parallelised.

python calculate_p_values.py [*permutations_over_median_pi.tab file]

This creates a file "p_values.tab".

----
