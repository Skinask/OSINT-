#!/usr/bin/env python3

import requests
import urllib.parse
from bs4 import BeautifulSoup
import sys

BANNER = r"""
========================================
   SIMPLE GOOGLE DORK OSINT TOOL
----------------------------------------
   Coded by : Rencezy
   Assisted by : ChatGPT
========================================
"""

print(BANNER)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def clean_ddg_url(url):
    """
    Extract real URL from DuckDuckGo redirect links
    """
    if "duckduckgo.com/l/?" in url:
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        if "uddg" in params:
            return urllib.parse.unquote(params["uddg"][0])
    return url


def search(username):
    query = f'site:facebook.com "{username}"'
    encoded = urllib.parse.quote(query)
    search_url = f"https://duckduckgo.com/html/?q={encoded}"

    response = requests.get(search_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    results = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "facebook.com" in href:
            clean_url = clean_ddg_url(href)
            if clean_url.startswith("https://www.facebook.com"):
                results.add(clean_url)

    return results


def main():
    try:
        username = input("Enter Username: ").strip()
    except KeyboardInterrupt:
        print("\nExit.")
        sys.exit(0)

    if not username:
        print("Username cannot be empty.")
        sys.exit(1)

    print("\nSearching...\n")
    results = search(username)

    if not results:
        print("No results found.")
        return

    for link in sorted(results):
        print(link)

    print(f"\nTotal results: {len(results)}")


if __name__ == "__main__":
    main()
