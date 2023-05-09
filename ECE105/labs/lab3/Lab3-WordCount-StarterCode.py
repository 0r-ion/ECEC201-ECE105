from collections import Counter

"""
Daniel Goulding
14511512

ASSIGNMENT: COMPLETE per specifications below
"""

"""
ECE 105: Programming for Engineers 2
Created September 5, 2020
Steven Weber

Modified April 17, 2023
Naga Kandasamy

Zipf's Law: code to create word count for text file

This code reads in a text file and writes a file listing counts of each word
"""

"""
Use the Python collections library, specifically the Counter class
https://docs.python.org/2/library/collections.html#collections.Counter

A Counter is a dict subclass for counting hashable objects.
It is an unordered collection where elements are stored as dictionary keys and
their counts are stored as dictionary values.
Counts are allowed to be any integer value including zero or negative counts.
The Counter class is similar to bags or multisets in other languages.
"""

# file holding the text to be read
input_filename = 'KingJamesBible-Modified.txt'
# filename to hold word frequency counts
output_filename = 'KingJamesBible-WordCounts.txt'

# open and read in filename as a single string
with open(input_filename, 'r') as f:
    file_as_string = f.read().replace('\n', ' ')

"""
COMPLETE:

The (very long) string file_as_string holds the source text

1. Use Python string split() command to split the string into a list of words
2. Read about the Counter class, described above.
Use Counter on the list of words to create a Counter instance named counts.
Use Counter's most_common() method to sort words in decreasing order

Having created the Counter dictionary named counts, the last block of code
will open a filepointer f ready to write ('w') to output_filename.  It will
iterate over the (key, value) pairs (c[0], c[1]) for each element c in counts
and print each pair to the file.
"""
splitted = file_as_string.split()
print(f"SPLITTED:{len(splitted)}")
counter_thing = Counter()
for word in splitted:
    counter_thing[word] += 1

counts = counter_thing.most_common(len(splitted))

# write the words and counts to the output file
with open(output_filename, 'w') as f:
    for c in counts:
        f.write('{} {}\n'.format(c[0],c[1]))
