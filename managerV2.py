import tkinter as tk
from tkinter import messagebox
# from subprocess import call
from selenium.common.exceptions import WebDriverException, NoSuchWindowException

from scraper import scraper
from scraper import settings
from functools import partial
from text_analyzer import OffensivenessAnalysis
from text_analyzer import PotentialFakeNewsAnalysis
from text_analyzer import SubjectsAnalysis

def scrape_and_analyze(email, password, mod, scrape_mod):
    print("Got to analyze!")
    if scrape_mod == 0:
        posts = scraper.main(email, password, mod, scrape_mod)
        analyze_profile(posts)

    elif scrape_mod == 1:
        all_friends_posts = scraper.main(email.get(), password.get(), mod.get(), scrape_mod.get())
        for friend in all_friends_posts:
            analyze_profile(friend.values())
    return 

# gets posts of profile. performs all analysis, and render results
def analyze_profile(posts):
    if isinstance(posts, str):
        print(posts)

    else:
        posts = posts.values()
        # perform all analyses
        offensiveness_analysis_result = OffensivenessAnalysis.analyze_profile_offensiveness(posts)
        potentialFakeNews_analysis_result = PotentialFakeNewsAnalysis.analyze_profile_potential_fake_news(posts)
        subjects_analysis_result = SubjectsAnalysis.analyze_profile_subjects(posts)

        print(subjects_analysis_result)