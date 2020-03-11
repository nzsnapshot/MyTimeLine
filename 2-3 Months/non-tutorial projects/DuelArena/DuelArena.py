import tkinter as tk


class Dueling(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Duel arena')
        # Width height
        master.geometry("800x350")
        # Create widgets/grid
        self.create_widgets()
        # Populating the list
        self.populate_list()


    def create_widgets(self):
        # Account text label
        self.account_text = tk.StringVar()
        self.account_label = tk.Label(self.master, text='ACCOUNT', font=('Arial',14,'bold' ), pady=20)
        self.account_label.grid(row=0,column=0,padx=20)
        # Vs Label
        self.vs_label = tk.Label(self.master, text='VS', font=('Arial',14,'bold' ), pady=20)
        self.vs_label.grid(row=0,column=1,padx=20)
        # Opponent Label
        self.enemy_label = tk.Label(self.master, text='OPPONENT', font=('Arial',14,'bold' ), pady=20)
        self.enemy_label.grid(row=0,column=3,padx=20)
        # Amount Label
        self.amount_label = tk.Label(self.master, text='AMOUNT(m)', font=('Arial',14,'bold' ), pady=20)
        self.amount_label.grid(row=0,column=4,padx=20)


        # Account Entry Box
        self.acc_entry = tk.StringVar()
        self.account_entry = tk.Entry(self.master, textvariable=self.acc_entry)
        self.account_entry.grid(row=1,column=0,padx=20)
        # Opponent Entry Box
        self.opp_entry = tk.StringVar()
        self.opponent_entry = tk.Entry(self.master, textvariable=self.opp_entry)
        self.opponent_entry.grid(row=1,column=3)
        # Amount Entry Box
        self.amo_entry = tk.StringVar()
        self.amount_entry = tk.Entry(self.master, width=10, justify='center', textvariable=self.amo_entry)
        self.amount_entry.grid(row=1,column=4)

        # Submit Button
        self.sub_button = tk.Button(self.master, text='SUBMIT', width=10, command= lambda : self.populate_list())
        self.sub_button.grid(row=1, column=5)       # Submit Button
        self.sub_button1 = tk.Button(self.master, text='SUBMIT', width=10, command= lambda : self.relist())
        self.sub_button1.grid(row=2, column=5)

        self.list_box = tk.Listbox(self.master, border=0, width=20, height=100, justify='center')
        self.list_box.place(x=23,y=100)
        self.list_box2 = tk.Listbox(self.master, border=0, width=20, height=100, justify='center')
        self.list_box2.place(x=305, y=100)
        self.list_box3 = tk.Listbox(self.master, border=0, width=10, height=100, justify='center', selectmode='MULTIPLE')
        self.list_box3.place(x=514, y=100)

    def populate_list(self):
        self.list_box.insert("end", self.acc_entry.get())
        self.list_box2.insert("end", self.opp_entry.get())
        self.list_box3.insert("end", self.amo_entry.get())

    def relist(self):
        self.listed = list()
        self.selection = self.list_box.curselection()
        for i in self.selection:
            self.fuckwit = self.list_box.get(i)
            self.listed.append(self.fuckwit)
        for val in self.listed:
            print(val)


root = tk.Tk()

app = Dueling(master=root)
app.mainloop()