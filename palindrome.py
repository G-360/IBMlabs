str='malayalam'
str=str.casefold()
rev=reversed(str)

if  list(str)==list(rev):
    print('the string is a palindrome')
else:
    print('the  string is not a palindrome')