import argparse
import os
import sys
from calendar import calendar

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
def to_bool(x):
    if x in ["False", "0", 0, False]:
        return False
    elif x in ["True", "1", 1, True]:
        return True
    else:
        raise argparse.ArgumentTypeError("Boolean value expected")


def create_post_link(post_id, selectors):
    return (
            selectors["facebook_https_prefix"] + selectors["facebook_link_body"] + post_id
    )


# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


# -------------------------------------------------------------
# Helper functions for Page scrolling
# -------------------------------------------------------------
# check if height changed
def check_height(driver, selectors, old_height):
    new_height = driver.execute_script(selectors.get("height_script"))
    return new_height != old_height


# helper function: used to scroll the page
# def scroll(total_scrolls, driver, selectors, scroll_time):
#     global old_height
#     current_scrolls = 0

#     while True:
#         try:
#             if current_scrolls == total_scrolls:
#                 return

#             old_height = driver.execute_script(selectors.get("height_script"))
#             driver.execute_script(selectors.get("scroll_script"))
#             WebDriverWait(driver, scroll_time, 0.05).until(
#                 lambda driver: check_height(driver, selectors, old_height)
#             )
#             current_scrolls += 1


#         except TimeoutException:
#             break
#     return

def my_scroll(number_of_posts, driver, selectors, scroll_time, elements_path):
    global old_height
    filename = "Posts.txt"
    try:
        f = open(filename, "w", newline="\r\n", encoding="utf-8")
        f.writelines(" TIME || TYPE  || TITLE || STATUS  ||   LINKS(Shared Posts/Shared Links etc) || POST_ID\n\n")
        f.close()
    except ValueError:
        print("Exception (my_scroll)", "Status =", sys.exc_info()[0])
    except Exception:
        print("Exception (my_scroll)", "Status =", sys.exc_info()[0])

    posts_scraped = 0
    cur_posts_scraped = 0
    last_post_id = 0
    while posts_scraped < number_of_posts:
        try:
            old_height = driver.execute_script(selectors.get("height_script"))
            driver.execute_script(selectors.get("scroll_script"))
            WebDriverWait(driver, scroll_time, 0.05).until(
                lambda driver: check_height(driver, selectors, old_height)
            )

            data = driver.find_elements_by_xpath(elements_path)
            data = remove_comments(data)
            lim = number_of_posts-posts_scraped

            cur_posts_scraped, last_post_id = my_extract_and_write_posts(data[posts_scraped:], filename, lim, last_post_id)
            posts_scraped += cur_posts_scraped
            
        except TimeoutException:
            break
    return


def remove_comments(data):
    posts = []
    for x in data:
        post_id = -1
        try:
            post_id = x.get_attribute("aria-posinset")
            if post_id != None:
                posts.append(x)
        except Exception:
            pass
    return posts


def my_extract_and_write_posts(elements, filename, lim, last_post_id):
    try:
        f = open(filename, "a", newline="\r\n", encoding="utf-8")
        posts_written = 0
        for x in elements:
            try:
                post_id = my_get_post_id(x)
                int_post_id = int(post_id)
                if post_id != None:
                    if int_post_id > last_post_id:
                        print("post_id:", int_post_id)
                        print("last_id:", last_post_id)
                        status = my_get_status(x)   
                        line = (
                                str(int_post_id)
                                + " || "
                                + str(status)
                                + "\n\n"
                        )
                        try:
                            if str(status) != "":
                                f.writelines(line)
                                posts_written += 1
                                last_post_id = int_post_id
                                if posts_written == lim:
                                    break
                        except Exception:
                            print("Posts: Could not map encoded characters")
            except Exception:
                pass
        f.close()
    except ValueError:
        print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
    except Exception:
        print("Exception (extract_and_write_posts)", "Status =", sys.exc_info()[0])
    return posts_written, last_post_id


# -----------------------------------------------------------------------------
# MyHelper Functions for Posts
# -----------------------------------------------------------------------------

def my_get_status(x):
    status = ""
    statuses = []
    try:
        post = x.find_element_by_xpath('./div/div/div/div/div/div[2]/div/div[3]/div/div/div/div/span')
        try:
            see_more_button = post.find_element_by_css_selector('.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.oo9gr5id.gpro0wi8.lrazzd5p')
            see_more_button.click()
        except NoSuchElementException:
            pass
        statuses = post.find_elements_by_xpath('./*[contains(@class, cxmmr5t8)]/div')
        for item in statuses:
            status += item.text

    except Exception:
        #     try:
        #         status = x.find_element_by_xpath(selectors.get("status_exc")).text
        #     except Exception:
        #         pass
        print("my_get_status exception")
    return status


def my_get_post_id(x):
    post_id = -1
    try:
        post_id = x.get_attribute("aria-posinset")
    except Exception:
        pass
    return post_id


# -----------------------------------------------------------------------------
# Helper Functions for Posts
# -----------------------------------------------------------------------------

def get_status(x, selectors):
    status = ""
    try:
        status = x.find_element_by_xpath(
            selectors.get("status")
        ).text  # use _1xnd for Pages
    except Exception:
        try:
            status = x.find_element_by_xpath(selectors.get("status_exc")).text
        except Exception:
            pass
    return status


def get_post_id(x):
    post_id = -1
    try:
        post_id = x.get_attribute("id")
        post_id = post_id.split(":")[-1]
    except Exception:
        pass
    return post_id


def get_group_post_id(x):
    post_id = -1
    try:
        post_id = x.get_attribute("id")

        post_id = post_id.split("_")[-1]
        if ";" in post_id:
            post_id = post_id.split(";")
            post_id = post_id[2]
        else:
            post_id = post_id.split(":")[0]
    except Exception:
        pass
    return post_id


def get_photo_link(x, selectors, small_photo):
    link = ""
    try:
        if small_photo:
            link = x.find_element_by_xpath(
                selectors.get("post_photo_small")
            ).get_attribute("src")
        else:
            link = x.get_attribute("data-ploi")
    except NoSuchElementException:
        try:
            link = x.find_element_by_xpath(
                selectors.get("post_photo_small_opt1")
            ).get_attribute("src")
        except AttributeError:
            pass
        except Exception:
            print("Exception (get_post_photo_link):", sys.exc_info()[0])
    except Exception:
        print("Exception (get_post_photo_link):", sys.exc_info()[0])
    return link


def get_post_photos_links(x, selectors, small_photo):
    links = []
    photos = safe_find_elements_by_xpath(x, selectors.get("post_photos"))
    if photos is not None:
        for el in photos:
            links.append(get_photo_link(el, selectors, small_photo))
    return links


def get_div_links(x, tag, selectors):
    try:
        temp = x.find_element_by_xpath(selectors.get("temp"))
        return temp.find_element_by_tag_name(tag)
    except Exception:
        return ""


def get_title_links(title):
    l = title.find_elements_by_tag_name("a")
    return l[-1].text, l[-1].get_attribute("href")


def get_title(x, selectors):
    title = ""
    try:
        title = x.find_element_by_xpath(selectors.get("title"))
    except Exception:
        try:
            title = x.find_element_by_xpath(selectors.get("title_exc1"))
        except Exception:
            try:
                title = x.find_element_by_xpath(selectors.get("title_exc2"))
            except Exception:
                pass
    finally:
        return title


def get_time(x):
    time = ""
    try:
        time = x.find_element_by_tag_name("abbr").get_attribute("title")
        time = (
                str("%02d" % int(time.split(", ")[1].split()[1]), )
                + "-"
                + str(
            (
                    "%02d"
                    % (
                        int(
                            (
                                list(calendar.month_abbr).index(
                                    time.split(", ")[1].split()[0][:3]
                                )
                            )
                        ),
                    )
            )
        )
                + "-"
                + time.split()[3]
                + " "
                + str("%02d" % int(time.split()[5].split(":")[0]))
                + ":"
                + str(time.split()[5].split(":")[1])
        )
    except Exception:
        pass

    finally:
        return time


def identify_url(url):
    """
    A possible way to identify the link.
    Not Exhaustive!
    :param url:
    :return:
    0 - Profile
    1 - Profile post
    2 - Group
    3 - Group post
    """
    if "groups" in url:
        if "permalink" in url:
            return 3
        else:
            return 2
    elif "posts" in url:
        return 1
    else:
        return 0


def safe_find_elements_by_xpath(driver, xpath):
    try:
        return driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return None


def get_replies(comment_element, selectors):
    replies = []
    data = comment_element.find_elements_by_xpath(selectors.get("comment_reply"))
    for d in data:
        try:
            author = d.find_element_by_xpath(selectors.get("comment_author")).text
            text = d.find_element_by_xpath(selectors.get("comment_text")).text
            replies.append([author, text])
        except Exception:
            pass
    return replies


def safe_find_element_by_id(driver, elem_id):
    try:
        return driver.find_element_by_id(elem_id)
    except NoSuchElementException:
        return None
