'''
First way is:
Using "num2words" module.
from num2words import num2words
def convert(x):
    return num2wors(x).replace('-', ' ')
'''

'''
Second way is:
Using "inflect" module.
Inflect is very useful module
import inflect
p = inflect.engine()

def convert(x):
    return p.number_to_words(x).replace('-',' ')
'''
global n2W
n2w = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',\
       6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
       15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',\
       19: 'nineteen',20:'twenty'}

def convert(x):
    try:
        return n2w[x]
    except:
        return n2w[20] + ' ' + n2w[x-20]

# inputs in hh and mm
h, m = int(input().strip()), int(input().strip())

if m == 0:
    print(convert(h), "o' clock")
elif m == 15 or m == 30:
    print("quarter past" if m == 15 else "half past", convert(h))
elif m < 30:
    print(convert(m), "minutes past", convert(h))
elif m == 45:
    print("quarter to", convert(h+1))
elif m > 30:
    print(convert(60-m), "minutes to", convert(h+1))

'''
Sample Input
    5  
    47  

Sample Output
    thirteen minutes to six
'''
