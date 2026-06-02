# Collect user input
name     = input('Enter your name: ')
age      = int(input('Enter your age: '))
language = input('Favourite programming language: ')

# Calculations
birth_year = 2025 - age

# Data structures
skills = ['Linux', 'Networking', 'Python']

profile = {
    'name':       name,
    'age':        age,
    'birth_year': birth_year,
    'language':   language,
    'skills':     skills
}

# Output — formatted profile card
print()
print('=' * 40)
print('       STUDENT PROFILE CARD')
print('=' * 40)
print(f"  Name:       {profile['name']}")
print(f"  Age:        {profile['age']}")
print(f"  Born:       {profile['birth_year']}")
print(f"  Favourite:  {profile['language']}")
print(f"  Skills:     {', '.join(profile['skills'])}")
print('=' * 40)





































































# Created by d4ktari on 2026-06-02