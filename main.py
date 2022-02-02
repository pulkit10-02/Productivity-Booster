from tkinter import *
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
TIMER = None
check_marks_list = ['✔', '✔✔', '✔✔✔', '✔✔✔✔']
i = 1
FREQ = DUR = 500


def start_timer():
    global REPS
    if REPS in (1, 3, 5, 7):

        timer_label.config(text='WORK', fg=RED)
        count_down(WORK_MIN * 60)
        my_canvas.itemconfig(timer_image, image=img_work)
    elif REPS in (2, 4, 6):

        timer_label.config(text='BREAK', fg=GREEN)
        count_down(SHORT_BREAK_MIN * 60)
        my_canvas.itemconfig(timer_image, image=img_break)

    elif REPS==8:
        my_canvas.itemconfig(timer_image, image=img_break)
        timer_label.config(text='BREAK', fg=GREEN)
        count_down(LONG_BREAK_MIN * 60)
    else:
        reset_timer()

    REPS += 1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, i, TIMER
    my_screen.after_cancel(TIMER)
    my_screen.after(1000)
    my_canvas.itemconfig(timer_image, image=bgpic)
    my_canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer')
    check_label.config(text='')
    REPS = i = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global i, REPS, TIMER
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'
    else:
        count_min = f'{count_min}'

    my_canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        TIMER = my_screen.after(1000, count_down, count - 1)
    else:
        winsound.Beep(FREQ, DUR)
        if REPS % 2 == 0:
            check_label.config(text=check_marks_list[i - 1])
            i += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
my_screen = Tk()
my_screen.title("Productivity Booster")
my_screen.minsize(height=400, width=500)
my_screen.config(bg=YELLOW, padx=70, pady=70)
img_break = PhotoImage(file='take a break.png')
img_work = PhotoImage(file='working.png')

my_canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
bgpic = PhotoImage(file="begin.png")
timer_image = my_canvas.create_image(125, 125, image=bgpic)
timer_text = my_canvas.create_text(125, 210, text='00:00', fill='black', font=(FONT_NAME, 35, 'bold'))
my_canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', highlightthickness=0, bg=YELLOW, fg='black', font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text='', fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)

my_screen.mainloop()
