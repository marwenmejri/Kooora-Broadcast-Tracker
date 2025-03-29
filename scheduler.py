import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import subprocess


logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

VENV_PYTHON = r"D:\KoooraBroadcastTracker\env\Scripts\python.exe"
SCRIPT_PATH = r"D:\KoooraBroadcastTracker\main.py"

def run_scraper_job():
    """
    Job function that runs the main scraper.
    """
    try:
        logging.info("Running scraper job...")
        result = subprocess.run([VENV_PYTHON, SCRIPT_PATH], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Script failed: {result.stderr}")
        else:
            logging.info("Script ran successfully.")
    except Exception as e:
        logging.exception("Failed to run the scraper job")

if __name__ == "__main__":
    scheduler = BlockingScheduler()

    # Schedule the scraper to run every hour, on the hour
    scheduler.add_job(
        run_scraper_job,
        trigger=CronTrigger(minute=0),  # Runs at minute 0 of every hour
        # trigger=CronTrigger(minute="*/2"),  # Runs every 2 minutes
        id="scraper_job",
        replace_existing=True
    )

    logging.info("Scheduler started. Scraper will run every hour, on the hour.")
    scheduler.start()