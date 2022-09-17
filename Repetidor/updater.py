from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from Repetidor import WebScrapper

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(WebScrapper.Web_scrapping_sender, 'interval', minutes=1440)
    scheduler.start()