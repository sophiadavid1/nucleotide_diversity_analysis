import csv
import os, sys, getopt, random, math
from optparse import OptionParser, OptionGroup
import os.path
from Bio import SeqIO
import glob
import shutil



def main():

	usage = "usage: %prog [options]"
	parser = OptionParser(usage=usage)
	
	parser.add_option("-n",action="store",dest="start",help="start value",metavar="")

	return parser.parse_args()


if __name__ == "__main__":
	
	(options,args) = main()


start_no = int(options.start)
end_no = int(options.start) + 50

pi_range = range(start_no,end_no)

for x in pi_range:
	pi_list = []
	st_combo = ""

	with open("Giant_table_of_pi_values_with_header.tab","rU") as input_file:
		reader = csv.reader(input_file,delimiter="\t")
		for row in reader:
			
			pi = row[x]
			#print pi
			if "_" in pi:
				st_combo = pi
			else:
				pi = float(pi)
				pi_list.append(pi)
		#print len(pi_list)

		#mean_pi = sum(pi_list)/len(pi_list)
		#mean_pi = str(mean_pi)
		pi_list.sort()
		if len(pi_list) % 2 == 1:
			median_pi = pi_list[len(pi_list)/2]
		else:
			median_pi = (pi_list[len(pi_list)/2]+pi_list[len(pi_list)/2-1])/2.0
		
		median_pi = str(median_pi)
		
		with open("Median_pi_values_for_all_combos.tab","a") as output:
			output.write(st_combo)
			output.write("\t")
			output.write(median_pi)
			output.write("\n")
		
		
			
