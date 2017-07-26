#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

##
## opens a file, splits it into words and makes a dictionary 
## where words are key and valuses are the number of occurencies of that word
##

def make_a_hash(filename):

  f= open(filename, 'rU')
  text = f.read() ## reads the entire file in one string
  words = text.lower().split() ## converts to lowercase and splits on white space into a list
  
  hash = {}
  for word in words:
    if word in hash:
      hash[word] = hash[word] + 1
    else:
      hash[word] = 1
      
  f.close()
  return hash

##
## function that counts how often each word appears in the text and prints:
## word1 count1
## word2 count2
## sorted by word
##

def print_words(filename):

  hash = make_a_hash(filename)## calls helper function
  
  for k in sorted(hash.keys()):
    print k, hash[k]
  
## 
##prints just the top 20 most common words sorted so the most common word is first
##

def last_elem_t(tuple):
  return tuple[1]

def print_top(filename):

  hash = make_a_hash(filename)## calls helper function
  list_of_tuples = []
  list_of_tuples = sorted(hash.items(), key = last_elem_t, reverse = True)
  
  if len(list_of_tuples) > 20:
    for i in range (20):
      mini_list = list_of_tuples[i]
      print mini_list[0], mini_list[1]
  else:
    for tup in list_of_tuples:
      mini_list = tup
      print mini_list[0], mini_list[1]



  


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
