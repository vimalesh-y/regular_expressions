## Import regular expression module
import re

# 4 lowercase letters
# 4-6 digits
# One symbol
# Up to two upper-case characters

## Defining pattern
# ^ indicates that whatever the pattern is, it should start at the beginning of the string
# [A-Z] indicates only upper-case characters are required
# [a-zA-Z] denotes either upper-case or lower-case characters
# \s allows for spaces
# + denotes that upper-case characters have to occur at least once but can be as many times as possible
# $ denotes end of the string
#### pattern = re.compile("^[A-Z\s]+$")
#### pattern = re.compile("^[a-z]{4}[0-9]{4,6}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
#### pattern = re.compile("^.{10}$")
pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")

# pattern.search checks for matches only at beginning of the string
print(pattern.search("vim_yo@gmail.com"))
print(pattern.search("mail@test.com"))
print(pattern.search("something.nothing.com"))

# pattern.match checks for matches throughout whole string
print(pattern.match("asdf13579&S"))
print(pattern.match("ASDF346£465msdf"))
print(pattern.match("bmsd45643$s"))




