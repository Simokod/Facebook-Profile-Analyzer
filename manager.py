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
        self.create_analyze_button()
        self.create_quit_button()

    def create_analyze_button(self):
        self.analyze_button = tk.Button(self)
        self.analyze_button["text"] = "Analyze Profile\n(click me)"
        self.analyze_button["command"] = self.scrape_and_analyze
        self.analyze_button.pack(side="top")
        # self.analyze.grid(row=1, column=1, sticky=tk.W, pady=4)
        return 

    def create_quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        return 

    def example(self):
        self.analyze_result = tk.Label(root, text= "Hello World!")
        self.analyze_result.pack()
        return

    def scrape_and_analyze(self):
        settings.init()
        posts = scraper.main().values()
        for post in posts:
            self.detect_post_subject(post)
            # SimpleSentimentAnalysis.analyze_post(post)
        # print(x)
        # call(["python", "scraper/scraper.py"])
        return 

    def detect_post_subject(self, post):
        post_subject = SimpleSentimentAnalysis.detect_post_subject(post)
        post_subject_text = "The subject of the post is: " + str(post_subject)
        analyze_result = tk.Label(root, text= post_subject_text)
        analyze_result.pack()
        return



root = tk.Tk()
app = Application(master=root)
app.mainloop()