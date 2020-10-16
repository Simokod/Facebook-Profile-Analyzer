import tkinter as tk
from tkinter import messagebox
# from subprocess import call
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from data_contracts.scan_result import ScanResult
from data_contracts.fb_user import FBUser
from modes import Scrape_mode, Mode
from scraper import scraper
from scraper import settings
from functools import partial
from analyzer import Analyzer


def scrape_and_analyze(email, password, user_url, mod, scrape_mod):
    scan_result = []
    users_to_analyze = scraper.main(email, password, user_url, mod, scrape_mod)
    for fb_user in users_to_analyze:
        user_result = Analyzer.analyze_user(fb_user)
        scan_result.append(user_result)

    return scan_result

# gets facebook user object, performs all analysis, and returns results as ScanResult object
def analyze_user(fb_user):
    posts = fb_user.posts
    name = fb_user.name
    print(name)
    # if posts==[]:
    #     # text message for none posts profile
    #     text = "This user Doesn't have any posts, hence does not have "
    #     result = ScanResult(name, text+"offensiveness result", text+"potential fake news result", text+"triggers result", utv_result)
    #     return result
    # else:
        # perform all analyses
<<<<<<< HEAD
        offensiveness_result = OffensivenessAnalysis.analyze_profile_offensiveness(posts)
        potentialFakeNews_result = PotentialFakeNewsAnalysis.analyze_profile_potential_fake_news(posts)
        subjects_result = SubjectsAnalysis.analyze_profile_subjects(posts)
        utv_result = UTVAnalysis.analyze_UTV(profile.age, profile.friendship_duration,
=======
    offensiveness_result = OffensivenessAnalysis.analyze_profile_offensiveness(posts)
    potentialFakeNews_result = PotentialFakeNewsAnalysis.analyze_profile_potential_fake_news(posts)
    subjects_result = SubjectsAnalysis.analyze_profile_subjects(posts)
    utv_result = UTVAnalysis.analyze_UTV(profile.age, profile.friendship_duration,
>>>>>>> 551aa351abbcd88fe7ce48f87e2bb26d4c764486
                                    profile.total_friends, profile.mutual_friends)

    return ScanResult(name, offensiveness_result, potentialFakeNews_result, subjects_result, utv_result)