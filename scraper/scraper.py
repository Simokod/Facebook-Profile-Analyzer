import json
import os
import sys
import urllib.request
from datetime import date

import yaml
# import utils
import argparse
import time

import fb_user
from . import settings
from . import utils
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# def get_facebook_images_url(img_links):
#     urls = []

#     for link in img_links:
#         if link != "None":
#             valid_url_found = False
#             driver.get(link)

#             try:
#                 while not valid_url_found:
#                     WebDriverWait(driver, 30).until(
#                         EC.presence_of_element_located(
#                             (By.CLASS_NAME, selectors.get("spotlight"))
#                         )
#                     )
#                     element = driver.find_element_by_class_name(
#                         selectors.get("spotlight")
#                     )
#                     img_url = element.get_attribute("src")

#                     if img_url.find(".gif") == -1:
#                         valid_url_found = True
#                         urls.append(img_url)
#             except Exception:
#                 urls.append("None")
#         else:
#             urls.append("None")

#     return urls


# -------------------------------------------------------------
# -------------------------------------------------------------

# takes a url and downloads image from that url
# def image_downloader(img_links, folder_name):
#     """
#     Download images from a list of image urls.
#     :param img_links:
#     :param folder_name:
#     :return: list of image names downloaded
#     """
#     img_names = []

#     try:
#         parent = os.getcwd()
#         try:
#             folder = os.path.join(os.getcwd(), folder_name)
#             utils.create_folder(folder)
#             os.chdir(folder)
#         except Exception:
#             print("Error in changing directory.")

#         for link in img_links:
#             img_name = "None"

#             if link != "None":
#                 img_name = (link.split(".jpg")[0]).split("/")[-1] + ".jpg"

#                 # this is the image id when there's no profile pic
#                 if img_name == selectors.get("default_image"):
#                     img_name = "None"
#                 else:
#                     try:
#                         urllib.request.urlretrieve(link, img_name)
#                     except Exception:
#                         img_name = "None"

#             img_names.append(img_name)

#         os.chdir(parent)
#     except Exception:
#         print("Exception (image_downloader):", sys.exc_info()[0])
#     return img_names


# -------------------------------------------------------------
# -------------------------------------------------------------


# def extract_and_write_posts(elements, filename):
#     try:
#         f = open(filename, "w", newline="\r\n", encoding="utf-8")
#         f.writelines(
#             " TIME || TYPE  || TITLE || STATUS  ||   LINKS(Shared Posts/Shared Links etc) || POST_ID "
#             + "\n"
#             + "\n"
#         )
#         i = 0
#         for x in elements:
#             try:
#                 link = ""
#                 post_id = utils.my_get_post_id(x)
#                 if post_id != None:
#                     print("id:", post_id)
#                 if post_id != None:
#                     status = utils.my_get_status(x)
#                     line = (
#                         str(post_id)
#                         + " || "
#                         + str(status)
#                         + "\n\n"
#                     )
#                     try:
#                         f.writelines(line)
#                     except Exception:
#                         print("Posts: Could not map encoded characters")
#             except Exception:
#                 print("passing")
#                 pass
#         f.close()
#     except ValueError:
#         print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
#     except Exception:
#         print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
#     return


# def get_status_and_title(link, x):
#     # title
#     title = utils.get_title(x, selectors)
#     if title.text.find("shared a memory") != -1:
#         x = x.find_element_by_xpath(selectors.get("title_element"))
#         title = utils.get_title(x, selectors)
#     status = utils.get_status(x, selectors)
#     if title.text == driver.find_element_by_id(selectors.get("title_text")).text:
#         if status == "":
#             temp = utils.get_div_links(x, "img", selectors)
#             if temp == "":  # no image tag which means . it is not a life event
#                 link = utils.get_div_links(x, "a", selectors).get_attribute("href")
#                 post_type = "status update without text"
#             else:
#                 post_type = "life event"
#                 link = utils.get_div_links(x, "a", selectors).get_attribute("href")
#                 status = utils.get_div_links(x, "a", selectors).text
#         else:
#             post_type = "status update"
#             if utils.get_div_links(x, "a", selectors) != "":
#                 link = utils.get_div_links(x, "a", selectors).get_attribute("href")

#     elif title.text.find(" shared ") != -1:
#         x1, link = utils.get_title_links(title)
#         post_type = "shared " + x1
#     elif title.text.find(" at ") != -1 or title.text.find(" in ") != -1:
#         if title.text.find(" at ") != -1:
#             x1, link = utils.get_title_links(title)
#             post_type = "check in"
#         elif title.text.find(" in ") != 1:
#             status = utils.get_div_links(x, "a", selectors).text
#     elif title.text.find(" added ") != -1 and title.text.find("photo") != -1:
#         post_type = "added photo"
#         link = utils.get_div_links(x, "a", selectors).get_attribute("href")

#     elif title.text.find(" added ") != -1 and title.text.find("video") != -1:
#         post_type = "added video"
#         link = utils.get_div_links(x, "a", selectors).get_attribute("href")

#     else:
#         post_type = "others"
#     if not isinstance(title, str):
#         title = title.text
#     status = status.replace("\n", " ")
#     title = title.replace("\n", " ")
#     return link, status, title, post_type


# def extract_and_write_group_posts(elements, filename):
#     try:
#         f = create_post_file(filename)
#         ids = []
#         for x in elements:
#             try:
#                 # id
#                 post_id = utils.get_group_post_id(x)
#                 ids.append(post_id)
#             except Exception:
#                 pass
#         total = len(ids)
#         i = 0
#         for post_id in ids:
#             i += 1
#             try:
#                 add_group_post_to_file(f, filename, post_id, i, total, reload=True)
#             except ValueError:
#                 pass
#         f.close()
#     except ValueError:
#         print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
#     except Exception:
#         print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
#     return


def add_group_post_to_file(f, filename, post_id, number=1, total=1, reload=False):
    # print("Scraping Post(" + post_id + "). " + str(number) + " of " + str(total))
    # photos_dir = os.path.dirname(filename)
    # if reload:
    #     driver.get(utils.create_post_link(post_id, selectors))
    # line = get_group_post_as_line(post_id, photos_dir)
    # try:
    #     f.writelines(line)
    # except Exception:
    #     print("Posts: Could not map encoded characters")
    print("ERROR -- add_group_post_to_file - not supposed to get here")


def create_post_file(filename):
    # """
    # Creates post file and header
    # :param filename:
    # :return: file
    # """
    # f = open(filename, "w", newline="\r\n", encoding="utf-8")
    # f.writelines(
    #     "TIME || TYPE  || TITLE || STATUS || LINKS(Shared Posts/Shared Links etc) || POST_ID || "
    #     "PHOTO || COMMENTS " + "\n"
    # )
    # return f
    print("ERROR -- create_post_file - not supposed to get here")


# -------------------------------------------------------------
# -------------------------------------------------------------


# def save_to_file(name, elements, status, current_section):
#     """helper function used to save links to files"""

#     # status 0 = dealing with friends list
#     # status 1 = dealing with photos
#     # status 2 = dealing with videos
#     # status 3 = dealing with about section
#     # status 4 = dealing with posts
#     # status 5 = dealing with group posts

#     try:
#         f = None  # file pointer

#         if status != 4 and status != 5:
#             f = open(name, "w", encoding="utf-8", newline="\r\n")

#         results = []
#         img_names = []

#         # dealing with Friends
#         if status == 0:
#             # get profile links of friends
#             results = [x.get_attribute("href") for x in elements]
#             results = [create_original_link(x) for x in results]

#             # get names of friends
#             people_names = [
#                 x.find_element_by_tag_name("img").get_attribute("aria-label")
#                 for x in elements
#             ]

#             # download friends' photos
#             try:
#                 if download_friends_photos:
#                     if friends_small_size:
#                         img_links = [
#                             x.find_element_by_css_selector("img").get_attribute("src")
#                             for x in elements
#                         ]
#                     else:
#                         links = []
#                         for friend in results:
#                             try:
#                                 driver.get(friend)
#                                 WebDriverWait(driver, 30).until(
#                                     EC.presence_of_element_located(
#                                         (
#                                             By.CLASS_NAME,
#                                             selectors.get("profilePicThumb"),
#                                         )
#                                     )
#                                 )
#                                 l = driver.find_element_by_class_name(
#                                     selectors.get("profilePicThumb")
#                                 ).get_attribute("href")
#                             except Exception:
#                                 l = "None"

#                             links.append(l)

#                         for i, _ in enumerate(links):
#                             if links[i] is None:
#                                 links[i] = "None"
#                             elif links[i].find("picture/view") != -1:
#                                 links[i] = "None"

#                         img_links = get_facebook_images_url(links)

#                     folder_names = [
#                         "Friend's Photos",
#                         "Mutual Friends' Photos",
#                         "Following's Photos",
#                         "Follower's Photos",
#                         "Work Friends Photos",
#                         "College Friends Photos",
#                         "Current City Friends Photos",
#                         "Hometown Friends Photos",
#                     ]
#                     print("Downloading " + folder_names[current_section])

#                     img_names = image_downloader(
#                         img_links, folder_names[current_section]
#                     )
#                 else:
#                     img_names = ["None"] * len(results)
#             except Exception:
#                 print(
#                     "Exception (Images)",
#                     str(status),
#                     "Status =",
#                     current_section,
#                     sys.exc_info()[0],
#                 )

#         # dealing with Photos
#         elif status == 1:
#             results = [x.get_attribute("href") for x in elements]
#             results.pop(0)

#             try:
#                 if download_uploaded_photos:
#                     if photos_small_size:
#                         background_img_links = driver.find_elements_by_xpath(
#                             selectors.get("background_img_links")
#                         )
#                         background_img_links = [
#                             x.get_attribute("style") for x in background_img_links
#                         ]
#                         background_img_links = [
#                             ((x.split("(")[1]).split(")")[0]).strip('"')
#                             for x in background_img_links
#                         ]
#                     else:
#                         background_img_links = get_facebook_images_url(results)

#                     folder_names = ["Uploaded Photos", "Tagged Photos"]
#                     print("Downloading " + folder_names[current_section])

#                     img_names = image_downloader(
#                         background_img_links, folder_names[current_section]
#                     )
#                 else:
#                     img_names = ["None"] * len(results)
#             except Exception:
#                 print(
#                     "Exception (Images)",
#                     str(status),
#                     "Status =",
#                     current_section,
#                     sys.exc_info()[0],
#                 )

#         # dealing with Videos
#         elif status == 2:
#             results = elements[0].find_elements_by_css_selector("li")
#             results = [
#                 x.find_element_by_css_selector("a").get_attribute("href")
#                 for x in results
#             ]

#             try:
#                 if results[0][0] == "/":
#                     results = [r.pop(0) for r in results]
#                     results = [(selectors.get("fb_link") + x) for x in results]
#             except Exception:
#                 pass

#         # dealing with About Section
#         elif status == 3:
#             results = elements[0].text
#             f.writelines(results)

#         # dealing with Posts
#         elif status == 4:
#             extract_and_write_posts(elements, name)
#             return

#         # dealing with Group Posts
#         elif status == 5:
#             extract_and_write_group_posts(elements, name)
#             return

#         """Write results to file"""
#         if status == 0:
#             for i, _ in enumerate(results):
#                 # friend's profile link
#                 f.writelines(results[i])
#                 f.write(",")

#                 # friend's name
#                 f.writelines(people_names[i])
#                 f.write(",")

#                 # friend's downloaded picture id
#                 f.writelines(img_names[i])
#                 f.write("\n")

#         elif status == 1:
#             for i, _ in enumerate(results):
#                 # image's link
#                 f.writelines(results[i])
#                 f.write(",")

#                 # downloaded picture id
#                 f.writelines(img_names[i])
#                 f.write("\n")

#         elif status == 2:
#             for x in results:
#                 f.writelines(x + "\n")

#         f.close()

#     except Exception:
#         print("Exception (save_to_file)", "Status =", str(status), sys.exc_info()[0])

#     return


# ----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# returns a dictionary containing the user's posts
def scrape_posts(url, scan_list, section, elements_path):
    # page = []
    # page.append(url)
    # page += [url + s for s in section]
    try:
        # settings.driver.get(page[0])
        print("scrape_posts")
        settings.driver.get(url)
        # time.sleep(3)
        print("after waiting")

        # my_posts = {key: post_id, value: actual post}
        my_posts = utils.my_scroll(settings.number_of_posts, settings.driver, settings.selectors, settings.scroll_time, elements_path[0])

    except Exception:
        print(
            "Exception (scrape_data)",
            "Status =",
            # str(save_status),
            sys.exc_info()[0],
        )
        return
    return my_posts
# returns total number of friends, and number of mutual friends


# returns total number of friends, and number of mutual friends
def parse_friends_data(friends_data):
    friends_data = friends_data.replace(',', '')
    print(friends_data)
    friends_data = friends_data.replace('(', ' ')
    # print(friends_data)
    # friends_data = friends_data.replace(')', ' ')
    friends_data = [int(s) for s in friends_data.split() if s.isdigit()]
    print(friends_data)
    return friends_data


# returns user's friends total friends count and mutual friends count
# def scrape_friends_count(url, scan_list, section, elements_path):
def scrape_friends_count():
    try:
        settings.driver.execute_script(settings.selectors.get("scroll_script"))

        settings.driver.implicitly_wait(5)
        time.sleep(0.5)
        friends_element = settings.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/span/span')
        element_text = friends_element.text

    except Exception:
        print("find_element FAILED")
    return parse_friends_data(element_text)


def month_switch(argument):
    switcher = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return switcher.get(argument, "Invalid month")

def calculate_age(profile_date, today):
    today_day, today_month, today_year = today.split('/')
    today_day = int(today_day)
    today_month = int(today_month)
    today_year = int(today_year)
    # print('day: ', today_day, '\nmonth: ', today_month, '\nyear: ', today_year)
    profile_day, profile_month, profile_year = profile_date.split(' ')
    profile_month = month_switch(profile_month)
    profile_day = int(profile_day)
    profile_month = int(profile_month)
    profile_year = int(profile_year)
    # print('\nday: ', profile_day, '\nmonth: ', profile_month, '\nyear: ', profile_year)
    age = today_year-profile_year + (today_month-profile_month)/12 + (today_day-profile_day)/365
    return age


def scrape_account_age(url):

    try:
        settings.driver.implicitly_wait(5)
        time.sleep(1)
        # photos_link = settings.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a[4]')
        photos_link = settings.driver.find_element_by_partial_link_text('Photos')
        photos_link.click()
        time.sleep(1)
        albums = settings.driver.find_element_by_partial_link_text('Albums')
        time.sleep(0.5)
        albums.click()
        time.sleep(0.5)
        profile_pictures_link = settings.driver.find_element_by_partial_link_text('Profile pictures')
        time.sleep(0.5)
        profile_pictures_link.click()
        time.sleep(5)
        profile_pictures = settings.driver.find_elements_by_css_selector('.g6srhlxm.gq8dxoea.bi6gxh9e.oi9244e8.l9j0dhe7')
        last_pic = profile_pictures[len(profile_pictures)-1]
        time.sleep(0.5)
        last_pic.click()
        date_element = settings.driver.find_element_by_css_selector('.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw')
        time.sleep(0.5)
        profile_date = date_element.get_attribute('aria-label')
        # print('profile date: ', profile_date)
        today = date.today().strftime("%d/%m/%Y")
        # print('today date: ', today)
        age = calculate_age(profile_date, today)
        settings.driver.get(url)
        time.sleep(0.5)
        return age
    except Exception:
        print("find_element FAILED")

def calculate_duration(friendship_year, friendship_month, today):
    today_day, today_month, today_year = today.split('/')
    today_day = int(today_day)
    today_month = int(today_month)
    today_year = int(today_year)
    # print('day: ', today_day, '\nmonth: ', today_month, '\nyear: ', today_year)
    # profile_day, profile_month, profile_year = profile_date.split(' ')
    friendship_month = month_switch(friendship_month)
    # profile_day = int(profile_day)
    friendship_month = int(friendship_month)
    friendship_year = int(friendship_year)
    # print('\nday: ', profile_day, '\nmonth: ', profile_month, '\nyear: ', profile_year)
    duration = today_year-friendship_year + (today_month-friendship_month)/12 + today_day/365
    return duration

def find_duration(url):
    try:
        more_button = settings.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[4]/div')
        time.sleep(0.5)
        more_button.click()
        time.sleep(0.5)

        friendship = settings.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/a')
        # friendship = settings.driver.find_element_by_partial_link_text('See friendship')
        friendship.click()
        time.sleep(2)
        duration = settings.driver.find_elements_by_css_selector('.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.rrkovp55.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.iv3no6db.jq4qci2q.a3bd9o3v.knj5qynh.oo9gr5id.hzawbc8m')[1]
        # print(duration)
        time.sleep(1)
        duration = duration.text
        # print(duration)
        duration = duration.split(" ")
        # print(duration)
        year = int(duration[len(duration)-1])
        month = duration[len(duration)-2]
        today = date.today().strftime("%d/%m/%Y")
        duration = calculate_duration(year, month, today)
        # print(duration)
        settings.driver.get(url)
        time.sleep(1)
        return duration
    except Exception:
        print("find_element FAILED")
        settings.driver.get(url)
        time.sleep(0.5)


def scrape_data(url, scan_list, section, elements_path, save_status):
    """Given some parameters, this function can scrap friends/photos/videos/about/posts(statuses) of a profile"""
    friendship_duration = find_duration(url)
    time.sleep(0.5)
    age = scrape_account_age(url)
    time.sleep(0.5)
    friends_data = scrape_friends_count()
    total_friends = friends_data[0]
    if len(friends_data) > 1:
        mutual_friends = friends_data[1]
    else:
        mutual_friends = 0
    print('total friends: ', total_friends, '\n'
                                            'mutual friends: ', mutual_friends)
    posts = scrape_posts(url, scan_list, section, elements_path)
    # elif save_status == 0:
    #     pass

    # elif save_status == 3:
    #     pass
    #     # about = scrape_about(url, scan_list, section, elements_path)
    # else:
    #     print("what the cat")
    profile = fb_user.FBUser(url, age, friendship_duration, total_friends, mutual_friends, posts)
    print('url: ', profile.url, '\nage: ', profile.age,
          '\nfriendship_duration: ', profile.friendship_duration,
          '\ntotal_friends: ', profile.total_friends,
          '\nmutual_friends: ', profile.mutual_friends)

    return profile


# return posts, friends, about

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def create_original_link(url):
    if url.find(".php") != -1:
        original_link = (
            settings.facebook_https_prefix + settings.facebook_link_body + ((url.split("="))[1])
        )

        if original_link.find("&") != -1:
            original_link = original_link.split("&")[0]

    elif url.find("fnr_t") != -1:
        original_link = (
            settings.facebook_https_prefix
            + settings.facebook_link_body
            + ((url.split("/"))[-1].split("?")[0])
        )
    elif url.find("_tab") != -1:
        original_link = (
            settings.facebook_https_prefix
            + settings.facebook_link_body
            + (url.split("?")[0]).split("/")[-1]
        )
    else:
        original_link = url

    return original_link

def scrap_all_friends():
    result = []
    # profile = settings.driver.find_element_by_xpath('./div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span')
    settings.driver.find_element_by_css_selector('.gs1a9yip.ow4ym5g4.auili1gw.rq0escxv.j83agx80.cbu4d94t.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.tgvbjcpo.hpfvmrgz.rz4wbd8a.a8nywdso.l9j0dhe7.du4w35lb.rj1gh0hx.pybr56ya.f10w8fjw').click()
    time.sleep(0.5)
    url = settings.driver.current_url
    settings.driver.get(url+"/friends")
    time.sleep(0.5)

    friends_count = scrape_friends_count()
    print(friends_count)
    utils.friends_scroll(settings.driver, settings.selectors, settings.scroll_time)
    friends_block = settings.driver.find_element_by_css_selector('.dati1w0a.ihqw7lf3.hv4rvrfc.discj3wi')
    friends = friends_block.find_elements_by_css_selector('.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.q9uorilb.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.wkznzc2l.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l.pioscnbf.etr7akla')

    links = [friend.get_attribute('href') for friend in friends]

    print(links, "\n", len(links))
    list = []
    count = 0           # DEBUG: control num of iterations
    for link in links:
        count += 1
        settings.driver.get(link)
        list.append(scrap_profile())

        # DEBUG: control num of iterations
        if count >= 5:
            break
    return list

def scrap_profile():
    data_folder = os.path.join(os.getcwd(), "data")
    utils.create_folder(data_folder)
    os.chdir(data_folder)

    # execute for all profiles given in input.txt file
    url = settings.driver.current_url
    user_id = create_original_link(url)

    print("\nScraping:", user_id)

    try:
        target_dir = os.path.join(data_folder, user_id.split("/")[-1])
        utils.create_folder(target_dir)
        os.chdir(target_dir)
    except Exception:
        print("Some error occurred in creating the profile directory.")
        os.chdir("../..")
        return

    # to_scrap = ["Friends", "Photos", "Videos", "About", "Posts"]
    to_scrap = ["Posts"]
    for item in to_scrap:
        print("----------------------------------------")
        print("Scraping {}..".format(item))

        if item == "Posts":
            scan_list = [None]
        elif item == "About":
            scan_list = [None] * 7
        else:
            scan_list = settings.params[item]["scan_list"]

        section = settings.params[item]["section"]
        elements_path = settings.params[item]["elements_path"]
        save_status = settings.params[item]["save_status"]
        profile = scrape_data(user_id, scan_list, section, elements_path, save_status)

        print("{} Done!".format(item))

    print("Finished Scraping Profile " + str(user_id) + ".")
    os.chdir("../..")

    return profile


# def get_comments():
#     comments = []
#     try:
#         data = driver.find_element_by_xpath(selectors.get("comment_section"))
#         reply_links = driver.find_elements_by_xpath(
#             selectors.get("more_comment_replies")
#         )
#         for link in reply_links:
#             try:
#                 driver.execute_script("arguments[0].click();", link)
#             except Exception:
#                 pass
#         see_more_links = driver.find_elements_by_xpath(
#             selectors.get("comment_see_more_link")
#         )
#         for link in see_more_links:
#             try:
#                 driver.execute_script("arguments[0].click();", link)
#             except Exception:
#                 pass
#         data = data.find_elements_by_xpath(selectors.get("comment"))
#         for d in data:
#             try:
#                 author = d.find_element_by_xpath(selectors.get("comment_author")).text
#                 text = d.find_element_by_xpath(selectors.get("comment_text")).text
#                 replies = utils.get_replies(d, selectors)
#                 comments.append([author, text, replies])
#             except Exception:
#                 pass
#     except Exception:
#         pass
#     return comments


# def get_group_post_as_line(post_id, photos_dir):
#     try:
#         data = driver.find_element_by_xpath(selectors.get("single_post"))
#         time = utils.get_time(data)
#         title = utils.get_title(data, selectors).text
#         # link, status, title, type = get_status_and_title(title,data)
#         link = utils.get_div_links(data, "a", selectors)
#         if link != "":
#             link = link.get_attribute("href")
#         post_type = ""
#         status = '"' + utils.get_status(data, selectors).replace("\r\n", " ") + '"'
#         photos = utils.get_post_photos_links(data, selectors, photos_small_size)
#         comments = get_comments()
#         photos = image_downloader(photos, photos_dir)
#         line = (
#             str(time)
#             + "||"
#             + str(post_type)
#             + "||"
#             + str(title)
#             + "||"
#             + str(status)
#             + "||"
#             + str(link)
#             + "||"
#             + str(post_id)
#             + "||"
#             + str(photos)
#             + "||"
#             + str(comments)
#             + "\n"
#         )
#         return line
#     except Exception:
#         return ""


def create_folders():
    """
    Creates folder for saving data (profile, post or group) according to current driver url
    Changes current dir to target_dir
    :return: target_dir or None in case of failure
    """
    folder = os.path.join(os.getcwd(), "data")
    utils.create_folder(folder)
    os.chdir(folder)
    try:
        item_id = get_item_id(driver.current_url)
        target_dir = os.path.join(folder, item_id)
        utils.create_folder(target_dir)
        os.chdir(target_dir)
        return target_dir
    except Exception:
        print("Some error occurred in creating the group directory.")
        os.chdir("../..")
        return None


def get_item_id(url):
    """
    Gets item id from url
    :param url: facebook url string
    :return: item id or empty string in case of failure
    """
    ret = ""
    try:
        link = create_original_link(url)
        ret = link.split("/")[-1]
        if ret.strip() == "":
            ret = link.split("/")[-2]
    except Exception as e:
        print("Failed to get id: " + format(e))
    return ret


def scrape_group(url):
    # if create_folders() is None:
    #     return
    # group_id = get_item_id(url)
    # # execute for all profiles given in input.txt file
    # print("\nScraping:", group_id)

    # to_scrap = ["GroupPosts"]  # , "Photos", "Videos", "About"]
    # for item in to_scrap:
    #     print("----------------------------------------")
    #     print("Scraping {}..".format(item))

    #     if item == "GroupPosts":
    #         scan_list = [None]
    #     elif item == "About":
    #         scan_list = [None] * 7
    #     else:
    #         scan_list = params[item]["scan_list"]

    #     section = params[item]["section"]
    #     elements_path = params[item]["elements_path"]
    #     file_names = params[item]["file_names"]
    #     save_status = params[item]["save_status"]

    #     scrape_data(url, scan_list, section, elements_path, save_status, file_names)

    #     print("{} Done!".format(item))

    # print("Finished Scraping Group " + str(group_id) + ".")
    # os.chdir("../..")
    print("Error -- scrape_group - not supposed to get here")


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def login(email, password):
    """ Logging into our own profile """

    try:


        options = Options()

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        # options.add_argument("headless")

        try:
            settings.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(), options=options
            )
        except Exception:
            print("Error loading chrome webdriver " + sys.exc_info()[0])
            exit(1)

        fb_path = settings.facebook_https_prefix + settings.facebook_link_body
        settings.driver.get(fb_path)
        settings.driver.maximize_window()

        # filling the form
        settings.driver.find_element_by_name("email").send_keys(email)
        settings.driver.find_element_by_name("pass").send_keys(password)

        try:
            # clicking on login button
            settings.driver.find_element_by_id("loginbutton").click()
        except NoSuchElementException:
            # Facebook new design
            settings.driver.find_element_by_name("login").click()

        # if your account uses multi factor authentication
        mfa_code_input = utils.safe_find_element_by_id(settings.driver, "approvals_code")

        if mfa_code_input is None:
            return

        mfa_code_input.send_keys(input("Enter MFA code: "))
        settings.driver.find_element_by_id("checkpointSubmitButton").click()

        # there are so many screens asking you to verify things. Just skip them all
        while (
            utils.safe_find_element_by_id(settings.driver, "checkpointSubmitButton") is not None
        ):
            dont_save_browser_radio = utils.safe_find_element_by_id(settings.driver, "u_0_3")
            if dont_save_browser_radio is not None:
                dont_save_browser_radio.click()

            settings.driver.find_element_by_id("checkpointSubmitButton").click()

    except Exception:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit(1)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def scraper(email, password, mod, scrape_mod, **kwargs):
    print(scrape_mod)
    if mod == 0:
        working_dir = os.path.dirname(os.path.abspath(__file__))
        with open(working_dir + "\credentials.yaml", "r") as ymlfile:
            cfg = yaml.safe_load(stream=ymlfile)

        if ("password" not in cfg) or ("email" not in cfg):
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit(1)
        email = cfg["email"]
        password = cfg["password"]

    urls = [
        settings.facebook_https_prefix + settings.facebook_link_body + get_item_id(line)
        for line in open(working_dir + "\input.txt", newline="\r\n")
        if not line.lstrip().startswith("#") and not line.strip() == ""
    ]
    login(email, password)
    if scrape_mod == 0:
        url = urls[0]
        settings.driver.get(url)
        result = scrap_profile()
    else:
        settings.selectors
        result = scrap_all_friends()
    settings.driver.close()
    # if len(urls) > 0:
    #     print("\nStarting Scraping...")
    #     login(email, password)
    #     for url in urls:
    #         settings.driver.get(url)
    #         link_type = utils.identify_url(settings.driver.current_url)
    #         if link_type == 0:
    #             result = scrap_profile()
    #         elif link_type == 1:
    #             # scrap_post(url)
    #             pass
    #         elif link_type == 2:
    #             scrape_group(settings.driver.current_url)
    #         elif link_type == 3:
    #             file_name = settings.params["GroupPosts"]["file_names"][0]
    #             item_id = get_item_id(settings.driver.current_url)
    #             if create_folders() is None:
    #                 continue
    #             f = create_post_file(file_name)
    #             add_group_post_to_file(f, file_name, item_id)
    #             f.close()
    #             os.chdir("../..")
    #     settings.driver.close()
    return result
    # else:
    #     print("Input file is empty.")


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

# if __name__ == "__main__":
def main(email, password, mod, scrape_mod):
    # print(email, password)
    settings.ap = argparse.ArgumentParser()
    # PLS CHECK IF HELP CAN BE BETTER / LESS AMBIGUOUS
    settings.ap.add_argument(
        "-dup",
        "--uploaded_photos",
        help="download users' uploaded photos?",
        default=True,
    )
    settings.ap.add_argument(
        "-dfp", 
        "--friends_photos", 
        help="download users' photos?", 
        default=True
    )
    settings.ap.add_argument(
        "-fss",
        "--friends_small_size",
        help="Download friends pictures in small size?",
        default=True,
    )
    settings.ap.add_argument(
        "-pss",
        "--photos_small_size",
        help="Download photos in small size?",
        default=True,
    )
    settings.ap.add_argument(
        "-ts",
        "--total_scrolls",
        help="How many times should I scroll down?",
        default=2500,
    )
    settings.ap.add_argument(
        "-st",
        "--scroll_time", 
        help="How much time should I take to scroll?", 
        default=8
    )
    settings.ap.add_argument(
        "-nop",
        "--number_of_posts",
        help="How many posts should i take?",
        default=10
    )

    settings.args = vars(settings.ap.parse_args())
    print(settings.args)

    # ---------------------------------------------------------
    # Global Variables
    # ---------------------------------------------------------

    # whether to download photos or not
    # download_uploaded_photos = utils.to_bool(args["uploaded_photos"])
    # download_friends_photos = utils.to_bool(args["friends_photos"])
    # download_uploaded_photos = False
    # download_friends_photos = False

    # whether to download the full image or its thumbnail (small size)
    # if small size is True then it will be very quick else if its false then it will open each photo to download it
    # and it will take much more time
    # friends_small_size = utils.to_bool(args["friends_small_size"])
    # photos_small_size = utils.to_bool(args["photos_small_size"])
    # friends_small_size = False
    # photos_small_size = False

    # settings.total_scrolls = int(args["total_scrolls"])
    settings.scroll_time = int(settings.args["scroll_time"])
    settings.number_of_posts = int(settings.args["number_of_posts"])

    # current_scrolls = 0
    # old_height = 0

    settings.driver = None

    working_dir = os.path.dirname(os.path.abspath(__file__))
    with open(working_dir + "\selectors.json") as selectors, open(working_dir + "\params.json") as params:
        settings.selectors = json.load(selectors)
        settings.params = json.load(params)

    # firefox_profile_path = settings.selectors.get("firefox_profile_path")
    settings.facebook_https_prefix = settings.selectors.get("facebook_https_prefix")
    settings.facebook_link_body = settings.selectors.get("facebook_link_body")

    # get things rolling
    scraper_result = scraper(email, password, mod, scrape_mod)
    return scraper_result

