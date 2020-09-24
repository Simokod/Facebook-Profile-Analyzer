# Projects and having fun

### Installation

You will need:

- Latest version of Google Chrome.
- Python 3.
- A facebook account.

```bash
# Clone project:
> git clone https://github.com/Simokod/Projects-and-Having-Fun.git
> cd Projects-and-Having-Fun

# Set up a virtual env
> pip install virtualenv
> virtualenv venv

# Open venv:
# Linux:
> source venv/bin/activate
# Windows:
> venv\Scripts\activate.bat
  
# Install Python requirements
(venv) > pip install -e .
(venv) > pip install webdriver_manager
```

### How to Run
- Add profile urls you'd like to scrape in [input.txt](input.txt)
- Enter your facebook username and password in [credentials.yaml](credentials.yaml):
    ```yaml
    email: your_email
    password: your_password
    ```
    (Dev_mode)
  OR
  enter facebook username and password in the Tkinter window after running the program 
- Scrape away!

Run the `python manager.py` command in the project folder.

### Note

This tool uses xpaths of **'divs'** to extract data. Since Facebook updates its site frequently, the 'divs' get changed. Consequently, we have to update the divs accordingly to correctly scrape data.

---
## Progress:
Currently the program can scrape only profiles, and extract posts.
