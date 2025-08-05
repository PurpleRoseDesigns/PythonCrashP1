def display_message():
    print("We are learning about functions")

display_message()

def favourite_book(title):
    print(f"One of my favourite books is {title}")

favourite_book('Rebecca')

"""Positional Argument in Functions"""

def my_pet(animal_type, name):
    print(f"My {animal_type} is called {name}")

my_pet('rabbit', 'Fred')

"""Keyword Argument in Functions"""

def my_pet_key(animal, age):
    print(f"My {animal} is called {age}")

my_pet_key(animal='rabbit', age='Fred')

"""Default Values"""

def my_favourite_book(date, b_title="Rebecca"):
    print(f"One of my favourite books is {b_title} and it was published in {date}")

my_favourite_book(date="1989", b_title="Hamilton")