# Fix csv
# takes a file with an incorrect delimiter and corrects it with a comma ,
import os
import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('original_file')
parser.add_argument('new_file')
parser.add_argument('--in-delimiter', default="|")
parser.add_argument('--in-quote', default='"')

args = parser.parse_args()

with open(args.original_file) as o:
    dialect = csv.Sniffer().sniff(o.read())

if args.in_delimiter:
    delimiter = args.in_delimiter
else:
    delimiter = dialect.delimiter

if args.in_quote:
    quotechar = dialect.quotechar
else:
    quotechar = dialect.quotechar

with open(args.original_file) as o:
    rows = list(csv.reader(o, delimiter = delimiter, quotechar = quote_char))

with open(args.new_file, 'w', newline='') as n:
    writer = csv.writer(n)
    writer.writerows(rows)