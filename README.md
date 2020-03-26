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
> pip install -e .
```

### How to Run
Run the `final-project` command in the project folder.
Using the built-in menu:
- Enter your facebook username and password. (or enter them manually in [credentials.yaml](credentials.yaml))
- Add profile urls you'd like to scrape. (or enter them manually in [input.txt](input.txt))
- Scrape away!


```bash
# Update configurations:
> python setup.py develop
