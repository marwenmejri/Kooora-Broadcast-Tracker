# scraper/exporter.py

import pandas as pd
from datetime import datetime

def export_matches(matches: list):
    """
    Exports parsed match data to a timestamped CSV.

    Args:
        matches (list): Parsed matches.
    """
    data = [match.to_dict() for match in matches]
    df = pd.DataFrame(data)
    filename = f"output/kooora_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Exported {len(matches)} matches to {filename}")
