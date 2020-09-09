import tkinter as tk
# from subprocess import call
from scraper import scraper
from scraper import settings

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Scrape Away!\n(click me)"
        self.hi_there["command"] = self.init_scrape
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def init_scrape(self):
        settings.init()
        x = scraper.main()
        print(x)
        # call(["python", "scraper/scraper.py"])



root = tk.Tk()
app = Application(master=root)
app.mainloop()