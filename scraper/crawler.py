# scraper/crawler.py

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.by import By
import time

from config import HEADLESS, USER_AGENTS

"""
crawler.py

Contains logic for launching the Selenium browser and navigating to match pages on kooora.live.
"""


def get_random_user_agent():
    """
    Returns a random user-agent string from a predefined list.
    """
    
    return random.choice(USER_AGENTS)


def launch_browser(headless=HEADLESS):
    """
    Launches an undetected Chrome browser with stealth options.
    
    Args:
        headless (bool): Whether to run browser in headless mode.
        
    Returns:
        WebDriver: Selenium WebDriver instance.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")

    # Anti-detection setup
    user_agent = get_random_user_agent()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)

    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    # Bypass webdriver detection
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """
    })

    return driver


def take_screenshot_of_iframe(driver, match, screenshot_dir):
    """
    Handles locating the iframe, interacting with it, and taking a screenshot.

    Args:
        driver: Selenium WebDriver instance.
        match: MatchResult object containing match details.
        screenshot_dir: Directory to save the screenshot.

    Returns:
        str: Path to the saved screenshot file.
    """
    try:
        driver.get(match.screenshot_url)
        scroll_amount = random.randint(500, 700)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(8, 10))
        filename = f"{screenshot_dir}/{match.teams.replace(' ', '_')}_{match.batch_time.strftime('%Y%m%d_%H%M%S')}.png"
        driver.find_element(By.XPATH, "//div[@class='server-body']").screenshot(filename)
        return filename
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None
