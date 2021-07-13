from speedtest import Speedtest
import threading
from tkinter import Tk, LabelFrame, Button, Label, Checkbutton, IntVar, Listbox, END


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
            self.test_frame,
            text="Download Test",
            font=("Arial 10 bold"),
            variable=self.download_var,
        )
        self.download_checkbox.grid(row=0, column=0, sticky="w", padx=20, pady=[10, 0])
        self.upload_checkbox = Checkbutton(
            self.test_frame,
            text="Upload Test",
            font=("Arial 10 bold"),
            variable=self.upload_var,
        )
        self.upload_checkbox.grid(row=1, column=0, sticky="w", padx=20)
        self.ping_checkbox = Checkbutton(
            self.test_frame,
            text="Ping Test",
            font=("Arial 10 bold"),
            variable=self.ping_var,
        )
        self.ping_checkbox.grid(row=2, column=0, sticky="w", padx=20)
        self.test_button = Button(
            self.test_frame,
            width=10,
            text="Run Tests",
            font=("Arial 14 bold"),
            command=lambda: threading.Thread(target=self.run_speed_test).start(),
        )
        self.test_button.grid(row=1, column=1, padx=[40, 35])

        self.results_frame = LabelFrame(self, text="Results")
        self.results_frame.grid(row=1, column=0, ipady=10)
        self.download_label = Label(
            self.results_frame, text="Download", font=("Courier 18 bold underline")
        )
        self.download_label.grid(row=0, column=0, padx=20, pady=[10, 5])
        self.download_result_label = Label(self.results_frame, font=("Tahoma 12 bold"))
        self.download_result_label.grid(row=1, column=0)
        self.upload_label = Label(
            self.results_frame, text="Upload", font=("Courier 18 bold underline")
        )
        self.upload_label.grid(row=0, column=1, padx=20, pady=[10, 5])
        self.upload_result_label = Label(self.results_frame, font=("Tahoma 12 bold"))
        self.upload_result_label.grid(row=1, column=1)
        self.ping_label = Label(
            self.results_frame, text="Ping", font=("Courier 18 bold underline")
        )
        self.ping_label.grid(row=0, column=2, padx=20, pady=[10, 5])
        self.ping_result_label = Label(self.results_frame, font=("Tahoma 12 bold"))
        self.ping_result_label.grid(row=1, column=2)

        self.status_listbox = Listbox(
            self,
            height=5,
            width=56,
            bg="black",
            fg="green",
            font=("Helvetica 10 bold"),
            selectborderwidth=1,
        )
        self.status_listbox.grid(row=2, column=0, pady=10)

    def download_test(self):
        self.status_listbox.insert(END, "Running Download Test")
        download_result = f"{self.test.download() / 1024 / 1024:.2f} Mbit/s"
        self.download_result_label["text"] = download_result

    def upload_test(self):
        self.status_listbox.insert(END, "Running Upload Test")
        upload_result = f"{self.test.upload() / 1024 / 1024:.2f} Mbit/s"
        self.upload_result_label["text"] = upload_result

    def run_speed_test(self):
        self.test = Speedtest()
        self.status_listbox.insert(END, "Running tests")
        self.status_listbox.insert(END, "Loading Server List")
        self.test.get_servers()
        self.status_listbox.insert(END, "Choosing Best Server")
        self.best_server = self.test.get_best_server()
        self.status_listbox.insert(
            END,
            f"Server: {self.best_server['name']} located in {self.best_server['country']}",
        )

        if self.download_var.get() == 1:
            self.download_test()

        if self.upload_var.get() == 1:
            self.upload_test()

        if self.ping_var.get() == 1:
            ping = self.test.results.ping
            self.ping_result_label["text"] = f"{ping:.0f} ms"


if __name__ == "__main__":
    speed_test_gui = Speed_Test_Gui()
    speed_test_gui.mainloop()
