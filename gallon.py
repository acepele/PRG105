import tkinter


class MPG:
    def __init__(self):
        # create main window
        self.gallons = float(self.gallons_entry.get())
        self.main_window = tkinter.Tk()

        # create four frames
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.gallons_frame, text='Enter how many gallons your car holds: ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.miles_frame, text='How many miles have you traveled: ')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.result_label = tkinter.Label(self.mpg_frame, text=' Converted to miles Per gallons')

        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg)

        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text='Convert', command=self.calc_mpg)

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.mpg_frame.pack()
        self.button_frame.pack()

    def calc_mpg(self):
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())
        # calculate MPG
        self.miles_per_gallon = self.miles / self.gallons
        self.mpg.set(str(round(self.miles_per_gallon, 2)))


carmpg = MPG()
