# Scraping_google.py

from google_images_download import google_images_download as google
from selenium import webdriver
import ssl, os
ssl._create_default_https_context = ssl._create_unverified_context


def get_google_image(keyword, dir):
    response = google.googleimagesdownload()
    arguments = {'keywords': keyword,
                 'limit': 100,
                 'print_urls': False,
                 'no_directory' : True,
                 'output_directory': dir,
                 'chromedriver':'/home/sunshine/Documents/Develop/Project/scraping/chromedriver'
                 }
    response.download(arguments)


def looping_keywords(keywords):
    cwd = os.getcwd()
    for keyword in keywords:
        dir = cwd + f"/images/{keyword}"

        if not os.path.exists(dir):
            os.mkdir(dir)
        get_google_image(keyword, dir)


def main():
    keywords = ['face']
    looping_keywords(keywords)

main()
