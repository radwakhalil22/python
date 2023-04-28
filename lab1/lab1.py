# 1-​ Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)


# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.

def value_of_nnn():
    n = int(input("Enter a number: "))
    nn = n * 11  # n*11 is equivalent to n+nn
    nnn = n * 111  # n*111 is equivalent to n+nn+nnn
    result = n + nn + nnn
    print(f"n + nn + nnn = {result}")

value_of_nnn()

# 3- Write a Python program to print the following here document.
# Sample string ​ : a string that you "don't" have to escape
    # This
    # is a ....... multi-line
    # heredoc string --------> example

def print_document():
    print('''a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example''')

print_document()


# 4- Write a Python program to get the volume of a sphere with radius 6.
import math

def volume_of_sphere(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radius = 6
volume = volume_of_sphere(radius)

print("The volume of the sphere with radius", radius, "is", volume)


# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

def print_pattern(n):
    for i in range(n):
        for j in range(i):
            print('* ', end="")
        print('')
    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end="")
        print('')

n = 5
print_pattern(n)



# 7- Write a Python program that accepts a word from the user and reverse it.

def reverse_word():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print("The reversed word is:", reversed_word)

reverse_word()

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.


def print_numbers():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        print(i, end=" ")

print_numbers()


# 9-Write a Python program to get the Fibonacci series between 0 to 50

def Fibonacci(n=50):
    prev=0
    next=1
    print(prev)
    while next<50:
        print(next)
        temp=next
        next=prev+next
        prev=temp

Fibonacci()


# 10- Write a Python program that accepts a string and calculate the number of digits and
# letters.

def count_letters_digits(s):
    letters = 0
    digits = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    print("Letters:", letters)
    print("Digits:", digits)

count_letters_digits("Hello World! 123")
