import textwrap
string = "This is a very very very very very long string."
print textwrap.wrap(string,8)
"""['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']"""

string = "This is a very very very very very long string."
print textwrap.fill(string,8)
"""This is
a very
very
very
very
very
long
string."""

print textwrap.fill(raw_input(),int(raw_input()))