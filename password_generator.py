import random
import string

letters = (''.join(random.choices(string.ascii_letters, k = 7)))
numbers = (''.join(random.choices(string.digits, k = 5)))
punctuation = (''.join(random.choices(string.punctuation, k = 3)))

#print(letters) 
#print(numbers) 
#print(punctuation)

generate = str(letters + numbers + punctuation)
password = (''.join(random.sample(generate, len(generate))))

print(password)
