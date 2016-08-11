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


output_file = infile1.split(".txt")[0]
output_file = "Permutation_over_median_pi_files/" + output_file + "_over_median_pi.tab"

with open(infile1,"rU") as input_file:
	for row in input_file:
		if '" "' in row:
			row = row.split("\n")
			five_sts = row[0].split('"')[3]
			each_sts = five_sts.split(" ")

			five_sts_concat = ""

			for st in each_sts:
				st = st.split("_")[0]
				five_sts_concat = five_sts_concat + st + "_"

			#print five_sts_concat

			next_row = input_file.next()
			next_row2 = input_file.next()
			pi = next_row2.split('" ')[1]
			pi = float(pi)
			
			average_pi = "NA"
			pi_over_average = "NA"

			with open("Median_pi_values_for_all_combos.tab","rU") as input_file2:
				reader = csv.reader(input_file2,delimiter="\t")
				for row in reader:
					st_combo = row[0]

					if five_sts_concat == st_combo:
						average_pi = row[1]
						average_pi = float(average_pi)
						
						if average_pi == 0:
							pi_over_average = "NA"
							print st_combo
						else:
					
							pi_over_average = pi/average_pi
							pi_over_average = str(pi_over_average)
						break

			with open(output_file,"a") as output:
				output.write(five_sts_concat)
				output.write("\t")
				output.write(pi_over_average)
				output.write("\n")

				
				
				
				
