# this is a simple tutorial about how to process the string

name = "ada lovelace"
print(name.title()) # title() is a function to change the first letter of each word to upper case

name = "Ada Lovelace"
print(name.upper()) # upper() is a function to change every letter to upper case
print(name.lower()) # lower() is a function to change every letter to lower case

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("python")
print("\tpython") # \t add a tab
print("Languages:\nPython\nC\nJavaScript") # \n line feed
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip()) # rstrip() is a function to remove the blank at the end of the string
print(favorite_language.lstrip()) # lstrip() is a function to remove the blank at the beginning of the string
print(favorite_language.strip()) # strip() is a function to remove the blank of thr string both at the end and beginning

