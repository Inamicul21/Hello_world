# FeBe 30.09.2016

#importare librarii
import sys
from random import randint
import os

# definire functii
def add(x, y):
   
   return x + y

def subtract(x, y):
   
   return x - y

def multiply(x, y):
   pass

   return x * y

def divide(x, y):

   return x / y

def my_friend():
   print ("Hello my friend\n")

def input_fNum():
     val =  int(input("Introdu primul numar: "))
     return val

def input_sNum():
      val = int(input("Introdu al doilea numar: "))
      return val
      
      # random number on demand
def talent():
   print("Numarul tau random este:",randint(0,9))

# take input from the user
print("Select operation.")
print("1.Aduna")
print("2.Scadere")
print("3.Multiplicare")
print("4.Impartire")
print("5.Hello friend!")
print("6.Talentul se dezvaluie")

choice = input("Enter alegere(1/2/3/4/5):")

if choice == '1':
   num1 = input_fNum() 
   num2 = input_sNum()
   print(num1,"+",num2,"=", add(num1,num2), "\nFacem adunari vai\n")

elif choice == '2':
   num1 = input_fNum() 
   num2 = input_sNum()
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   num1 = input_fNum() 
   num2 = input_sNum()
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   num1 = input_fNum() 
   num2 = input_sNum()
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
         my_friend()
elif choice == '6':
         talent()
elif choice != ('1','2','3','4','5','6'):
         print("v3rs1on1.0.py\n")
else:
   print("Input invalid! Mai incearca..\m")
