# Exercise 
# def say_hello():
#     print('Hello, Welcome to Python Functions!')

# Exercise 2
# def print_sum(a,b):
#     print(f"The sum is : {a+b}")    
# print_sum(10,20)    

# Exercise 3
# def print_banner():
#     print(f"=======================\nWELCOME TO MY PROGRAM \n=======================")
# print_banner()

# Exercise 4
# def ask_name():
#     name = input('Enter your name : ')
#     print(name)
# ask_name()


# Level up 
# Exercise 1
# from random import randint as r 
# def number_gueesing_game():
#     num = r(1,10)
#     while True:
#         guees = int(input('Enter your number : '))
#         if guees > num :
#             print('Your number is high')
#         elif guees < num :
#              print('Your number is less ')
#         else:
#             print('You won')
#             break 
# number_gueesing_game()

# Exercise 2
# def mini_atm():
#     balance = 1000
#     while True :
#         print('Welcome to my Mini ATM. You have to enter the number of operation ')
#         op = int(input('1.Check Balance \n2.Withdraw money \n3.Exit \nEnter your number : '))
#         if op == 1 :
#             print(f"Your balance is {balance}")
#         elif op == 2 :
#             take = int(input('Enter how much you will take : ')) 
#             if take < 0 :
#                 print('You enter wrong value ')
#             elif take > balance :
#                 print('Your balance is not enough ')
#             else:
#                 balance-= take 
#                 print(f"You took {take} from your balance and now your balance is { balance }")
#         elif op == 3 :
#             print('You exited....')
#             break     
#         else:
#             print('Thank you for using my ATM')
# mini_atm()

# Exercise 3
# def check_prime():
#     num = int(input('Enter a number here : '))
#     if num < 1 :
#         print('Invalid number!')
#     else:
#         is_prime = False
#         for i in range(2,num):
#             if num % i == 0 :
#                 is_prime = True  
#                 break 
#         if is_prime is True :
#             print('The number is prime ')
#         else:
#             print('The number is not prime')   
# check_prime()             

# Exercise 2 reversed 
def mini_atm():
    balance = 1000 
    while True : 
        print('============\nMini ATM\n============')
        print('1.Check balance')
        print('2.Withdraw money ')
        print('3.Exit')
        choice = int(input('Choose an option (1-3) : '))
        if choice == 1 :
            print(f"Your balance is {balance}")
        elif choice == 2:
            amount = float(input('Enter amount to withdraw : '))
            if amount > balance : 
                print('Error : Insuffiecent funds!')
            elif amount<=0:
                print('invalid amount ')
            else:
                balance-=amount 
                print(f"Successfully withdrew ${amount}.Remaining balance is {balance}")
        elif choice == 3:
            print('Thank you for using our Mini ATM!')
            break 
        else:
            print('Invalid choice! Please choose 1,2, or 3.')
mini_atm()            

    
# New topic of *args and **kwargs 
# def example(**kwargs):
#     for key,val in kwargs.items():
#         print(f"{key.title()} : {val.title()}")
# example(name='akhmet',surname='muratbaev',age='17',langauge='python')        
# Part 1
# Exercise 1
# def multiply_all(*numbers):
#     result = 1
#     for n in numbers :
#         result*=n
#     print(result)
# multiply_all(1,2,3,4,5)

# Exercise 2 
# def find_longest(*words):
#     words = list(words)
#     longest = words[0]
#     for w in words :
#         if len(longest) < len(w) : 
#             longest = w
#     print(longest)    
        
# find_longest('asderljkhgergoergereogheh','asdf','asdfg','asdfgh','asdfghjkl')

# Exercise 3 
# def calculate_average(*numbers):
#     total = sum(numbers)
#     divide = len(numbers)
#     print(f"Total is {total}\nAmount of numbers is {divide}\nAverage : {total/divide}")

# calculate_average(1,2,3,4,5,6,7,8,9,11)














