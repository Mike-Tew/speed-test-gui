import speedtest
from tkinter import Tk, Button, Label



class Speed_Test_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Test")
        self.geometry("400x300+900+300")
        self.test_button = Button(text="Run Test", command=self.run_speed_test)
        self.test_button.grid(row=0, column=0)


    def run_speed_test(self):
        print("Running test...")
        self.test = speedtest.Speedtest()
        print("Loading Server List...")
        self.test.get_servers()
        print("Choosing best server...")
        self.best_server = self.test.get_best_server()
        print(self.best_server)
        pass


if __name__ == "__main__":
    speed_test_gui = Speed_Test_Gui()
    speed_test_gui.mainloop()