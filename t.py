import os
directory = os.listdir('/mnt/data')
print(directory)


#input file
fin = open("./data/data.txt", "rt")
#output file to write the result to
fout = open("./data/out.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace("STR_TO_DATE(", ""))
f2in = open("./data/out.txt", "rt")
f2out = open("./data/transformed.txt", "wt")
for line in f2in:
	f2out.write(line.replace(", '%Y-%m-%d %H:%i:%s')", ""))
#close input and output files
fin.close()
fout.close()
f2in.close()
f2out.close()



