from pynput.keyboard import Key, Listener
from pynput.keyboard import  Controller
import json
# import logging
import pyperclip


# retrive json data
with open('things.json', 'r') as things:
    x = json.load(things)



def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

let_text = ''
def on_press(key):
    global let_text
    let_text = str(let_text) + str(key)
    let_text = let_text.replace("'", '')

    #################################
    for thing in x:
        if thing in let_text:
            clip = x[thing]
            pyperclip.copy(clip)
            pyperclip.paste()
            let_text = ''

with Listener(on_press=on_press) as listener:
    listener.join()
