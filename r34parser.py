import bs4, urllib3, os
class r34Parser:
	def _parse_img_url(self, request_url):
		session = urllib3.PoolManager()
		request = session.request("GET", request_url)
		#print(request.data)
		data=request.data
		parser = bs4.BeautifulSoup(data, "html.parser")
		for i in parser.find_all("img"):
			img_url=i.get("src")
			try:
				if (os.path.join(img_url).strip().split("/")[5][:-8]).endswith("?"):
					with open(os.path.join(img_url).strip().split("/")[5][:-9], "wb") as f:
						f.write(session.request("GET", img_url).data)
						print(f"Saved at: {os.path.join(img_url).strip().split('/')[5][:-9]}")
				else:
					with open(os.path.join(img_url).strip().split("/")[5][:-8], "wb") as f:
						f.write(session.request("GET", img_url).data)
						print(f"Saved at: {os.path.join(img_url).strip().split('/')[5][:-8]}")
			except:
				try:
					with open(os.path.join(img_url).strip().split("/")[4], "wb") as f:
						f.write(session.request("GET", img_url).data)
						print(f"Saved at: {os.path.join(img_url).strip().split('/')[4]}")
				except Exception as e:
					print(f"Error: {e}")
r=r34Parser()
r._parse_img_url("https://rule34.xxx/index.php?page=post&s=list&tags=brawl_stars+")