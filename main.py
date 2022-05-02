import requests
from bs4 import BeautifulSoup
from art import text2art
from colorama import init
from termcolor import colored
import datetime
from selenium import webdriver

Scraped_Links = []


def m3u_Creator(fname):
    x = datetime.datetime.now()
    
    i = 1

    print("[*]Generating the M3U playlist..")
    m3u_creator = open(f"{x.strftime('%d-%m-%y %I-%M-%S-%p')} {fname.upper()}.m3u8", "a", encoding="utf-8")
    m3u_creator.write("#EXTM3U \n")
    for link in Scraped_Links:
        m3u_creator.write(f'#EXTINF:-1 tvg-id="Channel{i}",Channel{i}\n{link}\n')
        i = i + 1

    print("[*]Generated file!")

	print("Checking for valid channels..")
	
	i = 1
	
	workingLinks = []
	
	try: 
			for link in Scraped_Links:
             	req=str(requests.get(link, timeout=(2,5)).status_code) 
             	if req == "200" or (req == "302"): 
                 	workingLinks.append(link)
 		m3u_creator.truncate()
 		m3u.creator.write("#EXTM3U")
 		for wlink in workingLinks:
 			m3u_creator.write(f'#EXTINF:-1 tvg-id="Channel{i}",Channel{i}')
 			m3u_creator.write(f'{wlink}')
 	except: 
             		print("An unknown error has occurred.")   
init()


def random_iptv(no, name):
    page_no = 1
    for i in range(no):
        print(f"{page_no}/{no}")
        url = f"https://streamtest.in/logs/page/{str(page_no)}?filter={name}&is_public=true"
        result = requests.get(url).text
        soup = BeautifulSoup(result, "html.parser")
        scraped_links = soup.find_all('div', {'class': 'url is-size-6'})

        for link in scraped_links:
            Scraped_Links.append(link.text)

        page_no = page_no + 1


art = text2art("Jackalope")
print(colored(art, "yellow"))
print(colored("by doubleohcosmo", "blue"))

channel_name = input("Channel to search: ")
no_of_pages_to_scrape = int(input("How many pages to scrape: "))

random_iptv(no_of_pages_to_scrape, channel_name)
m3u_Creator(channel_name)
