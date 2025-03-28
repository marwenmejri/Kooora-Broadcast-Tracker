
# Kooora Broadcast Tracker

**Kooora Broadcast Tracker** is a Python-based web scraper designed to monitor live football matches on [Kooora](https://kooora.live). It scrapes match details, captures screenshots of live broadcasts, and exports parsed data to CSV files. 

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#outputs)
- [Results](#results)

## Overview

The Kooora Broadcast Tracker automates the process of scraping live football match information from Kooora. Key functionalities include:
- Scraping match details such as teams, channels, and broadcast status.
- Capturing high-quality screenshots of live match broadcasts.
- Exporting parsed data to timestamped CSV files.

## Features

- **Scraping**: Efficiently extracts match details from Kooora's live stream pages.
- **Screenshot Capture**: Automatically takes screenshots of live broadcasts.
- **CSV Export**: Saves scraped data in structured CSV files for easy analysis.
- **Logging**: Detailed logs for debugging and monitoring.
- **Anti-Detection**: Uses stealthy browser configurations to avoid detection by anti-bot systems.

## Prerequisites

- **Python 3.8+**
- **Dependencies**:
  - `beautifulsoup4`
  - `undetected-chromedriver`
  - `selenium`
  - `pandas`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/marwenmejri/KoooraBroadcastTracker.git
   cd KoooraBroadcastTracker
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   env\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Settings**:
   - Edit `config.py` to set the target URL and other parameters if needed.

## Usage

1. **Run the Script**:
   ```bash
   python main.py
   ```

2. **Outputs**:
   - **CSV Files**: Saved in the `output/` directory.
   - **Screenshots**: Saved in the `Screenshots/` directory.
   - **Logs**: Saved in the `logs/` directory.

## Outputs

### CSV Output Example

The script generates CSV files with the following columns:
- `batch_time`: Timestamp of the scrape.
- `teams`: Names of the teams playing.
- `channel`: Broadcasting channel.
- `status`: Match status (`Broadcasted`, `Reported`, or `Finished`).
- `page_url`: URL of the match page.
- `match_url`: URL of the match video (if available).
- `screenshot_url`: Path to the screenshot file (if captured).

Example CSV row:
```
batch_time,teams,channel,status,page_url,match_url,screenshot_url
2025-03-28T21:58:12.855962,باير ليفركوزن VS بوخوم,beIN SPORTS 5 HD,Finished,https://kooora.live-kooora.com/,https://kooora.live-kooora.com/matches/%d8%a8%d8%a7%d9%8a%d8%b1-%d9%84%d9%8a%d9%81%d8%b1%d9%83%d9%88%d8%b2%d9%86-%d9%88-%d8%a8%d9%88%d8%ae%d9%88%d9%85-%d9%81%d9%8a-%d8%a7%d9%84%d8%af%d9%88%d8%b1%d9%8a-%d8%a7%d9%84%d8%a3%d9%84%d9%85%d8%a7/,باير_ليفركوزن_VS_بوخوم_20250328_215812.png
2025-03-28T21:58:13.831597,الزمالك VS سيراميكا كليوباترا,On Sport 1,Finished,https://kooora.live-kooora.com/,https://kooora.live-kooora.com/matches/%d8%a7%d9%84%d8%b2%d9%85%d8%a7%d9%84%d9%83-%d9%88-%d8%b3%d9%8a%d8%b1%d8%a7%d9%85%d9%8a%d9%83%d8%a7-%d9%83%d9%84%d9%8a%d9%88%d8%a8%d8%a7%d8%aa%d8%b1%d8%a7-%d9%81%d9%8a-%d9%83%d8%a3%d8%b3-%d9%85%d8%b5/,الزمالك_VS_سيراميكا_كليوباترا_20250328_215813.png
2025-03-28T21:58:14.542354,بيراميدز VS البنك الأهلي,On Sport 2,Finished,https://kooora.live-kooora.com/,https://kooora.live-kooora.com/matches/%d8%a8%d9%8a%d8%b1%d8%a7%d9%85%d9%8a%d8%af%d8%b2-%d9%88-%d8%a7%d9%84%d8%a8%d9%86%d9%83-%d8%a7%d9%84%d8%a3%d9%87%d9%84%d9%8a-%d9%81%d9%8a-%d9%83%d8%a3%d8%b3-%d9%85%d8%b5%d8%b1-2025-03-28/,بيراميدز_VS_البنك_الأهلي_20250328_215814.png
2025-03-28T21:58:15.126024,ستراسبورج VS أولمبيك ليون,beIN SPORTS 4 HD,Finished,https://kooora.live-kooora.com/,https://kooora.live-kooora.com/matches/%d8%b3%d8%aa%d8%b1%d8%a7%d8%b3%d8%a8%d9%88%d8%b1%d8%ac-%d9%88-%d8%a3%d9%88%d9%84%d9%85%d8%a8%d9%8a%d9%83-%d9%84%d9%8a%d9%88%d9%86-%d9%81%d9%8a-%d8%a7%d9%84%d8%af%d9%88%d8%b1%d9%8a-%d8%a7%d9%84%d9%81/,ستراسبورج_VS_أولمبيك_ليون_20250328_215815.png

```

### Screenshot Example

The script captures screenshots of live broadcasts and saves them in the `Screenshots/` directory. Here’s an example:

![Live Broadcast Screenshot](./Screenshots/ستراسبورج_VS_أولمبيك_ليون_20250328_214528.png)

## Results

### Chrome Driver Running

The script uses Selenium with `undetected-chromedriver` to interact with the website. Below is a screenshot of the Chrome browser running during the scraping process:

![Chrome Driver Running](./Screenshots/chrome_driver_running.png)

## Contact

For questions or feedback, contact [Marwen Mejri] at [mejri.marwen00@gmail.com].
