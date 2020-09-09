import tkinter as tk
# from subprocess import call
from scraper import scraper
from scraper import settings
from text_analyzer import SimpleSentimentAnalysis

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.analyze = tk.Button(self)
        self.analyze["text"] = "Analyze Profile\n(click me)"
        self.analyze["command"] = self.init_scrape
        self.analyze.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def init_scrape(self):
        settings.init()
        posts = scraper.main().values()
        for post in posts:
            SimpleSentimentAnalysis.analyze_post(post)
        # print(x)
        # call(["python", "scraper/scraper.py"])



root = tk.Tk()
app = Application(master=root)
app.mainloop()