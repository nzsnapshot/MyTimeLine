import tkinter as tk
import pyautogui
import time



class TkToggle(tk.Tk):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.geometry('150x150')


        self.delay = tk.IntVar()
        self.entry = tk.Entry(self, width=10, justify='center', textvariable=self.delay)
        self.entry.grid(row=0,column=0,padx=20,pady=20)


        self.Button = tk.Label(self, text='Start', relief='ridge')
        self.Button.grid(row=1,column=0,ipadx=5)
        self.Button.bind('<Button-1>', self.run)


        self.running = False
        self.programme_running = True
        self.mouseClick = pyautogui.leftClick(100,100)


    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop()
        self.programme_running = False

    def run(self, event):
        while self.programme_running:
            while self.running:
                self.mouseClick
                time.sleep(2)










if __name__ == "__main__":
    app = TkToggle(None)
    app.mainloop()