from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)