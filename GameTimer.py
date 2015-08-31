__author__ = 'Rizal'

from tkinter import *
import win32api
import win32con
import time
# from _thread import start_new_thread


class GameTimer:
    #FRAME_WIDTH = 5
    #FRAME_HEIGHT = 5
    START_FLAG = False
    START_KEY = win32con.VK_F10
    STOP_KEY = win32con.VK_F11

    def __init__(self, master):
        self.curr_time_sec = 0
        self.curr_time_min = 0
        self.curr_time_hour = 0

        # self.frame = Frame(master, width=100, height=50)
        # self.frame.grid_slaves(self.FRAME_HEIGHT, self.FRAME_WIDTH)
        self.time_label = Label(master, text=self.get_curr_time(), fg='green', bg='black', font=('System', 60, 'bold'))
        self.time_label.grid(row=0, column=0, padx=40, pady=40)

        self.start_label = Label(master, text='Start Timer : F10', fg='red', bg='black', font=('System', 10, 'bold'))
        self.stop_label = Label(master, text='Stop Timer : F11', fg='red', bg='black', font=('System', 10, 'bold'))

        self.start_label.place(relx=.05, rely=.05)
        self.stop_label.place(relx=.05, rely=.15)

        self.start_count()

    def start_count(self):
        while True:
            main_window.update()
            if win32api.GetAsyncKeyState(self.START_KEY) != 0:
                self.START_FLAG = True
            if win32api.GetAsyncKeyState(self.STOP_KEY) != 0:
                self.START_FLAG = False
            if self.START_FLAG:
                main_window.update()
                self.curr_time_sec += 1
                time.sleep(1)
                if self.curr_time_sec >= 60:
                    self.curr_time_sec -= 60
                    self.curr_time_min += 1
                if self.curr_time_min >= 60:
                    self.curr_time_min -= 60
                    self.curr_time_hour += 1

                print(self.get_curr_time())
                self.time_label.config(text=self.get_curr_time())

    def get_curr_time(self):
        return str(self.curr_time_hour).zfill(2) + ':' \
               + str(self.curr_time_min).zfill(2) + ':' \
               + str(self.curr_time_sec).zfill(2)

    def setlab(self):
        self.time_label.config(text="ForFun")

if __name__ == '__main__':
    main_window = Tk()
    main_window.resizable(width=FALSE, height=FALSE)
    main_window.title('GameTimer')
    main_window.config(background='black')
    ui = GameTimer(main_window)
    main_window.mainloop()

