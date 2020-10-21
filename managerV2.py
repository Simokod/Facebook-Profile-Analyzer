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


def scrape_and_analyze(email, password, user_url, mod, scrape_mod, scan_type):
    scan_results = []

    users_to_analyze = scraper.main(email, password, user_url, mod, scrape_mod, scan_type)
    for fb_user in users_to_analyze:
        print(fb_user.url)
        user_result = Analyzer.analyze_user(fb_user)
        scan_results.append(user_result)

    # sort users result according to dangerous level
    scan_results.sort(reverse=True, key=calculate_analyzes_sum)  # sort descending, according to sum of analyzes
    return scan_results

def calculate_analyzes_sum(scan_result):
    offensive = scan_result.offensiveness_result.numeric
    fakeNews = scan_result.offensiveness_result.numeric
    trigers = scan_result.trigers_result.numeric
    utv = scan_result.utv_result.numeric

    # calculate utv as: 1-utv (take the unreliable part)
    return offensive + fakeNews + trigers + (1-utv)
