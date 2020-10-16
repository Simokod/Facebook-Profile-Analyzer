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