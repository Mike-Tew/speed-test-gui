import speedtest
from tkinter import Tk, LabelFrame, Button, Label, Checkbutton


class Speed_Test_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Test")
        self.geometry("+900+300")
        self.test_frame = LabelFrame(self, text="Select Tests")
        self.test_frame.grid(row=0, column=0, padx=20, pady=10, ipadx=10, ipady=10)
        self.download_checkbox = Checkbutton(self.test_frame, text="Download Test")
        self.download_checkbox.grid(row=0, column=0, sticky="w")
        self.upload_checkbox = Checkbutton(self.test_frame, text="Upload Test")
        self.upload_checkbox.grid(row=1, column=0, sticky="w")
        self.ping_checkbox = Checkbutton(self.test_frame, text="Ping Test")
        self.ping_checkbox.grid(row=2, column=0, sticky="w")
        self.test_button = Button(
            self.test_frame, text="Run Tests", command=self.run_speed_test
        )
        self.test_button.grid(row=1, column=1)

    def run_speed_test(self):
        print("Running test...")
        self.test = speedtest.Speedtest()
        print("Loading Server List...")
        self.test.get_servers()
        print("Choosing best server...")
        self.best_server = self.test.get_best_server()
        print(self.best_server)
        print(
            f"Found: {self.best_server['host']} located in {self.best_server['country']}"
        )

        print("Performing download test...")
        self.download_result = self.test.download()
        print("Performing upload test...")
        self.upload_result = self.test.upload()
        self.ping_result = self.test.results.ping

        print(self.download_result)
        print(self.upload_result)
        print(self.ping_result)


if __name__ == "__main__":
    speed_test_gui = Speed_Test_Gui()
    speed_test_gui.mainloop()