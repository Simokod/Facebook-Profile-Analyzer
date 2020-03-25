# Projects and having fun

### Installation

You will need:

- Latest version of Google Chrome.
- Python 3.
- A facebook account.

```bash
# Clone project:
$ git clone https://github.com/Simokod/Projects-and-Having-Fun.git
$ cd 

# Set up a virtual env
$ pip install virtualenv
$ virtualenv venv

# Open venv:
# Linux:
$ source venv/bin/activate
# Windows:
  venv\Scripts\activate.bat
  
# Install Python requirements
$ pip install -e .
```

### How to Run
- Enter your facebook username and password in [`credentials.yaml`](credentials.yaml).
- In the [`input.txt`](input.txt) file add profile urls with each link on a new line.

> Search the profile you want in facebook, and that is the url you want to write in input.txt.

Run the `ultimate-facebook-scraper` command in the project folder.
