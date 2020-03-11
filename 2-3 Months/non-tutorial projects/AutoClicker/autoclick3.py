import tkinter as tk
import time
import pyautogui
import threading

root = tk.Tk()
root.geometry('175x150')

class AutoClick(threading.Thread):
    def __init__(self, master):
        super(AutoClick).__init__()
        self.master = master
        self.program_running = False

        self.delay = tk.IntVar()
        self.entry = tk.Entry(root, width=5, textvariable=self.delay, justify='center')
        self.entry.grid(row=0,column=0,pady=20,padx=20)

        self.var = tk.IntVar()
        self.label1 = tk.Label(root, text='',textvariable=self.var, width=5, justify='center')
        self.label1.grid(row=1,column=0,pady=20,padx=20)

        self.startButton = tk.Button(root, text='Start (f)', command=self.start_clicking)
        self.startButton.grid(row=0, column=1,ipady=2,ipadx=5)

        self.stopButton = tk.Button(root, text='Stop', command=self.stop_clicking)
        self.stopButton.grid(row=0, column=2,ipady=2,ipadx=5)

        self.click = 0

    # master.bind('f', self.stop_clicking)
    # def keyevent(self, _event=None):
    #     self.int = self.delay.get()
    #     self.key = True
    #     while self.key:
    #         pyautogui.click(pause=self.int)

    def run(self):
        self.running = True
        self.int = self.delay.get()
        while self.running:
            pyautogui.leftClick()
            time.sleep(self.int)
            self.var.set(self.var.get() + 1)


    def start_clicking(self):
        th = threading.Thread(target=self.run)
        th.start()

    def stop_clicking(self):
        self.running = False
        self.key = False

if __name__ == '__main__':
    auto = AutoClick(root)
    tk.mainloop()