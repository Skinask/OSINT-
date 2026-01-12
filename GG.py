#!/usr/bin/env python3

import urllib.parse

BANNER = r"""
========================================
   SIMPLE GOOGLE DORK GENERATOR
----------------------------------------
   Coded by : Rencezy
   Assisted by : ChatGPT
========================================
"""

print(BANNER)


def generate_dorks(name):
    parts = name.split()

    dorks = [
        f'site:facebook.com {name}',
        f'site:facebook.com "{name}"',
        f'site:facebook.com "{name}" posts',
        f'site:facebook.com "{name}" comments',
        f'site:facebook.com "{name}" photos',
        f'site:facebook.com "{name}" videos',
        f'site:facebook.com "{name}" profile',
        f'site:facebook.com "{name}" groups',
        f'site:facebook.com "{name}" public',
        f'site:facebook.com "{name}" people',
    ]

    for p in parts:
        dorks.append(f'site:facebook.com {p}')
        dorks.append(f'site:facebook.com "{p}"')

    # Remove duplicates and limit to 15
    return list(dict.fromkeys(dorks))[:15]


def main():
    name = input("Enter Username or Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    print("\nGoogle Dork URLs (Copy & Paste):\n")

    dorks = generate_dorks(name)

    for dork in dorks:
        encoded = urllib.parse.quote(dork)
        url = f"https://www.google.com/search?q={encoded}"
        print(url)

    print(f"\nTotal Dorks Generated: {len(dorks)}")


if __name__ == "__main__":
    main()
