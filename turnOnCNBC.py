import schedule
import time
import webbrowser
from selenium import webdriver


socialMediaUrls = ["http://www.cnbc.com/live-tv/?trknav=navigation:livetv:watch-cnbc-tv:100746233", "https://www.cnn.com", "https://www.gmail.com"]
def open_tabs(url_lists):
	for url in url_lists:
		 webbrowser.open_new_tab(url)

def job(t):
	open_tabs(socialMediaUrls), t
	return

schedule.every().day.at("8:00").do(job,'It is 8:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

