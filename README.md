# Scraper-SINTA-UPI-2022
A program that functions to retrieve data for every UPI lecturer on the SINTA Indonesia website. Program written in the python programming language consists of several python files, each of which serves to retrieve data. For example, the univ_scraper is used to retrieve university data. In general, scraping programs use the scrapy library (official documentation is below) and some programs use regex.

## Documentation
https://docs.google.com/document/d/1uwXgovvAkaTEcOTPYtbZVLRdJvjZPcewc_nxSrRDlSA/edit?usp=sharing

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
    
