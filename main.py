# Python 2.7.5 Terminal OS, Windows 1 based terminal.

# Imports

import time

import os

import socket

from Tkinter import *

# Start code

def start_code():

   print("Python 2.7.5 Terminal OS, Windows 1 based terminal ")

   print("Type help() to print on the screen all commands ")

# Input command

def input_command():

   input_command = raw_input("> ")

   if input_command == "help()":

       help()

   elif input_command == "calculator()":

       calculator()

   elif input_command == "time_command()":

       time_command()

   elif input_command == "file_command()":

       file_command()

   elif input_command == "PC_shutdown()":

       PC_shutdown()

   elif input_command == "PC_restart()":

       PC_restart()

   elif input_command == "IP_address()":

       IP_address()

   elif input_command == 'list()':

       dir_list = os.listdir(path)

       print("Files and Directories in '", path, "' :")

       print(dir_list)

   elif input_command == "list -a()":

       file_var = raw_input("Enter The Direct File Path To Read: ")

       dir_list2 = os.listdir(file_var)

       print("Files and directories in '", file_var, "':")

       print(dir_list2)

   elif input_command == "exit()" or "quit()":

       quit()

# Help

def help():

   print("help(), calculator(), time_command(), file_command(), PC_shutdown(), PC_restart(), IP_address(), list(), list -a(), exit(), quit()")

   input_command()

# IP address

def IP_address():

   hostname = socket.gethostname()

   IP_address = socket.gethostbyname(hostname)

   print(IP_address)

# Date and Time

def time_command():

   t = time.localtime(time.time())

   time_string = "Date and time: " + time.asctime(t)

   print(time_string)

# Shutdown PC

def PC_shutdown():

   os.system("shutdown /s /t 1")

# Restart PC

def PC_restart():

   os.system("shutdown /r /t 1")

# File command

def file_command():

   what_to_write = raw_input("Input what to write in here ")

   file_var = open("file_python", "w")

   file_var.write(what_to_write)

   file_var.close()

# Calculator

def calculator():

   num1 = float(input("Number One "))

   op = raw_input("Operator ")

   num2 = float(input("Number Two "))

   if op == "+":

       print(num1 + num2)

   elif op == "-":

       print(num1 - num2)

   elif op == "/":

       print(num1 / num2)

   elif op == "*":

       print(num1 * num2)

   else:

       print("Invalid")

# Terminal

path = 'C:/'

print("Terminal OS [Version 1.00]")

start_code()

while True:

   input_command()

