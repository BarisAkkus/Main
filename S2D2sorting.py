pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3,4.5,8.7,3.1,9.2,1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
#another_sorted_numbers = numbers.sort()
print(numbers)
#print(another_sorted_numbers) çalışmaz
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)