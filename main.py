import tkinter
import customtkinter
import random
from openpyxl import load_workbook

wb = load_workbook(filename='Draw.xlsx')
ws = wb.active

d = {}

for row in list(ws.rows):
    if row[1].value is not None:
        d[row[0].value] = row[1].value
print(d)

set1 = set()


def randomInt(maxvalue):
    return random.randint(1, maxvalue)


def draw(numOfPrize, totalAttendant):
    list0 = []
    list1 = []
    options = True
    for i in range(numOfPrize):
        ranint = randomInt(totalAttendant)
        while ranint in list0 or ranint in set1:
            ranint = randomInt(totalAttendant)
            if len(set1) == totalAttendant:

                if list0 is None:
                    return False
                else:
                    for num in list0:
                        list1.append(d[num])
                    return list1
        list0.append(ranint)
        set1.add(ranint)

    for num in list0:
        list1.append(d[num])
    return list1


def startDraw():
    listOfWinners = draw(int(input1.get()), len(d))
    if not listOfWinners:
        Results.configure(text="You ran out of options! ", text_color="red", font=("Times New Roman", 20, "bold"))

    else:
        Results.configure(text="Winners: \n" + ', '.join(listOfWinners), text_color="blue",
                          font=("Times New Roman", 20, "bold"))


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# frame
app = customtkinter.CTk()
app.geometry("1024x600")
app.title("Draw")

# Adding UI elements
title1 = customtkinter.CTkLabel(app, text="Number of prize: ", font=("Times New Roman", 20, "bold"))
title1.pack(padx=50, pady=70)

num1 = tkinter.StringVar()
input1 = customtkinter.CTkEntry(app, width=350, height=40, textvariable=num1)
input1.pack()

# num2 = tkinter.StringVar()
# title2 = customtkinter.CTkLabel(app, text = "Total attendants: ", font=("Times New Roman", 20, "bold"))
# title2.pack(padx=50, pady=20)
# input2 = customtkinter.CTkEntry(app, width=350, height=40, textvariable=num2)
# input2.pack()

# Draw Button
Draw = customtkinter.CTkButton(app, text="Draw", text_color="black", font=("Times New Roman", 20, "bold"), height=50,
                               width=150, command=startDraw)
Draw.pack(padx=50, pady=70)

Results = customtkinter.CTkLabel(app, text="")
Results.pack(padx=50, pady=30)

# Run app
app.mainloop()
