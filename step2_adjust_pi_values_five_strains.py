import csv


with open("Nucleotide_diversity_five_STs_of_interest.txt") as input_file:
	reader = csv.reader(input_file,delimiter="\t")
	for row in reader:
		if "LPC" not in row[0]:
			if "x" not in row[0]:
				print row[0]
				pi = row[0].split("1 ")[1]
				pi = float(pi)
				
				adjusted_pi = pi/0.01328805
				adjusted_pi = str(adjusted_pi)
				
				with open("Adjusted_nucleotide_diversity_values_five_STs_of_interest.txt","a") as output:
					output.write(adjusted_pi)
					output.write("\n")
