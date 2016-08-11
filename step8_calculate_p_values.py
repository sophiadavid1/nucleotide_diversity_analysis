import csv
import glob
import sys
import getopt



def getOptions(arg):
	
	try:
		opts, args = getopt.getopt(argv, "h", ["help"])
	except getopt.GetoptError:
		print "Option Error!", argv
		Usage()
		sys.exit(2)
		
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			Usage()
			sys.exit()
			
	if len(args) < 1:
		Usage()
		sys.exit()
		
	infile1 = args[0]
	
	return infile1
	

if __name__ == "__main__":
        argv=sys.argv[1:]
        infile1 =getOptions(argv)


gene = infile1.split("_24.fa.aln")[0]
gene = gene.split("files/")[1]

print gene

adjusted_pi_list = []

with open(infile1,"rU") as input_file:
	reader = csv.reader(input_file,delimiter="\t")
	for row in reader:
		five_st_combo = row[0]
		adjusted_pi = row[1]
		if adjusted_pi != "NA":
			adjusted_pi = float(adjusted_pi)
			adjusted_pi_list.append(adjusted_pi)

print len(adjusted_pi_list)

if len(adjusted_pi_list) == 42503:

	with open("Adjusted_nucleotide_diversity_values_five_STs_of_interest.tab","rU") as input_file2:
		reader2 = csv.reader(input_file2,delimiter="\t")
		for row2 in reader2:
			corby_gene = row2[0]
			corby_gene = corby_gene.split(".fa.aln")[0]
			print corby_gene
			pi_in_five_sts = row2[1]
			pi_in_five_sts = float(pi_in_five_sts)
			

			if gene == corby_gene:
			
				print pi_in_five_sts

				over_group = 0
				under_group = 0

				for each in adjusted_pi_list:
					each = float(each)
					if each > pi_in_five_sts:
						over_group = over_group + 1
					if each <= pi_in_five_sts:
						under_group = under_group + 1

				over_group = float(over_group)
				under_group = float(under_group)
				
				print over_group
				print under_group

				p_value = under_group/42503
				p_value = str(p_value)

				with open("p_values.tab","a") as output:
					output.write(gene)
					output.write("\t")
					output.write(p_value)
					output.write("\n")


			
			
