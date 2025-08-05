def get_price(price=None):
    the_price = f"{price}"
    return the_price

print_price = get_price(2.80)
print(print_price)


# def favourite_musical(name, genre):
#     musical_dict = {
#         'name': name,
#         'genre': genre
#     }
#     return musical_dict

# #promts

# prompt_one = "What is your fav musical? "
# prompt_two = "What genre is it? "

# print("To quit at anytime press q")

# while True:
#     name = input(prompt_one)
#     if name == "q":
#         break

#     genre = input(prompt_two)
#     if genre == "q":
#         break

#     musical_list = favourite_musical(name, genre)
#     print(musical_list)
