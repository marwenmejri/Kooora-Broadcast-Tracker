
# Kooora Broadcast Tracker

**Kooora Broadcast Tracker** is a Python-based web scraper designed to monitor live football matches on [Kooora](https://kooora.live). It scrapes match details, captures screenshots of live broadcasts, and exports parsed data to CSV files. 

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Scheduling](#Ssheduling)
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
  - `Scheduler`

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

## Scheduling
To run the scraper automatically every hour, we use the included scheduler script (scheduler.py) along with a .bat file.

### Scheduler Setup
1. **Scheduler Script**:

   ```bash
   VENV_PYTHON = r"D:\KoooraBroadcastTracker\env\Scripts\python.exe"
   SCRIPT_PATH = r"D:\KoooraBroadcastTracker\main.py"
   ```

2. **Run the Scheduler**:
   ```bash
      python scheduler.py
   ```
Start the scheduler manually

3. **Keep the Scheduler Running**:

   ```bash
      @echo off
      :: Navigate to the project directory
      cd D:\KoooraBroadcastTracker

      :: Activate the virtual environment
      call env\Scripts\activate

      :: Run the scheduler script
      python scheduler.py

   ```
To ensure the scheduler runs continuously, create a .bat file to execute it and keep it running in the background.
Create run_scheduler.bat

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


### Example Scheduler Logs
```
2025-03-29 03:12:06,658 [INFO] Scheduler started
2025-03-29 03:14:00,017 [INFO] Running job "run_scraper_job (trigger: cron[minute='*/2'], next run at: 2025-03-29 03:14:00 GMT)" (scheduled at 2025-03-29 03:14:00+00:00)
2025-03-29 03:14:00,018 [INFO] Running scraper job...
2025-03-29 03:14:25,446 [INFO] Script ran successfully.
2025-03-29 03:14:25,446 [INFO] Job "run_scraper_job (trigger: cron[minute='*/2'], next run at: 2025-03-29 03:16:00 GMT)" executed successfully
2025-03-29 03:16:00,003 [INFO] Running job "run_scraper_job (trigger: cron[minute='*/2'], next run at: 2025-03-29 03:18:00 GMT)" (scheduled at 2025-03-29 03:16:00+00:00)
2025-03-29 03:16:00,003 [INFO] Running scraper job...
2025-03-29 03:16:32,621 [INFO] Script ran successfully.
2025-03-29 03:16:32,621 [INFO] Job "run_scraper_job (trigger: cron[minute='*/2'], next run at: 2025-03-29 03:18:00 GMT)" executed successfully
2025-03-29 03:18:00,001 [INFO] Running job "run_scraper_job (trigger: cron[minute='*/2'], next run at: 2025-03-29 03:20:00 GMT)" (scheduled at 2025-03-29 03:18:00+00:00)
2025-03-29 03:18:00,001 [INFO] Running scraper job...
2025-03-29 03:18:41,117 [INFO] Script ran successfully.
```

## Contact

For questions or feedback, contact [Marwen Mejri] at [mejri.marwen00@gmail.com].
