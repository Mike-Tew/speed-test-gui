from speedtest import Speedtest
from tkinter import Tk, LabelFrame, Button, Label, Checkbutton, IntVar


class Speed_Test_Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Test")
        self.geometry(f"+500+300")
        self.download_var = IntVar(value=1)
        self.upload_var = IntVar(value=1)
        self.ping_var = IntVar(value=1)

        self.test_frame = LabelFrame(self, text="Select Tests")
        self.test_frame.grid(row=0, column=0, padx=20, pady=10, ipadx=10, ipady=10)
        self.download_checkbox = Checkbutton(
            self.test_frame, text="Download Test", variable=self.download_var
        )
        self.download_checkbox.grid(row=0, column=0, sticky="w", padx=20, pady=[10, 0])
        self.upload_checkbox = Checkbutton(
            self.test_frame, text="Upload Test", variable=self.upload_var
        )
        self.upload_checkbox.grid(row=1, column=0, sticky="w", padx=20)
        self.ping_checkbox = Checkbutton(
            self.test_frame, text="Ping Test", variable=self.ping_var
        )
        self.ping_checkbox.grid(row=2, column=0, sticky="w", padx=20)
        self.test_button = Button(
            self.test_frame,
            width=15,
            height=2,
            text="Run Tests",
            font=("Helvetica 10 bold"),
            command=self.run_speed_test,
        )
        self.test_button.grid(row=1, column=1, padx=[40, 20])

        self.results_frame = LabelFrame(self, text="Results")
        self.results_frame.grid(row=1, column=0)
        self.download_label = Label(
            self.results_frame, text="Download", font=("Times 14 bold")
        )
        self.download_label.grid(row=0, column=0, padx=20)
        self.upload_label = Label(
            self.results_frame, text="Upload", font=("Times 14 bold")
        )
        self.upload_label.grid(row=0, column=1, padx=20)
        self.ping_label = Label(
            self.results_frame, text="Ping", font=("Times 14 bold")
        )
        self.ping_label.grid(row=0, column=2, padx=20)

    def update_results_label(self, test_name, result):
        formatted_result = f"{test_name}: {result / 1024 / 1024:.2f} Mbit/s"
        print(f"{formatted_result}")

    def download_test(self):
        print("Running Download Test...")
        download_result = self.test.download()
        self.update_results_label("download", download_result)

    def upload_test(self):
        print("Running Upload Test...")
        upload_result = self.test.upload()

    def run_speed_test(self):
        self.test = Speedtest()
        print("Running test...")
        print("Loading Server List...")
        self.test.get_servers()
        print("Choosing best server...")
        self.best_server = self.test.get_best_server()
        print(
            f"Server: {self.best_server['name']} located in {self.best_server['country']}"
        )

        if self.download_var.get() == 1:
            self.download_test()

        if self.upload_var.get() == 1:
            self.upload_test()

        if self.ping_var.get() == 1:
            print("Ping test")
            ping = self.test.results.ping
            formatted_ping_results = f"Ping: {ping:.0f} ms"
            print(f"Ping: {ping:.0f} ms")


if __name__ == "__main__":
    speed_test_gui = Speed_Test_Gui()
    speed_test_gui.mainloop()
