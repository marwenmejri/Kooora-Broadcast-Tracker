# scraper/parser.py

import time
import random
from bs4 import BeautifulSoup
from models import MatchResult
from datetime import datetime

def parse_matches_from_html(html: str, page_url: str) -> list[MatchResult]:
    soup = BeautifulSoup(html, 'html.parser')
    matches = []

    for match_div in soup.find_all("div", class_="AY_Match"):
        try:
            time.sleep(random.uniform(0.5, 1.0))
            team1 = match_div.find("div", class_="MT_Team TM1").find("div", class_="TM_Name").text.strip()
            team2 = match_div.find("div", class_="MT_Team TM2").find("div", class_="TM_Name").text.strip()
            teams = f"{team1} VS {team2}"

            channel = match_div.find("div", class_="MT_Info").find("ul").find_all("li")[0].text.strip()
            video_link_tag = match_div.find("a", href=True)
            match_url = video_link_tag["href"] if video_link_tag else None

            if "live" in match_div.get("class", []):
                status = "Broadcasted"
                screenshot_url = match_url
            elif "finished" in match_div.get("class", []):
                status = "Finished"
                screenshot_url = match_url
            else:
                status = "Reported"
                screenshot_url = None
                match_url = None

            match = MatchResult(
                batch_time=datetime.now(),
                teams=teams,
                channel=channel,
                status=status,
                page_url=page_url,
                match_url=match_url,
                screenshot_url=screenshot_url
            )
            matches.append(match)
        except Exception as e:
            print(f"Error parsing a match block: {e}")
            continue

    return matches
