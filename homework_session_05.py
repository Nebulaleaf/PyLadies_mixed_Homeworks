#Using this string - str1 = "It's always darkest before dawn." create a new string by putting together the first, fifth, last and one before the last character.
#I wanted to do it smart but I dont get those charakters together as string now, so not so smart -.-

str1 = "It's always darkest before dawn."
str2 = [str1[i] for i in [0, 4, -1, -2]]
print(str2)

#final, maybe there is a more smart way to do it but I didn't find it
str1 = "It's always darkest before dawn."
first = str1[0]
fifth = str1[4]
last = str1[-1]
second_last = str1[-2]

str2 = first + fifth + last + second_last

print(str2)

#Try to read on the internet what the string replace method does and what arguments are needed. Then try to replace all occurrences of “a” with “?” character in the original string from exercise 1
#the replace method is a method for replacing a specified phrase with another. the arguments needed are: string.replace(old, new, count), though count is optional

str1 = "It's always darkest before dawn."
str2 = str1.replace("a", "?")
print(str2)

#Write a function to return a reversed version of a given word (or longer sentence). There is a nice Python trick :)
def str_reverse(str1):
  return str1[::-1]

string = input("What shall be reversed?\n")
reversed_string = str_reverse(string)
print(reversed_string)

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
def str_reverse(str1):
  return str1[::-1]

string = input("What shall be reversed?\n")
reversed_string = str_reverse(string)
if string.lower() == reversed_string.lower():
  print("Your input: ", string, "is a palindrome.")
else:
  print("Your input: ", string, "is not a palindrome. Backwards it looks like this: ", reversed_string)

#Write a function which takes as argument any string and returns length of that given string
def length(str1):
  return len(str1)

string = input("Say something:\n")
len_string = length(string)
print(len_string)

#Write a function where you give a word and number and it will return a substring from the start of the string up to the number given.#
#Try to format answers nicely using formatting options from the lesson. Consider that the number can be larger than the length of the string.

def function(word, num):
  sub_str = word[:num]
 #formatting with {}×{} equals {}
  return "'{}' up to index {} is '{}'".format(word, num, sub_str)

word = "Hello"
num = 3
print(function(word, num))



#Write a while loop that adds all the numbers up to 100 (inclusive) and print the sum.
sum = 0
num = 1
while num <= 100:
  sum += num
  num += 1
print(sum)

#Change the Rock, Scissors, Paper to repeat the game until the user enters the "end".
from random import randrange

while True:

  pc_choice = randrange(3)
  if pc_choice == 0:
    pc_choice = 'rock'
  elif pc_choice == 1:
    pc_choice = 'scissors'
  else:
    pc_choice = 'paper'
  user_choice = input('rock, paper, or scissors or end to stop the game?\n')

  if user_choice == 'end':
    break

  print("pc chose :", pc_choice)

  if user_choice == 'rock':
      if pc_choice == 'rock':
          print('Draw.')
      elif pc_choice == 'scissors':
          print ('You win!')
      elif pc_choice == 'paper':
          print ('Computer won!')
  elif user_choice == 'scissors':
      if pc_choice == 'rock':
          print('Computer won!')
      elif pc_choice == 'scissors':
          print('Draw.')
      elif pc_choice == 'paper':
          print('You win!')
  elif user_choice == 'paper':
      if pc_choice == 'rock':
          print('You win!')
      elif pc_choice == 'scissors':
          print('Computer won!')
      elif pc_choice == 'paper':
          print('Draw.')
  else:
      print('I do not understand.')
print("Gamestop")

#this took me ages, had many other trys with while loops outside the user_choice but got serveral infernal loop-outputs ^^, but this works, I hope it's a good way or sloppy? I dont know!

