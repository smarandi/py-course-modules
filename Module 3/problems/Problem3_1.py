def problem3_1(filename):
    text_file=open(filename);
    no_of_characters = 0
    for line in text_file:
        no_of_characters = no_of_characters + len(line)
        print(line, end="")
    print("\n\nThere are {} letters in the file.".format(no_of_characters))

