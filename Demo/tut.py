# from faker import Faker
# fake = Faker()

# for number in range(1,21):
#     if 8 <= number <= 12:
#         continue
#     print(number,end = ',')
#
# for numbers in range(1,10):
#     if numbers == 7:
#         break
#     print(numbers,end=',')
#
#
# my_string = 'abcabc'
# for c in my_string:
#     if c == 'a':
#         print('A', end=" ")
#     else:
#         print(c, end=" ")
#
# cars = ["merc","bmw", "audi", "nissan"]
# for car in cars:
#     print(car,end=",")

# sample_dict = {"one": 1, "two": 2, "three": 3}
# for k in sample_dict:
#     print(k + " " + str(sample_dict[k]))
# print("*" * 10)
# for k,v in sample_dict.items():
#     print(k + ":" + str(v))

# l1 = [2,7,1,2,0,2]
# l2 = [4,5,6,2]
# for a,b in zip(l1,l2):
#     print(a, b)
# for i in range(0,20,5):
#     print(i)

#ChatGPT Assignment
# a = int(input("Enter a number:"))
# if a%2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

# for i in range(31):
#     if i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# for i in range(21):
#         if i % 4 == 0:
#             continue
#         print(i)


# for i in range(1,50):
#     if 30<= i <40:
#         continue
#     if i == 45:
#         break
#     print(i)

# for i in range(1,15):
#     if i % 2 == 0:
#         print(f"Even number: {i}")
#     elif i % 2 != 0 and i < 10:
#        continue
#     else:
#         print(f"Odd number: {i}")
#

# def sum1(n1, n2=4):
#     return n1 + n2
#
# sum = sum1(10)
# print(sum)


# def metro(city):
#     a = ['mum', 'kol', 'del']
#     if city in a:
#         return True
#     else:
#         return False
#
# x = metro('mum')
# print(x)

# def eve_or_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# eve_or_odd(5)

# a = 10
# def num():
#   global a
#   a = 2
#   print(a)
#
# num()
#
#
# def max_num(*args):
#   print(max(args))
#
# max()
# def max_num2(*args):
#   print(max(args))
#   return(max(args))
#
# max_num2(3,5,1)

def calculateNetTax(gross,state):
    state_tax = {'Mum': 10, 'Del': 9, 'Pun': 0}
    net = gross - (gross * 10)
    if state in state_tax:
        net = net - (gross * state_tax[state]/100)
        print("Your net amount is: " + str(net))
        return net
    else:
        print("State not in list")
        return None

calculateNetTax(600000,'Mum')


