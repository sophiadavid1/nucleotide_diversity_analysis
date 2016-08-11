import csv
import glob


with open("Title_row_for_table.tab","a") as output:
	output.write("\t")
	output.close()
	

with open("LPC_3318_27.fa.aln_permutations.txt","rU") as input_file2:


        for row2 in input_file2:
                if '" "' in row2:

                        row2 = row2.split("\n")
                        five_sts2 = row2[0].split('"')[3]
                        each_sts2 = five_sts2.split(" ")

                        five_sts_concat2 = ""

                        for st2 in each_sts2:
                                st2 = st2.split("_")[0]
                                five_sts_concat2 = five_sts_concat2 + st2 + "_"

                        #print five_sts_concat2
			
			with open("Title_row_for_table.tab","a") as output:
				output.write(five_sts_concat2)
				output.write("\t")
	

with open("Title_row_for_table.tab","a") as output:
	output.write("\n")
	output.close()
