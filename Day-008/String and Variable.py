

#Concatenation
Name = "Samia"
print(Name + " is cool.")

# Escape Characters in Python

print ("Samia is cool.") #Normal print statement
print("Name: Samia\nRoll Number: 24") # Newline: after \n the text moves to the next line
print("Samia\"Samia") # \" Double Quote: adds double quotation inside the text
print("Samia Jahan Ananna \\ is cool") # Backlash: add a single backlash into the text
print("Samia Jahan \r Ananna") # Carriage Return: Moves the curser to the beginning of the current line, allowing the next text to overwrite
print("Samia Jahan \t Ananna") # Horizontal Tab: Moves the cursor to the next tab stop creating horizontal spacing between the text

#Common Function in Python:

phrase="Samia is cool. She is one of the best student in the class and always attentive."
print(phrase.lower())
print(phrase.upper())


#Checking if the text is in upper or lower case:
Text= "SAMIA IS COOL. SHE IS ONE OF THE BEST STUDENT IN THE CLASS AND ALWAYS ATTENTIVE."
print(Text.isupper())
print(Text.islower())

# Using the upper or lower functions also checking the case simultaneously:
Txt = "Samia is a cool girl. She has been working on her coding so long. Now she is more focused on building things which will save the community from any kind of disaster."
print(Txt.upper().isupper())
print(Txt.lower().islower())

# Checking how many characters inside the variable:
txt = "I am Samia Jahan"
print(len(txt))

# Checking the character in the text:
text = "I am Samia Jahan Ananna"
print(text[2])

#Index Function
TXT = "I am Samia Jahan Ananna"
print(TXT.index("A"))

#Replace function:
Phrase = "Giraffe is one of the largest animal"
print(Phrase.replace("Giraffe", "Elephant"))



