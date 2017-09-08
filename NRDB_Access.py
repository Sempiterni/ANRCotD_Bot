import requests

class NRDB_Access:

	def GetPackURLs(self):
		url = 'https://api.github.com/repos/Alsciende/netrunner-cards-json/contents/pack/'

		pack_urls = []

		req = requests.get(url)
		if req.status_code == requests.codes.ok:
		    req = req.json()
		    for item in req:
		    	pack_urls.append(item['download_url'])
		else:
		    print 'Error downloading pack list.'

		return pack_urls

	def DownloadPacks(self, urls):
		packs = []

		for url in urls:
			# print url
			pack = []
			req = requests.get(url)
			if req.status_code == requests.codes.ok:
			    req = req.json()
			    for item in req:
			    	pack.append(item)
			    packs.append(pack)
			else:
			    print 'Error downloading pack:', url
		return packs

	def PickRandom(self, packs):
		import random
		pack = random.choice(packs)
		pick = random.choice(pack)
		return pick

def main():
	NRDB = NRDB_Access()

	print 'Downloading pack list...'
	pack_urls = NRDB.GetPackURLs()
	print 'Downloading packs...'
	packs = NRDB.DownloadPacks(pack_urls)
	print 'Downloaded %d packs' % len(packs)

	print 'Choosing randomly'
	pick = NRDB.PickRandom(packs)
	print pick

if __name__ == "__main__":
    main()