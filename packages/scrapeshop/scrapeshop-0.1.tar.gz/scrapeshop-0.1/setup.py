from setuptools import setup, find_packages
import requests
import json
import logging

setup(
    name="scrapeshop",
    version='0.1',
    author="Malik Hassan",
    author_email="<malikkhabhassan@gmail.com>",
    packages=find_packages('requests', 'json', 'logging'),
    install_requires=[],
    keywords=['python', 'shopify', 'scrape', 'shopify scraper', 'web scraping', 'web'],
)