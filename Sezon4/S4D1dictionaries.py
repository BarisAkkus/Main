fruit = {"orange":"a sweet, orange , citrus fruit",
         "apple" : "good for making cider",
         "lemon":"a sour, yellow citrus fruit",
         "grappe":"a small,sweet fruit growing in bunches",
         "lime":"a sour, green citrus fruit"}

print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shape apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# #del fruit["lemon"]
# #fruit.clear()
# #print(fruit)
# print(fruit["tomato"])
# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we dont have a "+ dict_key)
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
# for snack in fruit
# for f in fruit:
#     print(f + " - " + fruit[f])
# for val in fruit.values():
#     print(val)

# print('-'*40)

# for key in fruit:
#     print(fruit[key])
fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)