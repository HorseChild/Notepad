from tkinter import *
from tkinter import ttk

short_break = 5*60
long_break = 10*60
work_time = 25*60
long_work_time = 50*60

root = Tk()
root.geometry("400x300")
root.title("Pomodoro Timer")
style = Style(theme="Simplex")
style.theme_use()

mainframe = ttk.Frame(root, padding=(10, 10, 10, 10))
mainframe.grid(column=5, row=5, sticky=(N, W, E, S))

time = StringVar()
time_entry = ttk.Entry(mainframe, width=300, height=400, textvariable=time)
time_entry.grid(column=2, row=1, sticky=(W, E))

def start_timer():
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    is_running = True
    update_timer()
def stop_timer():
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    is_running = False
def update_timer():
    if is_running:
        if is_work_time:
            time.set(f"{work_time // 60:02d}:{work_time % 60:02d}")
            work_time -= 1
            if work_time <= 0:
                is_work_time = False
                blocks_completed += 1
                if blocks_completed % 4 == 0:
                    break_time = long_break
                    MessageBox.showinfo("Great job!", "You've earned a long break!")
                else:
                    break_time = short_break
                    MessageBox.showinfo("Time for a break!", "Take a small break to relax.")
        else:
            time.set(f"{break_time // 60:02d}:{break_time % 60:02d}")
            break_time -= 1
            if break_time <= 0:
                is_work_time = True
                MessageBox.showinfo("Back to work!", "Time to focus on your tasks.")
