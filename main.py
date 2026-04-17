import random
import string
while True:
    try:
        length = int(input("enter the length of the string: "))
        if length <= 0 :
            print("the length of the string must be greater than 0")
            continue
        if length > 94:
            print("the length of the string must be less than 94")
            continue
        break
    except ValueError:
        print("invalid input")
        break
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

all_func = lower + upper + digits + punctuation
temp = random.sample(all_func, length)
password = "".join(temp)
print(f"PASSWORD: {password}")
