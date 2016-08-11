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
	
x = 0	

gene = infile1.split(".fa.aln")[0]
output_file = "Permutation_row_files/" + gene + "_permutations_by_row.tab"

with open(output_file,"a") as output:
	output.write(gene)
	output.write("\t")

with open(infile1,"rU") as input_file:	
	
	for row2 in input_file:
		if '" "' in row2:
			next_row = input_file.next()
			next_row2 = input_file.next()
			pi = next_row2.split('" ')[1]
			pi = pi.split("\n")[0]
			x = x + 1
			#print x

			with open(output_file,"a") as output:

				output.write(pi)
				output.write("\t")
				
with open(output_file,"a") as output:	
	output.write("\n")
