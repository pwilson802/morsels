# Fix csv
# takes a file with an incorrect delimiter and corrects it with a comma ,
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('original_file')
parser.add_argument('new_file')
args = parser.parse_args()
original_file = args.original_file
new_file = args.new_file


write_file = open(new_file, 'w')

with open(original_file) as o:
    for line in o.readlines():
        write_file.write(line.replace("|", ","))

write_file.close()
