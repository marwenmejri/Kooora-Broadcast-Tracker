# main.py

from scraper.crawler import launch_browser, take_screenshot_of_iframe
from scraper.parser import parse_matches_from_html
from scraper.exporter import export_matches
from config import TARGET_URL, RETRY_COUNT, SCREENSHOT_DIR
from logger import setup_logger

import os
import time

logger = setup_logger()

def run_scraper():
    """
    Main runner: launches browser, scrapes, and exports matches.
    """
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    logger.info("Scraping started.")

    driver = launch_browser()
    try:
        driver.get(TARGET_URL)
        html = driver.page_source
        page_url = driver.current_url
        matches = parse_matches_from_html(html, page_url)
        logger.info(f"Found {len(matches)} matches.")

        for match in matches:
            if match.status in ["Broadcasted", "Finished"] and match.screenshot_url:
                for attempt in range(1, RETRY_COUNT + 1):
                    try:
                        logger.info(f"[{attempt}/{RETRY_COUNT}] Screenshotting: {match.teams}")
                        screenshot_path = take_screenshot_of_iframe(driver, match, SCREENSHOT_DIR)
                        if screenshot_path:
                            logger.info(f"Screenshot saved: {screenshot_path.split('/')[-1]}")
                            match.screenshot_url = screenshot_path.split("/")[-1]
                            break
                        else:
                            logger.warning("Failed to take screenshot.")
                    except Exception as e:
                        logger.warning(f"Screenshot failed: {e}")
                        time.sleep(2)
                else:
                    logger.error(f"Screenshot failed after {RETRY_COUNT} tries: {match.teams}")
                    match.screenshot_url = None

        export_matches(matches)
        logger.info("Scraping finished.")
    finally:
        driver.quit()
        

if __name__ == "__main__":
    run_scraper()
