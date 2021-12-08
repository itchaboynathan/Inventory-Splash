import os,sys,json
from subprocess import call
from pprint import pprint

#Creates a new inventory item when called                                                                                       
def build(material,size,amount):                                                                                                
    material = input('[Material?]')                                                                                             
    size = input('[Size?]')                                                                                                     
    amount = input('[Amount?]')                                                                                                 
                                                                                                                                
    created_object = Item(material,size,amount)                                                                                 
    json_save(created_object)                                                                                                   
    return created_object                                                                                                       
                                                                                                                                
def json_save(object):                                                                                                          
    j = json.loads('base.json')                                                                                                 
    json_data = [object]                                                                                                        
    with open('base.json', 'a') as f:                                                                                           
        json_data.append(object.__dict__)                                                                                       
        json.dumps(json_data, f, ensure_ascii=False, sort_keys=False,  indent=4)                                                
                                                                                                                                
def prnt(doc):                                                                                                                  
    splash = open(doc,'r')                                                                                                      
    file_contents = splash.read()                                                                                               
    print(file_contents)                                                                                                        
                                                                                                                                
#Blueprint for the inventory item                                                                                               
class Item(object):                                                                                                                     json_data.append(object.__dict__)
        json.dumps(json_data, f, ensure_ascii=False, sort_keys=False,  indent=4)

def prnt(doc):
    splash = open(doc,'r')
    file_contents = splash.read()
    print(file_contents)

#Blueprint for the inventory item
class Item(object):
    material = ''
    size = 0
    amount = 0
    def __init__(self,material,size,amount):
        self.material = material
        self.size = size
        self.amount = amount
        
#Handles user input and information output
class user_interface():
    def clear():
        call('clear' if os.name =='posix' else 'cls')
    def splash():
        material = ''
        size = 0
        amount = 0

        prnt('splash.txt')

        person = input('[Terminal]')

        if person  == '1':
            print()
        elif person == '2':
            build(material,size,amount)
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





