from tkinter import *
tk = Tk()

result = ''

def btn_click(value):
    global result

    if value == '=':
        result = str(eval(result))
    else:
        result = result + value
    lbl['text'] = result
    

lbl = Label(tk, text='0', height=5)
lbl.grid(row=0, columnspan=4)

btn = Button(tk, text='1', width=5, command=lambda:btn_click('1'))
btn.grid(row=1, column=0)
btn = Button(tk, text='2', width=5, command=lambda:btn_click('2'))
btn.grid(row=1, column=1)
btn = Button(tk, text='3', width=5, command=lambda:btn_click('3'))
btn.grid(row=1, column=2)
btn = Button(tk, text='+', width=5, command=lambda:btn_click('+'))
btn.grid(row=1, column=3)

btn = Button(tk, text='4', width=5, command=lambda:btn_click('4'))
btn.grid(row=2, column=0)
btn = Button(tk, text='5', width=5, command=lambda:btn_click('5'))
btn.grid(row=2, column=1)
btn = Button(tk, text='6', width=5, command=lambda:btn_click('6'))
btn.grid(row=2, column=2)
btn = Button(tk, text='-', width=5, command=lambda:btn_click('-'))
btn.grid(row=2, column=3)

btn = Button(tk, text='7', width=5, command=lambda:btn_click('7'))
btn.grid(row=3, column=0)
btn = Button(tk, text='8', width=5, command=lambda:btn_click('8'))
btn.grid(row=3, column=1)
btn = Button(tk, text='9', width=5, command=lambda:btn_click('9'))
btn.grid(row=3, column=2)
btn = Button(tk, text='*', width=5, command=lambda:btn_click('*'))
btn.grid(row=3, column=3)

btn = Button(tk, text='0', width=5, command=lambda:btn_click('0'))
btn.grid(row=4, column=0)
btn = Button(tk, text='=', width=5, command=lambda:btn_click('='))
btn.grid(row=4, column=2)
btn = Button(tk, text='/', width=5, command=lambda:btn_click('/'))
btn.grid(row=4, column=3)


tk.mainloop()