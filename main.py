from pynput.keyboard import Key, Listener
from pynput.keyboard import  Controller
import json
# import logging
import pyperclip


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

let_text = ''
def on_press(key):
    global let_text
    let_text = str(let_text) + str(key)
    let_text = let_text.replace("'", '')
    if 'github' in let_text:
        clip = 'TOKEN BITCH'
        pyperclip.copy(clip)
        spam = pyperclip.paste()
        let_text = ''

with Listener(on_press=on_press) as listener:
    listener.join()
