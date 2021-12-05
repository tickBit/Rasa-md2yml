'''
    Converts the most common md files of Rasa to yml files,
    nlu.md and stories.md, but you'll probably need to make some
    changes to domain.yml, too. Also, there can be more outdated syntaxes in the files...

    Usage: python Rasa-md2yml.py <md_file> <yml_file>
    
    version 0.5
'''

import sys

# check that there is 2 arguments from the command line
if len(sys.argv) < 3:
    print("Usage: python rasa-md2yml.py 'input file' 'output file'")
    exit(1)


# open the input file

try:
    # open the input file
    inputfile = open(sys.argv[1], "r").readlines()
except:
    print("Error: Input file not found.")
    exit(1)



output = 'version: "3.0"\n\n'

# read input and output files from the command line
print(sys.argv[1])

if "nlu" in sys.argv[1]:
    print("Converting nlu.md to yml...")

    # Convert's Rasa's nlu.md to nlu.yml
    output += "nlu:\n"

    # Read the file line by line until end of file:
    for line in inputfile:
        line = line.rstrip()
        # If the line is not empty:
        if line != "":
           
            if line.startswith("##"):
                keywords = line.split(":")
                output += "  - " + keywords[0][2:].strip() + ": " + keywords[1].strip() + "\n"     
                
                if (len(keywords) > 1):
                    output += "    examples: |\n"
             
                
            else:
                output += "      "+line+"\n"

if "stories" in sys.argv[1]:
    print("Converting stories.md to yml...")
    
    # Convert's Rasa's stories.md to stories.yml
    output += "stories:\n"
    # Read the file line by line until end of file:

    for line in inputfile:
        line = line.rstrip()
        # If the line is not empty:
        if line != "":

            if line.startswith("##"):
                output += "- story:" + line[2:] + "\n"
                output += "  steps:\n"
            elif line.strip().startswith("*"):
                output += "    - intent:" + line[1:] + "\n"
            elif line.strip().startswith("-"):
                output += "    - action:" + line.strip()[1:] + "\n"

# Write the output to a file
try:
    with open(sys.argv[2], "w") as outputfile:
        outputfile.write(output)
except:
    print("Error in writing the output file.")
