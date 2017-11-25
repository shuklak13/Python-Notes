# Metacharacters:
#   []  create character classes
#   [^] create negations of character classes
#   ?   0 or 1
#   *   0 or more
#   +   1 or more
#   {m,n}   at least m, at most n   (m=0, n=inf if omitted)
#   .   any character
#   \   escape character
#   |   or
#   ^$  start, end of line

# Common Regexes
#   [a-zA-Z0-9]     all alphanumerics
#   [^a-zA-Z0-9_]   all non-alphanumerics

import re
pattern = re.compile('[a-z]+') # a, followed by any number of b's

def match(s):
    """ Check if pattern matches beginning of string.
        Return match object, or None.       """
    pattern.match(s)

def search(s):
    """ Check if pattern matches any substring,
            sstarting at the beginning of the string.
        Return match object, or None.       """
    pattern.search(s)

def findall(s):
    """ Returns list of all substrings matching pattern. """
    pattern.findall(s)

match("1hi2bye")    # None
search("1hi2bye")   # <_sre.SRE_Match object; span=(1, 3), match='hi'>
findall("1hi2bye")  # ['hi', 'bye']