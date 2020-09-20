import tkinter as tk
from tkinter import messagebox
# from subprocess import call
from selenium.common.exceptions import WebDriverException, NoSuchWindowException

from scraper import scraper
from scraper import settings
from functools import partial
from text_analyzer import OffensivenessAnalysis
from text_analyzer import PotentialFakeNewsAnalysis

class Application(tk.Frame):
    # Dev mode selector
    mod = None
    c2 = None
    # Scrape mode selector
    scrape_mod = None
    # s2 = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.create_mode_selector()
        self.create_scrape_selector()
        self.create_analyze_button()
        self.create_quit_button()

    def create_mode_selector(self):
        # mod = tk.IntVar()
        global mod
        global c2
        mod = tk.IntVar()

        c1 = tk.Radiobutton(root, text="Dev_mod", variable=mod, value=0).grid(row=0, column=0, sticky="w")
        c2 = tk.Radiobutton(root, text="Login_mode", variable=mod, value=1).grid(row=1, column=0, sticky="w")

        return

    def create_scrape_selector(self):
        # mod = tk.IntVar()
        global scrape_mod
        # global s2
        scrape_mod = tk.IntVar()

        s1 = tk.Radiobutton(root, text="Analyze specific profile", variable=scrape_mod, value=0).grid(row=0, column=2, sticky="w")
        s2 = tk.Radiobutton(root, text="Analyze all friends", variable=scrape_mod, value=1)\
            .grid(row=1, column=2, sticky="w")

        return

    def create_analyze_button(self):
        global c2
        usernameLabel = tk.Label(root, text="User Name").grid(row=2, column=0, in_=c2)
        username = tk.StringVar()
        usernameEntry = tk.Entry(root, textvariable=username).grid(row=2, column=1, in_=c2)

        # password label and password entry box
        passwordLabel = tk.Label(root, text="Password").grid(row=3, column=0, in_=c2)
        password = tk.StringVar()
        passwordEntry = tk.Entry(root, textvariable=password, show='*').grid(row=3, column=1, in_=c2)
        print(username.get(), password.get())
        scrape_and_analyze = partial(self.scrape_and_analyze, email=username, password=password)

        # login button
        self.analyze_button = tk.Button(root, text="Analyze Profile", command=scrape_and_analyze).grid(row=4, column=0)

        return

    def create_quit_button(self):
        self.quit = tk.Button(root, text="QUIT", fg="red",
                              command=self.master.destroy).grid(row=5, column=0)
        return

    def scrape_and_analyze(self, email, password):
        global mod
        global scrape_mod
        settings.init()

        if scrape_mod.get() == 0:
            posts = scraper.main(email.get(), password.get(), mod.get(), scrape_mod.get()).values()
            self.analyze_profile(posts)

        elif scrape_mod.get() == 1:
            all_friends_posts = scraper.main(email.get(), password.get(), mod.get(), scrape_mod.get())
            for friend in all_friends_posts:
                self.analyze_profile(friend.values())
        return 

    # gets posts of profile. performs all analysis, and render results
    def analyze_profile(self, posts):
        print(posts)
        
        # perform all analyses
        offensiveness_result = OffensivenessAnalysis.analyze_profile_offensiveness(posts)
        potentialFakeNews_result = PotentialFakeNewsAnalysis.analyze_profile_potential_fake_news(posts)

        # render results of analyses
        self.render_result(offensiveness_result)
        self.render_result(potentialFakeNews_result)

    def render_result(self, textResult):
        result_label = tk.Label(root, text=textResult)
        result_label.grid(sticky='s')

root = tk.Tk()
root.geometry('500x250')
root.title("FB profile Analyzer")

app = Application(master=root)
app.mainloop()