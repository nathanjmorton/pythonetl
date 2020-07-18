import os
directory = os.listdir('/mnt/data')
print(directory)


#input file
fin = open("./data/out.txt", "rt")
#output file to write the result to
fout = open("./data/transformed.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace(", '%Y-%m-%d %H:%i:%s')", ""))

#close input and output files
fin.close()
fout.close()




