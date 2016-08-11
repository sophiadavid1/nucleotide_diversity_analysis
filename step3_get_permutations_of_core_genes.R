library(ape)
library(gtools)
library(pegas)

args <- commandArgs(TRUE)

file_name <- args[1]

file.names <- dir(pattern=file_name)

for(i in 1:length(file.names)){
	gene <- read.dna(file.names[i],format="fasta",as.matrix=FALSE)
	output <- paste(file.names[i],"permutations.txt",sep="_")
	gene_names <- names(gene)
	combs <- combinations(27,5,gene_names,repeats.allowed=FALSE)
	nuc <- apply(combs,1,function(x){
		bu<-which(names(gene) %in% x)
		subseq<-gene[bu]
		pi <- nuc.div(subseq)
		STs <- paste(x,collapse=" ")
		write.table(STs,file=output,append=TRUE)
		write.table(pi,file=output,append=TRUE)
		
	})
}
