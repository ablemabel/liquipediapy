from bs4 import BeautifulSoup
from configparser import ConfigParser
from glob import glob
import unicodedata


class DevParser():
	"""Object used to write query to file and re-read data from it,
	Avoiding liquidpedia overload.
	DevParser takes in the path of folder 
	where we'll store html pages
	"""

	def __init__(self, config_folder: str):
		self.__folder_path = config_folder

	def isPageAvailableLocally(self, page: str) -> bool:
		page = self.format_page(page)
		glb = glob(self.__folder_path + '*.html')
		glb = [g.split('\\')[-1] for g in glb]
		return f"{page}.html" in glb

	def format_page(self, page: str) -> str:
		page = page.replace('/', '_')
		page = page.replace(':', '_')
		return page

	def format_data(self, data: str) -> str:
		data = unicodedata.normalize("NFKD", data)
		data = data.replace('\t', ' ')
		return data

	def fromFile(self, page: str) -> tuple:
		print(f"fromFile")
		try:
			page = self.format_page(page)
			page_path = f"{self.__folder_path}{page}.html"
			soup = None
			with open(page_path, 'r', encoding="utf-8") as f:
				content = f.read()
				content = self.format_data(content)
				soup = BeautifulSoup(content, features="lxml")
			return True, soup
		except FileNotFoundError:
			return False, None

	def toFile(self, soup: BeautifulSoup, page: str):
		print(f"toFile")
		# Only for smash player pages, we'll have to handle that better on
		page = self.format_page(page)
		page_path = f"{self.__folder_path}{page}.html"
		with open(page_path, 'w', encoding="utf-8") as f:
			f.write(str(soup))
