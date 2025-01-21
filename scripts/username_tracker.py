import requests
from bs4 import BeautifulSoup
import re
import time
from colorama import Fore, init  

init(autoreset=True)  

def run():
    try:
        sites = {
        "Roblox Trade": "https://rblx.trade/p/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Instagram": "https://www.instagram.com/{}",
        "Paypal": "https://www.paypal.com/paypalme/{}",
        "GitHub": "https://github.com/{}",
        "Giters": "https://giters.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Telegram": "https://t.me/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Blogger": "https://{}.blogspot.com",
        "Tumblr": "https://{}.tumblr.com",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Keybase": "https://keybase.io/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Behance": "https://www.behance.net/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "Patreon": "https://www.patreon.com/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Disqus": "https://disqus.com/by/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Weebly": "https://{}.weebly.com",
        "YouTube": "https://www.youtube.com/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "Mix": "https://mix.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Strava": "https://www.strava.com/athletes/{}",
        "Internet Archive": "https://archive.org/search?query={}",
        "Twitter Archive": "https://web.archive.org/web/*/https://twitter.com/{}/status/*",
        "Linktree": "https://linktr.ee/{}",
        "Xbox": "https://www.xboxgamertag.com/search/{}",
        "Twitter": "https://twitter.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Goodreads": "https://www.goodreads.com/{}",
        "VK": "https://vk.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Dribbble": "https://dribbble.com/{}",
        "AngelList": "https://angel.co/{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Tidal": "https://tidal.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",  
        "Ello": "https://ello.co/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "VK": "https://vk.com/{}",
        }

        username = input(f"{Fore.RED}[*] {Fore.GREEN}Enter the Username to Track: ").strip().lower()
        print("\nScanning... Please Wait.")

        session = requests.Session()
        number_site = 0
        number_found = 0
        sites_and_urls_found = []

        for site, url_template in sites.items():
            number_site += 1
            url = url_template.format(username)
            try:
                response = session.get(url, timeout=5)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_title = soup.title.string.lower() if soup.title else ""
                    if username in page_title or username in response.text.lower():
                        number_found += 1
                        sites_and_urls_found.append(f"{site}: {url}")
                        print(f"{Fore.RED}[+] {Fore.GREEN}{site}: {url}")
                    else:
                        print(f"{Fore.RED}[x] Not found on {site}")
                else:
                    print(f"{Fore.RED}[x] Not found on {site}")
            except requests.RequestException as e:
                print(f"{Fore.RED}[x] Error checking {site}: {e}")

        print("\nSummary:")
        print(f"Total sites checked: {number_site}")
        print(f"Total sites found: {number_found}")
        if sites_and_urls_found:
            print("\nSites where the username was found:")
            for site in sites_and_urls_found:
                print(site)

    except Exception as e:
        print(f"{Fore.RED} [!] An error occurred: {e}")
        
