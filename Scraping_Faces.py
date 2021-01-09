# pip3 install git+https://github.com/Joeclinton1/google-images-download.git
# https://google-images-download.readthedocs.io/en/latest/arguments.html# 

from google_images_download import google_images_download as google
from selenium import webdriver
import ssl, os
ssl._create_default_https_context = ssl._create_unverified_context # if more than 100 images

def get_google_image(keyword):
    response = google.googleimagesdownload()
    arguments = {'keywords': keyword,
                 'limit': 500,
                 'output_directory': 'before_images', # The directory structure : <output_directory><image_directory><images>
                 'image_directory': 'others',
                #'no_directory' : True,         
                 'print_urls': False,
                 'format':'jpg',
                 'chromedriver':'./chromedriver'
                 }
    response.download(arguments)

def main():
    if not os.path.exists('./before_images/others'):
        os.makedirs('./before_images/others')

    keywords = ['face'] 
    for keyword in keywords:
        get_google_image(keyword) 

main()
