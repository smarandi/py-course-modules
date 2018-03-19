
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

def problem3_6(input_file, output_file):
    infile = open(input_file)
    outfile = open(output_file, "w")
    for line in infile:
        count =  len(line.strip("\n"))
        outfile.write(str(count) + "\n")

    infile.close()
    outfile.close()

problem3_6(filename1, filename2)
