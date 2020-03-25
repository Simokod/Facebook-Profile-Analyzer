# Simokod
Projects and having fun
### Installation 💻 

You will need to:

- Install latest version of [Google Chrome](https://www.google.com/chrome/).
- Install [Python 3](https://www.python.org/downloads/)
- Have a Facebook account without 2FA enabled

```bash
$ git clone https://github.com/harismuneer/Ultimate-Facebook-Scraper.git
$ cd Ultimate-Facebook-Scraper

# Set up a virtual env
$ python3 -m venv venv
$ source venv/bin/activate

# Install Python requirements
$ pip install -e .
```

The code is multi-platform and is tested on both Windows and Linux.
The tool uses latest version of [Chrome Web Driver](http://chromedriver.chromium.org/downloads). I have placed the webdriver along with the code but if that version doesn't work then replace the chrome web driver with the latest one according to your platform and your Google Chrome version.

### How to Run

- Fill your Facebook credentials into [`credentials.yaml`](credentials.yaml)
- Edit the [`input.txt`](input.txt) file and add many profiles links as you want in the following format with each link on a new line:

Make sure the link only contains the username or id number at the end and not any other stuff. Make sure its in the format mentioned above.

> Note: There are two modes to download Friends Profile Pics and the user's Photos: Large Size and Small Size. You can change the following variables in [`scraper/scraper.py`](scraper/scraper.py#L30). By default they are set to Small Sized Pics because its really quick while Large Size Mode takes time depending on the number of pictures to download

```python
# whether to download the full image or its thumbnail (small size)
# if small size is True then it will be very quick else if its False then it will open each photo to download it
# and it will take much more time
friends_small_size = True
photos_small_size = True
```

Run the `ultimate-facebook-scraper` command ! 🚀
