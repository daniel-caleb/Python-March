# strings
name = "Daniel"
city = 'New York'
bio = """Daniel is a Cybersecurity Analyst who loves coding and traveling."""

print(name)
print(city)
print(bio)

# String concatenation
print("Hello, " + name + "! Welcome to " + city + ".")

# String formatting
print(f"{name} is a Cybersecurity Analyst who loves coding and traveling.")

# String methods
print(name.upper())  # Convert to uppercase
print(city.lower())  # Convert to lowercase
print(bio.split())  # Split into a list of words
print(bio.replace("loves", "enjoys"))  # Replace a word

# String indexing and slicing
print(name[0])  # First character
print(name[-1])  # Last character
print(name[1:4])  # Substring from index 1 to 3
