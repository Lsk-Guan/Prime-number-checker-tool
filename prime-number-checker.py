import math
import tkinter as tk
from tkinter import simpledialog

def prime(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def checker():
    Pnumber = simpledialog.askinteger("Prime Check", "Please enter your prime number below:")
    if Pnumber is not None:
        if prime(Pnumber):
            result = "Confirmed, that's a prime."
        else:
            result = "Looks like it's not a prime number."
        print(result)
        tk.messagebox.showinfo("Result", result)
    else:
        print("Empty content.")

root = tk.Tk()
root.withdraw()  

checker()
