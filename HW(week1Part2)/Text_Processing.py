import re 

new_string = "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"

#1. Extract the numbers
#\d means 0-9
numbers = re.findall(r"\d+", new_string)
print("1. Extract the numbers: ", numbers)
print()

#2. Exract the names
#use regex. findall is returns a list containing all mathes
regex = re.findall(r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.? \s*)?[A-Z][a-z]+", new_string)
print("2. Extract the names: " ,regex)
print()

#3. Rearrange the vector so that all elements conform to the standard “firstname lastname”, 
# preserving any titles (e.g., “Rev.”, “Dr.”, etc) or middle/second names.
regex_withTitles = re.findall(r"(?:(?<=^)|(?<=[^A-Za-z.,]))[A-Za-z.,]+(?: [A-Za-z.,]+)*(?:(?=[^A-Za-z.,])|(?=$))", new_string)
print("3. Name: ", regex_withTitles)
print()

#4. Construct a logical vector indicating whether a character has a title (i.e., Rev. and Dr.)
title = re.findall(r"([A-Z][a-z]*\.)", new_string)
print("4. Title: ", title)
print()

#5. Construct a logical vector indicating whether a character has a middle/second name.  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!
middle_name =re.findall(r"\s[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.? \s*)", new_string)
print("5. Middle or second name: ",middle_name)
print()

#6. Consider the HTML string <title>+++BREAKING NEWS+++<title>. We would like to extract the first HTML tag (i.e., “<title>”). 
#To do so we write the regular expression “<.+>”. Explain why this fails and correct the expression.
html_tag = "<title>+++BREAKING NEWS+++<title>";
tag = re.findall(r"<[a-z]+>", html_tag )
print("6. answer is: ", tag)
print()

#7. Consider the string “(5-3)^2=5^2-2*5*3+3^2”. 
#We would like to extract the equation in its entirety from the string. 
#To do so we write the regular expression “[^0-9=+*()]+”. Explain why this fails and correct the expression.
equation ="(5-3)^2=5^2-2*5*3+3^2"
#\d : matches digits 0-9.
#+ : matches the expression to its left 1 or more times.
equation_string = re.findall("\(\d\-\d\)\^\d.*", equation)
print("7. answer is: ", equation_string)