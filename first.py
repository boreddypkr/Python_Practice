# This file describes all the attributes of a variable 
text="python program"
print(text)

a = input("Please Enter a String: ")
print(f"The total no of operations that can be performed on the string : ", len(dir(a)))

num_text = "12345"
space_text = "   "
mixed_text = "Python123"
case_text = "CaseFold"
tabs_text = "Python\tProgram"

# 1. Capitalize() - Capitalizes the first leter of a string.

print("capitalize:", text.capitalize())

# 2. casefold() - Converts string to lowercase, more aggressive than lower(),it converts other language and special symbols as well.
print("casefold:", case_text.casefold())

# 3. center() - Centers the string within a specified width, filling with given character.
print("center:", text.center(20, "-"))

# 4. count() - Counts occurrences of a substring.
print("count:", text.count("o"))

# 5. encode() - Encodes the string in UTF-8 format.
print("encode:", text.encode())

# 6. endswith() - Checks if the string ends with a specified suffix.
print("endswith:", text.endswith("program"))

# 7. expandtabs() - Replaces tab characters with spaces (default: 8 spaces).
print("expandtabs:", tabs_text.expandtabs(10))

# 8. find() - Finds the first occurrence of a substring, returns -1 if not found.
print("find:", text.find("o"))

# 9. format() - Formats strings using placeholders.
print("format:", "My name is {}".format("Sumanth"))

# 10. format_map() - Similar to format(), but works with dictionaries.
person = {'name': 'Sumanth', 'age': 30}
print("format_map:", "My name is {name} and I am {age} years old.".format_map(person))

# 11. index() - Finds first occurrence of a substring, raises an error if not found.
print("index:", text.index("o"))

# 12. isalnum() - Returns True if all characters are alphanumeric.
print("isalnum:", mixed_text.isalnum())

# 13. isalpha() - Returns True if all characters are alphabetic.
print("isalpha:", text.isalpha())

# 14. isascii() - Returns True if all characters are ASCII.
print("isascii:", text.isascii())

# 15. isdecimal() - Returns True if all characters are decimals (only digits 0-9).
print("isdecimal:", num_text.isdecimal())

# 16. isdigit() - Returns True if all characters are digits.
print("isdigit:", num_text.isdigit())
print("isdigit:", text.isdigit())

# 17. isidentifier() - Checks if the string is a valid Python identifier.
print("isidentifier:", "Python Program".isidentifier())

# 18. islower() - Returns True if all characters are lowercase.
print("islower:", text.islower())

# 19. isnumeric() - Returns True if all characters are numeric (including fractions, superscripts).
print("isnumeric:", num_text.isnumeric())

# 20. isprintable() - Returns True if all characters are printable.
print("isprintable:", text.isprintable())

# 21. isspace() - Returns True if the string contains only whitespace.
print("isspace:", space_text.isspace())

# 22. istitle() - Returns True if the string follows title case (first letter capitalized).
print("istitle:", "Python Program".istitle())

# 23. isupper() - Returns True if all characters are uppercase.
print("isupper:", "Python".isupper())

# 24. join() - Joins elements of an iterable with a separator.
print("join:", "-".join(["Python", "Programs"]))

# 25. ljust() - Left-aligns the string, filling remaining space with given character.
print("ljust:", text.ljust(20, "-"))

# 26. lower() - Converts the string to lowercase.
print("lower:", "HELLO".lower())

# 27. lstrip() - Removes leading whitespace.
print("lstrip:", "  hello".lstrip())

# 28. maketrans() and translate() - Used for character replacement.
trans_table = str.maketrans("h", "H")  # Replaces 'h' with 'H'
print("translate:", text.translate(trans_table))

# 29. partition() - Splits the string into three parts: before, separator, after.
print("partition:", text.partition(","))

# 30. removeprefix() - Removes a specified prefix from the string.
print("removeprefix:", "unhappy".removeprefix("un"))

# 31. removesuffix() - Removes a specified suffix from the string.
print("removesuffix:", "filename.txt".removesuffix(".txt"))

# 32. replace() - Replaces occurrences of a substring with another string.
print("replace:", text.replace("program", "course"))

# 33. rfind() - Finds the last occurrence of a substring, returns -1 if not found.
print("rfind:", text.rfind("o"))

# 34. rindex() - Finds the last occurrence of a substring, raises an error if not found.
print("rindex:", text.rindex("o"))

# 35. rjust() - Right-aligns the string, filling remaining space with given character.
print("rjust:", text.rjust(20, "-"))

# 36. rpartition() - Like partition(), but searches from the right.
print("rpartition:", text.rpartition(","))

# 37. rsplit() - Splits the string from the right into a list.
print("rsplit:", "one,two,three".rsplit(","))

# 38. rstrip() - Removes trailing whitespace.
print("rstrip:", "hello   ".rstrip())

# 39. split() - Splits the string into a list based on a separator.
print("split:", "one,two,three".split(","))

# 40. splitlines() - Splits the string into a list at line breaks.
print("splitlines:", "Python\nProgram".splitlines())

# 41. startswith() - Checks if the string starts with a specified prefix.
print("startswith:", text.startswith("hello"))

# 42. strip() - Removes leading and trailing whitespace.
print("strip:", "  hello  ".strip())

# 43. swapcase() - Swaps uppercase to lowercase and vice versa.
print("swapcase:", "PYTHON program".swapcase())

# 44. title() - Converts the string to title case.
print("title:", "python program".title())

# 45. upper() - Converts the string to uppercase.
print("upper:", "hello".upper())

# 46. zfill() - Pads the string with zeros to match a specified width.
print("zfill:", num_text.zfill(10))

