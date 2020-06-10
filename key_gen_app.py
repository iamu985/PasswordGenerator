import tkinter as tk
import pyperclip as pc
from random_key_gen import RandomKeyGenerator

def generate_key(event):
    key = scaler_key.get()
    generator = RandomKeyGenerator(key)
    get_key = generator.run()
    lbl_keygen['text'] = get_key

    copy_key = pc.copy(get_key)
    print('Key Copied')
    
    

def reset_event(event):
    lbl_keygen['text'] = 'Random Key Generator'

window = tk.Tk()
window.configure(bg='#b8edd3')
window.title('Random Key Generator')

window.rowconfigure([i for i in range(8)], weight=1, minsize=30)
window.columnconfigure([i for i in range(20)], weight=1, minsize=30)

lbl_scale = tk.Label(window, text='Length of Key', font=10, relief=tk.GROOVE, bg='#bbccdd', borderwidth=5)
lbl_scale.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=7)

scaler_key = tk.Scale(window, from_=8, to=35, tickinterval=1, orient=tk.HORIZONTAL, bg='light blue', bd=2, relief=tk.RAISED)
scaler_key.grid(row=3, column=3, columnspan=15, sticky='ew')

lbl_keygen = tk.Label(window, text='Randomly Generated key', bg='#bebebe', relief=tk.SUNKEN, borderwidth=5, font=14)
lbl_keygen.grid(row=2, column=0, columnspan=20, sticky='ew', padx=5, pady=5)

btn_generate =  tk.Button(window, text='Generate',relief=tk.RAISED, bg='#e1f7d5', bd=3)
btn_generate.grid(row=5, column=4, columnspan=5, sticky='ew')
btn_generate.bind('<Button-1>', generate_key)

btn_reset = tk.Button(window, text='Reset', relief=tk.RAISED, bg='#e1f7d5', bd=3)
btn_reset.grid(row=5, column=10, columnspan=5, sticky='ew')
btn_reset.bind('<Button-1>', reset_event)

window.mainloop()


