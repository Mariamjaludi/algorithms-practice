# Log File
# You have been given a task of recording some data 40M a log file. In the log
# file, every line is a space-delimited list of strings. All lines begin with an
# alphanumeric identifier. There will be no lines consisting only of an
# identifier. After the alphanumeric identifier a line will consist of either:
# - a list of words using only lowercase English letters
# - or list of only integers.

# You have to reorder the data such that all of the lines with words are at the
# top of the log file. The lines with words are ordered lexicographically.
# ignoring the identifier except in the case of ties In the case of ties (if
# there are two lines that are identical except for the identifier) the
# identifier is used to order lexicographically. Alphanumeric should be sorted
# in ASCII order (numbers come before letters) The identifiers most still be pan
# of the lines in the output Strings. Lines with integers must be left in the
# original order they were in the file.
# Write an algorithm to reorder the data in the log file, according to the rules
# above.

# Input
# The input to the function/method consists of two argument - logFileSize, an
# integer representing the number of log lines.
# logLines, a list of strings representing the log file.
