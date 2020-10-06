#a very simple code for demonstration purpose

from ordering import *
import os
import json
from math import pow,log2,ceil

with open("output.json") as jsonobj:
    data = json.load(jsonobj)


text = ""
enchantment_list = []

while text != "Q":
    print(text)
    text = input("Input the name of enchantment(type q to order): ")
    text = text.title()
    try:
        enchantment = (text,int(data[text]['levelMax'])*int(data[text]['weight']))
        enchantment_list.append(enchantment)
    except:
        print("no such that enchantment")

print("Start ordering...")
print("*"*20)
ordering(enchantment_list)
print("Program ended")
