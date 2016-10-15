from selenium import webdriver


driver = webdriver.PhantomJS(executable_path='/Users/alexlanders/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('http://localhost:8000') #TODO Move to settings.py

assert 'desyREPORTS' in driver.title