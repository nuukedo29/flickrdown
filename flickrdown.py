import requests 
import re
import sys

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"

response = requests.get(sys.argv[1], headers={"User-Agent": USER_AGENT})

downloaded = []

for url, filename in re.findall(r"(live.staticflickr.com/.{4}/(.{11}_.{10}_o.jpg))", response.text.replace("\\", "")):
	if filename in downloaded: continue
	print(url, filename)
	with requests.get("https://" + url, headers={"User-Agent": USER_AGENT}, stream=True) as response:
		with open(filename, "wb") as file:
			for chunk in response.iter_content(chunk_size=1024*64):
				file.write(chunk)
	downloaded.append(filename)