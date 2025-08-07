# text = "Lion king"
#Alignment on the center
#print(f'[{text:^15}]')
#print(len(f'[{text:^15}]'))
# text_aligned = (f'[{text:^15}]')
#
# print(text_aligned)
# print(len(text_aligned))

#Using string format() method
# num1 = 567
# num2 = 39.980
# print('{:d}  {:.2f}'.format(num1,num2))

#using + and * to repeat strings. using join.
# fruit = 'apple'
# fruit = '*'
# print(fruit*10)

# fruit = 'apple for food'
# fruit = ['apple', 'for', 'food']
# print('-'.join(fruit))

#Stripping whitespaces from strings using strip(), 1Strip(), rStrip().
# place = ' jungle race on '
# place = ' \t\tjungle\t\t'
# print(place)
# print(place.strip())

#CHANGING CHARACTER CASE AND COMPARISON
# name = 'chief okafor'
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.title())

#Ascii table is used to compare
# print('cat' > 'dog')

# word = 'polymorphism'
#
# print(word.find('morph'))
# print(word.index('morph'))
# print(word.find('m'))
# print(word.index('m'))

#using replace string


#Splitting and joining strings
# word = "Time bound"
# print(word.split())

#Raw String
# raw_str = r"C:\Users\Name"
# print(raw_str)

#REGULAR EXPRESSION
import re
#MATCH
# pattern = '02935'
#
# print(True if re.fullmatch(pattern, '0293') else False)

#PATTERN,REPLACEMENT AND TEXT
#pattern = 'yahoo.com'
#text = 'oba@yahoo.com'
#replacement = 'gmail.com'
#result = re.sub(pattern, replacement, text)
#print(result)

#patterns and String using split
# text = "letter story comprehension"
# pattern = ' '
# print(re.split(pattern, text))

# money = '80,000,000'
# pattern = ','
# print(re.split(pattern,money))

# money = '80,000,000.00.00'
# pattern = ','
# pattern_two = '.'
# first_match = re.split(pattern,money)


# result_in_str = ''.join(first_match)
# print(result_in_str)


