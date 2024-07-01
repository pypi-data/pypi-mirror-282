"""
Gameplus: A simple way to make text based games in Python.
Useful tools:
Ascii Text Art Generator: patorjk.com/software/taag/
LICENSE:
Copyright 2024 Alexander DeStefano

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from types import FunctionType
# menu: Creates a simple menu. (options = [(text,function)...], mode = "keypress"|"input", clearterm = True|False)
def menu(options: list|dict,mode="keypress",clearterm=True,call=True) -> FunctionType:
    def makescreen(si: int,screens: list) -> FunctionType:
        if clearterm: clear()
        from time import sleep
        sleep(.25)
        c = 0
        for i in screens[si]:
            print(f"{str(c)}: {i[0]}")
            c += 1
        def manage(number):
            if number >= len(screens[si]):
                print("Invalid option, please pick another.\nPress Enter.")
                input()
                return makescreen(si,screens)
            if screens[si][number][0] == "Previous Page" and screens[si][number][1] == None:
                return makescreen(si-1,screens)
            elif screens[si][number][0] == "Next Page" and screens[si][number][1] == None:
                return makescreen(si+1,screens)
            else:
                return screens[si][number][1]
        if mode == 'keypress':
            import keyboard
            while True:
                if keyboard.is_pressed('0'):
                    return manage(0)
                elif keyboard.is_pressed('1'):
                    return manage(1)
                elif keyboard.is_pressed('2'):
                    return manage(2)
                elif keyboard.is_pressed('3'):
                    return manage(3)
                elif keyboard.is_pressed('4'):
                    return manage(4)
                elif keyboard.is_pressed('5'):
                    return manage(5)
                elif keyboard.is_pressed('6'):
                    return manage(6)
                elif keyboard.is_pressed('7'):
                    return manage(7)
                elif keyboard.is_pressed('8'):
                    return manage(8)
                elif keyboard.is_pressed('9'):
                    return manage(9)
        elif mode == 'input':
            sel = input()
            try:
                return manage(int(sel))
            except TypeError:
                print("Invalid option, please pick another.\nPress Enter.")
                input()
                return makescreen(si,screens)
    if type(options) == list:
        from math import floor
        mx = 10
        screens = [[] for i in range(0,floor((len(options)-1)/mx)+1)]
        c = 0
        l = 0
        for i in options:
            if c%mx == mx-2 and l != 0:
                screens[l].append(("Previous Page",None))
                screens[l].append(("Next Page",None))
                l+=1
                c+=2
            elif c%mx == mx-1 and l == 0:
                screens[l].append(("Next Page",None))
                l+=1
                c+=1
            screens[l].append(i)
            c+=1
        if l > 0:
            screens[::-1][0].append(("Previous Page",None))
        c = makescreen(0,screens)
        if call:
            c()
        return c
    elif type(options) == dict:
        if clearterm: clear()
        for i,t in options.items():
            print(i+":",t[0])
        sel = input()
        if not sel in list(options.keys()):
            print("Invalid option, please pick another.\nPress Enter.")
            input()
            menu(options,mode,clearterm)
        else:
            c = options[sel][1]
            if call:
                c()
            return c
    else:
        raise TypeError(f"Invalid options type \"{str(type(options))}\". Type must be list or dictionary.")
#clear: clears the terminal. ().
def clear():
    from os import system,name
    if name == 'nt':
        system('cls')
    else:
        system('clear')