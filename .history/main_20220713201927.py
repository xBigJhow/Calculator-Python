# ********************************************************** #
#                       Python Calculator                    #
# ********************************************************** #

from tkinter import *
from PIL import 


def key_event(event):
    if event.keysym == 'Return':
        return equals()
    elif event.keysym == 'Delete':
        return clear()
    else:
        return button_press(event.char)


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def equals():

    try:
        global equation_text

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    except SyntaxError:

        equation_label.set('Syntax Error')

        equation_text = ""
    except ZeroDivisionError:

        equation_label.set('Division by Zero')

        equation_text = ""


def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


class Buttons:
    def __init__(self, text, number_button, color: str = 'white') -> None:
        """ Receive args to:
        text: The text that appears in button
        number_button: The value that the number will have
        color: background button color -> color default: white"""

        self.text = text
        self.number_button = number_button
        self.color = color

    def create_button(self):
        return Button(master=frame,
                      text=self.text,
                      height=3,
                      width=8,
                      font=35,
                      bg=self.color,
                      command=lambda: button_press(self.number_button))

    def create_command_button(self):
        return Button(master=frame,
                      text=self.text,
                      height=3,
                      width=8,
                      font=35,
                      bg=self.color,
                      command=self.number_button)


window = Tk()                                   # Creating Windows with Tkinter
window.title("Calculator")                      # Windows Title
window.geometry("322x400")                      # Windows Size
window.resizable(width=False, height=False)     # Not resizable windows
window.config(bg="#2d2e2e")                     # Color background windows




icon_image = PhotoImage()
window.iconphoto(icon_image)


equation_text = ""

equation_label = StringVar()

label = Label(master=window,
              textvariable=equation_label,
              font=('consolas', 20),
              bg="#2d2e2e",
              fg='#f5f5f5',
              width=21,
              height=2,
              anchor=SE,
              text='')
label.pack()

frame = Frame(master=window)
frame.pack()

# Create Button 1
button1 = Buttons(1, 1)
button1.create_button().grid(row=2, column=0)

# Create Button 2
button2 = Buttons(2, 2)
button2.create_button().grid(row=2, column=1)

# Create Button 3
button3 = Buttons(3, 3)
button3.create_button().grid(row=2, column=2)

# Create Button 4
button4 = Buttons(4, 4)
button4.create_button().grid(row=1, column=0)

# Create Button 5
button5 = Buttons(5, 5)
button5.create_button().grid(row=1, column=1)

# Create Button 6
button6 = Buttons(6, 6)
button6.create_button().grid(row=1, column=2)

# Create Button 7
button7 = Buttons(7, 7)
button7.create_button().grid(row=0, column=0)

# Create Button 8
button8 = Buttons(8, 8)
button8.create_button().grid(row=0, column=1)

# Create Button 9
button9 = Buttons(9, 9)
button9.create_button().grid(row=0, column=2)

# Create Button 0
button0 = Buttons(0, 0)
button0.create_button().grid(row=3, column=0)

# Create Button Point
button_point = Buttons('.', '.')
button_point.create_button().grid(row=3, column=1)

# Create Button Equals
button_equals = Buttons('=', equals, '#57baf2')
button_equals.create_command_button().grid(row=3, column=3)

# Create Button Minus
button_minus = Buttons('-', '-')
button_minus.create_button().grid(row=2, column=3)

# Create Button Divider
button_divider = Buttons('/', '/')
button_divider.create_button().grid(row=0, column=3)

# Create Button Multiply
button_multiply = Buttons('*', '*')
button_multiply.create_button().grid(row=1, column=3)

# Create Button Add
button_add = Buttons('+', '+')
button_add.create_button().grid(row=3, column=2)

# Create Button Clear
button_add = Buttons('Clear', clear)
button_add.create_command_button().grid(row=4, column=3)


# Create Key Event 0
window.bind('0', key_event)

# Create Key Event 1
window.bind('1', key_event)

# Create Key Event 2
window.bind('2', key_event)

# Create Key Event 3
window.bind('3', key_event)

# Create Key Event 4
window.bind('4', key_event)

# Create Key Event 5
window.bind('5', key_event)

# Create Key Event 6
window.bind('6', key_event)

# Create Key Event 7
window.bind('7', key_event)

# Create Key Event 8
window.bind('8', key_event)

# Create Key Event 9
window.bind('9', key_event)

# Create Key Event Divider
window.bind('</>', key_event)

# Create Key Event Minus
window.bind('<minus>', key_event)

# Create Key Event Add
window.bind('<plus>', key_event)

# Create Key Event Period
window.bind('period', key_event)

# Create Key Event Multiply
window.bind('<asterisk>', key_event)

# Create Key Event Equals
window.bind('<Return>', key_event)

# Create Key Event Clear
window.bind('<Delete>', key_event)

window.mainloop()
