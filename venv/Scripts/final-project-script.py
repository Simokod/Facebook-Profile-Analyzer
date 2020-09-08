#!C:\FinalProject\Projects-and-Having-Fun\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ultimate-facebook-scraper','console_scripts','final-project'
__requires__ = 'ultimate-facebook-scraper'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ultimate-facebook-scraper', 'console_scripts', 'final-project')()
    )
