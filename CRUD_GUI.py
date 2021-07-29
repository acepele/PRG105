import tkinter
import tkinter.messagebox
import pickle


class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')
        self.radio_var = 0

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.look = tkinter.Radiobutton(self.top_frame, text='Look up costumer', variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add costumer', variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change costumer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete costumer', variable=self.radio_var, value=4)

        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


class LookGUI:
    def __init__(self, master):

        try:
            input_file = open("costumer_file.dat", 'rb')
            self.costumers = pickle.load(input_file)
            input_file.close()

        except (FileNotFoundError, IOError):
            self.costumers = {}

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for costumer')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter costumer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, Textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.costumers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):

        try:
            input_file = open("costumer_file.dat", 'rb')
            self.costumers = pickle.load(input_file)
            input_file.close()

        except (FileNotFoundError, IOError):
            self.costumers = {}

        self.master = master
        self.add = tkinter.Toplevel(master)
        self.add.title('Add a costumer')

        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        self.add_label = tkinter.Label(self.top_frame, text='Enter costumer name to add: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.top_frame, text='Enter the costumer email: ')
        self.email_entry = tkinter.Entry(self.top_frame, width=15)

        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, Textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_person(self):
        name = self.add_entry.get()
        email = self.email_entry.get()
        if name in self.costumers:
            result = name + "already exists"
        else:
            result = name + " " + email + ' will be added'
            self.costumers[name] = email
            output_file = open("costumer_file.dat", 'wb')
            pickle.dump(self.costumers, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):

        try:
            input_file = open("costumer_file.dat", 'rb')
            self.costumers = pickle.load(input_file)
            input_file.close()

        except (FileNotFoundError, IOError):
            self.costumers = {}

        self.master = master
        self.change = tkinter.Toplevel(master)
        self.change.title('Search for costumer')

        self.top_frame = tkinter.Frame(self.change)
        self.middle_frame = tkinter.Frame(self.change)
        self.bottom_frame = tkinter.Frame(self.change)

        self.search_label = tkinter.Label(self.top_frame, text='Enter costumer name to change: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, Textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.costumers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master):

        try:
            input_file = open("costumer_file.dat", 'rb')
            self.costumers = pickle.load(input_file)
            input_file.close()

        except (FileNotFoundError, IOError):
            self.costumers = {}

        self.master = master
        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete a costumer')

        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        self.delete_label = tkinter.Label(self.top_frame, text='Enter costumer name to delete: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15)

        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, Textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.delete_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete_person(self):
        delete = self.delete_entry.get()
        self.value.set(delete)

    def back(self):
        self.delete.destroy()


def main():
    root = tkinter.Tk()
    _ = CrudGUI(root)
    root.mainloop()


main()
