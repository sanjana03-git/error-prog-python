#Filenotfounderror
# with open("file.txt") as f:
#     print(f.read())

#Keyerror
# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["gender"])

#Indexerror
# my_list = [1, 2, 3]   
# print(my_list[5])

#Typeerror
# result = "Hello" + 5


# try:
#     file = open("file.txt")
# except:
#     file = open("error/file.txt", "w")
#     file.write("This is a new file created because the original file was not found.")
# finally:
#     file.close()

# try:
#     with open("file.txt") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("The file 'file.txt' was not found.")

# try:   
#     my_dict = {"name": "Alice", "age": 30}
#     print(my_dict["gender"])
# except KeyError:
#     print("The key 'gender' was not found in the dictionary.")

# try:
#     my_list = [1, 2, 3]   
#     print(my_list[5])
# except IndexError:
#     print("The index 5 is out of range for the list.")

# try:
#     result = "Hello" + 5
# except TypeError:
#     print("Cannot concatenate a string and an integer.")


#use try,  except, else, finally
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
# except ValueError:
#     print("Please enter valid integers.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print(f"The result of {num1} divided by {num2} is: {result}")
# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not.")

#Raising exceptions
# def divide_numbers(num1, num2):
#     if num2 == 0:
#         raise ValueError("Cannot divide by zero.")
#     return num1 / num2
# try:
#     result = divide_numbers(10, 0)
#     print(f"The result is: {result}")
# except ValueError as e:
#     print(f"Error: {e}")



