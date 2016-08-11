library(pegas)
library(ape)

file.names <- dir(pattern=".fasta")

for(i in 1:length(file.names)){
	gene <- read.dna(file.names[i],format="fasta",as.matrix=FALSE)
	output <- "Nucleotide_diversity_five_STs_of_interest.txt"
	pi <- nuc.div(gene)
	write.table(file.names[i],file=output,append=TRUE)
	write.table(pi,file=output,append=TRUE)
	
}
