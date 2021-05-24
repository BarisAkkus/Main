panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,755,807"
print(numbers.split(","))

#values = "".join(char if char not in seperators else " " for char in numbers).split()
generated_list= ['9', ' ',
                 '2','2','3',' ',
                 '3','7','2',' ',
                 '0','3','6',' ',
                 '8','5','4',' ',]
values = "".join(generated_list)
print(values)
values_list = values.split()
print(values_list)

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)

integer_values =[]
for value in values_list:
    integer_values.append(int(value))
print(integer_values)