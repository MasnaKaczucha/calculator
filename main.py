import tkinter


def addition():
    print('add shit')


def subtraction():
    print('subtract shit')


def division():
    print('divide shit')


def multiplication():
    print('multiply shit')


def exponentiation():
    print('to the power of shit')


def square_root():
    print('square root of shit')


root = tkinter.Tk()
root.geometry('500x500')

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

button = []
for num in nums:
    button.append(tkinter.Button(root, text=num))

button[7].grid(row=0, column=0, sticky="w", pady=2)
button[8].grid(row=0, column=1, sticky="w", pady=2)
button[9].grid(row=0, column=2, sticky="w", pady=2)

button[4].grid(row=1, column=0, sticky="w", pady=2)
button[5].grid(row=1, column=1, sticky="w", pady=2)
button[6].grid(row=1, column=2, sticky="w", pady=2)


tkinter.mainloop()