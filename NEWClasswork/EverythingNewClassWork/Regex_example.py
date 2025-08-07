import re



# text = "The Silent Boy, is sick today , call this number 09012345678"
# text = "The silent 12 Boy, is sick23 today , call this number**0903 king73738"

# pattern = re.compile(r'\b[0-9]+')
# pattern = re.compile(r'[^0-9]+')
# pattern = re.compile(r'[0-9]+')
# pattern = re.compile(r'[0-9]')

# pattern = re.compile("'[a-zA-Z]'+")
# pattern = re.compile('[a-zA-Z]+')
# pattern = re.compile(r"^[a-zA-Z0-9]+") #print only the first word

# match = pattern.findall(text)
# print(match)

# pattern = re.findall(r'\b\d+\b',text)
# pattern = re.findall('[a-zA-Z]+', text)
# print(pattern)



# text = """"The  boys link is https://localhost/pythoncode and the git address is http://king123/git"""

# pattern = re.compile(r'([a-z]+)(://)([a-z]+/[a-zA-Z]+)')
# pattern = re.compile(r'([a-z]+)(://)(([a-z0-9]+)/([a-zA-Z0-9]+))',re.IGNORECASE)
# pattern = re.compile(r'([a-z]+)(://)([a-zA-Z0-9/]+)',re.IGNORECASE)



# matches = pattern.finditer(text)

# for match in matches:
#     print(match.group(1), match.group(2), match.group(3)) #print at each group
    # print(match)

text = "my account number  is 009-324-5354"

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
print(re.findall(pattern, text))







