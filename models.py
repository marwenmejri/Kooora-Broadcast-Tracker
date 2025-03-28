# models.py

from datetime import datetime
from urllib.parse import urlparse
from typing import Optional

class MatchResult:
    """
    Represents a scraped match result from the kooora live stream site.
    """
    def __init__(self, batch_time: datetime, teams: str, channel: str, status: str, page_url: str, 
                 match_url: Optional[str] = None,screenshot_url: Optional[str] = None):
        self.batch_time = batch_time
        self.teams = teams
        self.channel = channel
        self.status = status
        self.page_url = page_url
        self.match_url = match_url
        self.screenshot_url = screenshot_url

        self.validate()

    def validate(self):
        """Validates the match result."""
        if not self.teams or not self.teams.strip():
            raise ValueError("Teams field cannot be empty")

        if not self.channel or not self.channel.strip():
            raise ValueError("Channel field cannot be empty")

        if self.status not in ["Broadcasted", "Reported", "Finished"]:
            raise ValueError("Status must be either 'Broadcasted' or 'Reported' or 'Finished' ")

        try:
            urlparse(self.page_url)
        except Exception:
            raise ValueError("Invalid page URL")

        if self.status == "Broadcasted" and not self.screenshot_url:
            raise ValueError("Screenshot URL is required when status is 'Broadcasted'")

        if self.status == "Reported" and self.screenshot_url:
            raise ValueError("Screenshot URL must be None when status is 'Reported'")

    def to_dict(self):
        """Converts the object to a dictionary."""
        return {
            "batch_time": self.batch_time.isoformat(),
            "teams": self.teams,
            "channel": self.channel,
            "status": self.status,
            "page_url": self.page_url,
            "match_url": self.match_url,
            "screenshot_url": self.screenshot_url
        }
