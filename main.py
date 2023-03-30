import tkinter

root = tkinter.Tk()
root.geometry('200x300')


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rownum = 6
colnum = 4

for a in range(rownum):
    for b in range(colnum):
        root.rowconfigure(a, weight=1)
        root.columnconfigure(b, weight=1)


entry = tkinter.Entry(root)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

calc = ""
# lmfao
def count(value):
    global entry
    global calc

    entry.insert("end", value)
    calc += value

    return calc


def create_button(num):
    content = (tkinter.Button(root, text=num, command=lambda: count(str(num))))
    button.append(content)


button = []
for num in nums:
    create_button(num)


button[7].grid(row=2, column=0, sticky="nsew")
button[8].grid(row=2, column=1, sticky="nsew")
button[9].grid(row=2, column=2, sticky="nsew")

button[4].grid(row=3, column=0, sticky="nsew")
button[5].grid(row=3, column=1, sticky="nsew")
button[6].grid(row=3, column=2, sticky="nsew")

button[1].grid(row=4, column=0, sticky="nsew")
button[2].grid(row=4, column=1, sticky="nsew")
button[3].grid(row=4, column=2, sticky="nsew")
button[0].grid(row=5, column=0, columnspan=2, sticky="nsew")

clr_all = tkinter.Button(root, text="AC")
clr_all.grid(row=1, column=0, sticky="nsew")

exp = tkinter.Button(root, text="x^2")
exp.grid(row=1, column=1, sticky="nsew")

sqrt = tkinter.Button(root, text="√")
sqrt.grid(row=1, column=2, sticky="nsew")

div = tkinter.Button(root, text="÷")
div.grid(row=1, column=3, sticky="nsew")

mult = tkinter.Button(root, text="X")
mult.grid(row=2, column=3, sticky="nsew")

sub = tkinter.Button(root, text="-")
sub.grid(row=3, column=3, sticky="nsew")

add = tkinter.Button(root, text="+")
add.grid(row=4, column=3, sticky="nsew")

result = tkinter.Button(root, text="=")
result.grid(row=5, column=3, sticky="nsew")

point = tkinter.Button(root, text=",")
point.grid(row=5, column=2, sticky="nsew")

tkinter.mainloop()
