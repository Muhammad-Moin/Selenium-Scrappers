# Selenium Scrapers

A collection of Python web scrapers built with Selenium, plus a small threading example.

## Contents

| Folder | What it does |
|--------|--------------|
| [`Gitex/`](Gitex/) | Scrapes the GITEX Global 2023 exhibitor directory with Selenium and ChromeDriver, walks the exhibitor listings, and saves the collected company data to a spreadsheet with pandas. Available as a script and as a Jupyter notebook. |
| [`Threading/`](Threading/) | A minimal example of running two CPU-bound functions in parallel with Python's `threading` module and timing the result. |

## Requirements

- Python 3.8 or newer
- Google Chrome (ChromeDriver is downloaded automatically by `webdriver-manager`)

```bash
pip install selenium webdriver-manager pandas
```

## Run the GITEX scraper

```bash
cd Gitex
python gitext_scrapper.py
```

The script opens Chrome, loads the exhibitor list, collects each exhibitor's details and writes them out with pandas. Or open `gitext_scrapper.ipynb` to step through it cell by cell.

## Run the threading example

```bash
cd Threading
python threading.py
```

## Notes

- Sites change their markup over time. If a scraper stops finding elements, update the XPath or CSS selectors in the script.
- For personal and educational use. Check a site's terms of use before scraping it.
