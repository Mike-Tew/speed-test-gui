from speedtest import Speedtest
from tkinter import Tk, LabelFrame, Button, Label, Checkbutton, IntVar


class Speed_Test_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Test")
        self.geometry(f"+500+300")
        self.download_var = IntVar()
        self.upload_var = IntVar()
        self.ping_var = IntVar()

        self.test_frame = LabelFrame(self, text="Select Tests")
        self.test_frame.grid(row=0, column=0, padx=20, pady=10, ipadx=10, ipady=10)
        self.download_checkbox = Checkbutton(
            self.test_frame, text="Download Test", variable=self.download_var
        )
        self.download_checkbox.grid(row=0, column=0, sticky="w")
        self.upload_checkbox = Checkbutton(
            self.test_frame, text="Upload Test", variable=self.upload_var
        )
        self.upload_checkbox.grid(row=1, column=0, sticky="w")
        self.ping_checkbox = Checkbutton(
            self.test_frame, text="Ping Test", variable=self.ping_var
        )
        self.ping_checkbox.grid(row=2, column=0, sticky="w")
        self.test_button = Button(
            self.test_frame, text="Run Tests", command=self.run_speed_test
        )
        self.test_button.grid(row=1, column=1)

    def download_test(self):
        print("Running Download Test...")
        self.download_result = self.test.download() / 1024 / 1024
        print(f"{self.download_result:.2f} Mbit/s")

    def upload_test(self):
        print("Running Upload Test...")
        self.upload_result = self.test.upload() / 1024 / 1024
        print(f"{self.upload_result:.2f} Mbit/s")


    def run_speed_test(self):
        self.test = Speedtest()
        print("Running test...")
        print("Loading Server List...")
        self.test.get_servers()
        print("Choosing best server...")
        self.best_server = self.test.get_best_server()
        print(self.best_server)

        if self.download_var.get() == 1:
            self.download_test()
        if self.upload_var.get() == 1:
            self.upload_test()
        if self.ping_var.get() == 1:
            print("Ping test")

        # print(
        #     f"Found: {self.best_server['host']} located in {self.best_server['country']}"
        # )


if __name__ == "__main__":
    speed_test_gui = Speed_Test_Gui()
    speed_test_gui.mainloop()
