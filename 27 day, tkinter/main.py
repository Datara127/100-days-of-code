from tkinter import *


def main_func():
    window = Tk()
    window.title("GUI ")

    enter_miles = Entry()
    enter_miles.grid(row=0, column=1)
    enter_miles.config(width=9)

    label_1 = Label(text="Miles")
    label_1.config(padx=5, pady=5)
    label_1.grid(row=0, column=2)
    label_2 = Label(text="is equal to")
    label_2.grid(row=1, column=0)
    label_3 = Label(text="0")
    label_3.grid(row=1, column=1)
    label_4 = Label(text="km")
    label_4.grid(row=1, column=2)

    def click_calc():
        label_3.config(text=round(float(enter_miles.get()) * 1.609))

    button_calc = Button(text="Calculate", command=click_calc)
    button_calc.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    main_func()
