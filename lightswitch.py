import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

flip = False

def switch():
    global flip,button
    if flip == False:
        button.config(text='button is on')
        window.configure(bg='yellow')
        print('button is on')
        flip = True
    else:
        button.config(text='button is off')
        window.configure(bg='black')
        print('button is off')
        flip = False

window.configure(bg='black')
button.config(text='button is off',command=switch)
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

window.mainloop()