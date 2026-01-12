#!/usr/bin/env python3
"""
Simple Google Dork OSINT Tool
Author: YourName
Purpose: Username-based OSINT using search engine dorks
"""

import requests
import urllib.parse
from bs4 import BeautifulSoup
import sys
import time


BANNER = r"""
====================================
   SIMPLE GOOGLE DORK OSINT TOOL
====================================
"""


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}


def build_dorks(username):
    """
    Generate dorks for Facebook
    """
    return [
        f'site:facebook.com "{username}"',
        f'site:facebook.com "{username}" "posts"',
        f'site:facebook.com "{username}" "comment"',
        f'site:facebook.com "{username}" "photos"'
    ]


def duckduckgo_search(query):
    """
    Perform DuckDuckGo HTML search
    """
    encoded = urllib.parse.quote(query)
    url = f"https://duckduckgo.com/html/?q={encoded}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        return response.text
    except requests.RequestException:
        return None


def extract_links(html):
    """
    Extract Facebook links from HTML
    """
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "facebook.com" in href:
            if href.startswith("/l/?kh="):
                continue
            links.add(href)

    return links


def main():
    print(BANNER)

    try:
        username = input("Enter Username: ").strip()
    except KeyboardInterrupt:
        print("\nExit.")
        sys.exit(0)

    if not username:
        print("Username cannot be empty.")