name = "Khan Israk Ahmed"

print(name.upper())  # Converts all characters to uppercase

print(name.lower())  # Converts all characters to lowercase

print(name.capitalize())  # Capitalizes only the first letter

print(name)
print()

name = name.lower()
print(name)
print()

name = name.upper()
print(name)
print()

print(name.find('N'))  # Looks for 'N' in the uppercase string

print()

print(name.find('A'))  # Finds the first occurrence of 'A'

name = name.replace("ISRAK", "MOWDUD")  # Replaces "ISRAK" if found

# Print name again to confirm replacement
print(name)


print('ISRAK' in name)
print('KHAN' in name)

name = "Israk"
print(name*5) # Israk 5 time's
print()

address = '''Dhaka Bangladesh UIU'''

print(address)