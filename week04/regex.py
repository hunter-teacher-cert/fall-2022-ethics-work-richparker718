import re

pattern = re.compile(r'Dr\.?\s[A-Z][a-z]*\s[A-Z]\.?[a-z]*\s|[A-Z][a-z]+\s[A-Z][a-z]+\w')


with open ('names.txt', 'r') as text:
  file = text.read()

  matches = pattern.finditer(file)
  
  for match in matches:
    print(match)


