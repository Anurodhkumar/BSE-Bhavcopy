from apscheduler.schedulers.background import BackgroundScheduler
from csv_data_updater import redis_csv_updatedata

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(csv_data_updater.csv_data, trigger='cron', hour='18', minute='00')
    scheduler.start()