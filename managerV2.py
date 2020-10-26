import tkinter as tk
import csv
from tkinter import messagebox
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from data_contracts.scan_result import ScanResult
from data_contracts.fb_user import FBUser
from scraper.modes import Scrape_mode, Mode, Scan_type
from scraper import scraper
from scraper import settings
from functools import partial
from analyzer import Analyzer


def scrape_and_analyze(email, password, user_url, mod, scrape_mod, scan_type):
    scan_results = []

    users_to_analyze = scraper.main(email, password, user_url, mod, scrape_mod, scan_type)
    for fb_user in users_to_analyze:
        user_result = Analyzer.analyze_user(fb_user)
        scan_results.append(user_result)

    # sort users result according to dangerous level
    scan_results.sort(reverse=True, key=calculate_analyzes_sum)  # sort descending, according to sum of analyzes

    # write results to file
    write_results_to_file(scan_results)

    return scan_results

def calculate_analyzes_sum(scan_result):
    offensive = scan_result.offensiveness_result.numeric
    fakeNews = scan_result.offensiveness_result.numeric
    trigers = scan_result.trigers_result.numeric
    utv = scan_result.utv_result.numeric

    # calculate utv as: 1-utv (take the unreliable part)
    return offensive + fakeNews + trigers + (1-utv)

def write_results_to_file(scan_results):
    if len(scan_results)==1:
        write_specific_user_result_to_file(scan_results[0])
    else:
        write_all_friends_result_to_file(scan_results)
    return


def write_specific_user_result_to_file(scan_result):
    offensive = scan_result.offensiveness_result
    fakeNews = scan_result.offensiveness_result
    trigers = scan_result.trigers_result
    utv = scan_result.utv_result

    with open('scan_result.csv', mode='w') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # headline
        result_writer.writerow(["Analysis Name", "Percentage Result", "Description"])

        # write results as rows
        result_writer.writerow(["Offensiveness Analysis", offensive.percent, offensive.text])
    return


def write_all_friends_result_to_file(scan_results):
    with open('scan_result.csv', mode='w') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # headline
        # result_writer.writerow([])

        # write results as rows
        for scan_result in scan_results:
            result_writer.writerow(scan_result)
    return


        
            


