# Scraper-SINTA-UPI-2022
A program that functions to retrieve data for every UPI lecturer on the SINTA Indonesia website

## Installation
    pip install scrapy
    pip install requests

## Run Program
    scrapy runspider scraper.py
    
## Export Data
### csv
    scrapy runspider scraper.py -o dosen.csv
### json
    scrapy runspider scraper.py -o dosen.json
    
