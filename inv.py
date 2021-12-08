import os,sys,json
from subprocess import call
from pprint import pprint

#Creates a new inventory item when called
def build(name,material,size,amount):
    name = input('[Name?]')
    material = input('[Material?]')
    size = input('[Size?]')
    amount = input('[Amount?]')
    
    created_object = Item(name,material,size,amount)
    json_save(created_object)
    return created_object

def json_save(object):
    with open('base.json', 'w', encoding='utf-8') as f:
        json.dump(object.__dict__, f, ensure_ascii=False, indent=4)

#Blueprint for the inventory item
class Item(object):
    name = ''
    material = ''
    size = 0
    amount = 0
    def __init__(self,name,material,size,amount):
        self.name = name
        self.material = material
        self.size = size 
        self.amount = amount

#Handles user input and information output
class user_interface():
    def clear():
        call('clear' if os.name =='posix' else 'cls')
    def splash():
        name = ''
        material = ''
        size = 0
        amount = 0

        splash = open('splash.txt','r')
        file_contents = splash.read()
        print(file_contents)
        person = input('[Terminal]')
        
        if person  == '1':
            print()
        elif person == '2':
            build(name,material,size,amount)
        elif person == '3':
            print()
        elif person == '4':
            print()
        elif person == '5':
            print()
        else:
            user_interface.clear()
            user_interface.splash()


face = user_interface
face.splash()




