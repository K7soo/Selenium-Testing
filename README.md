Selenium-Testing

INSTRUCTIONS 

# CONFIG #
1) pip install selenium -- installation of selenium
2) GO TO chromedriver and install win64 vers
3) install chromedriver 
    # https://sites.google.com/chromium.org/driver/ -- link
4) extract chromedriver in folder (selenium project folder)
5) get chromedriver.exe and place in same directory as main test file (main.py OR any other name)

# CODE #
1) install dependencies and libraries (import libs)
    # import selenium libs
    # import pandas libs
2) set variables for chromedriver
    # service = Service(executable_path="chromedriver.exe") 
    # driver = webdriver.Chrome(service=service)
3) write whole test script simulation
    # Open browser
    # Open website
    # Sign In
    # Login to acc
    # Find selenium tab
    # Scrape table data
4) run code (python main.py)