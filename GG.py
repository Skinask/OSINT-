#!/usr/bin/env python3

import requests
import urllib.parse
from bs4 import BeautifulSoup
import sys
import time

print("""
====================================
   SIMPLE GOOGLE DORK OSINT TOOL
====================================
""")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def search(username):
    query = f'site:facebook.com "{username}"'
    encoded = urllib.parse.quote(query)
    url = f"https://duckduckgo.com/html/?q={encoded}"

    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    results = set()
    for a in soup.find_all("a", href=True):
        if "facebook.com" in a["href"]:
            results.add(a["href"])

    return results


def main():
    username = input("Enter Username: ").strip()

    if not username:
        print("Username cannot be empty")
        sys.exit(1)

    print("\nSearching...\n")
    results = search(username)

    if not results:
        print("No results found.")
        return

    for link in results:
        print(link)

    print(f"\nTotal results: {len(results)}")


if __name__ == "__main__":
    main()
