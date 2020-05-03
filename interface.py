from tkinter import *

class Interface():
    #create simple chat ui
    def create_window(self):
        self.window = Tk()
        self.window.geometry("300x350")
        self.window.title("NorkQ Chat")
        self.messagesList = Listbox(self.window, width=48, height=19)
        self.messagesList.pack(side=TOP, pady=5)

        self.messageEntry = Text(width=25, height=1)
        self.messageEntry.pack(side=LEFT, padx=5)

        self.sendButon = Button(text="Send", width=10, height=1, command=self.send_message)
        self.sendButon.pack(side=RIGHT, padx=5)
        self.window.mainloop()

    #add item to local list
    def add_message(self, message):
        self.messagesList.insert(END, message)
        self.messageEntry.delete("1.0", END)
        return message

    #get text from chat entry
    def get_text(self):
        return self.messageEntry.get("1.0", END)
