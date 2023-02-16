import requests as req
from bs4 import BeautifulSoup
import pandas as pd

# this class search for all information in IPMA API - OPEN DATA
# to collect all files available
class IPMACrawler :

  # loading initial configuration
  def __init__(self, verbose=True):
    self.initial_page = "https://api.ipma.pt/open-data"
    self.verb = verbose

  # get information about an specific page of IPMA API
  def _get_info(self, path = '/' ):
      if self.verb: print(f"getting {self.initial_page}{path}")
      text = req.get(f'{self.initial_page}{path}').text
      result = []
      for tag in  BeautifulSoup(text, 'html.parser').find('table').find_all('tr'):
        try:  _ , name, last_modification, size, description = tag.find_all('td')
        except: continue
        result.append({
          'name_resource' : name.find('a').text,
          'path_request'  : path,
          'last_modific'  : last_modification.text,
          'size_document' : size.text,
          'desc_resource' : description.text
        })
      return list(filter(lambda x : x['name_resource'] != 'Parent Directory' ,result))

  # this function detects all the subpaths in the list of information
  def _detect_paths(self,info_list):
    links = []
    for info in info_list:
      if '/' in info['name_resource']:
        links.append(f'{info["path_request"]}{info["name_resource"]}')
    return links

  # preprocessing information
  def _preprocessing(self,data):
    data = pd.DataFrame(data)
    data = data[data['name_resource'].apply(lambda x: not '/' in x)]
    data['format'] = data['name_resource'].apply(lambda x: x.split(".")[-1])
    data['url'] = self.initial_page + data['path_request'] + data['name_resource']
    data = data.drop(['desc_resource','path_request'],axis=1)
    return data

  # execute the crawler
  def collect_information(self):
    paths , data = ['/'] , []
    while len(paths) :
      path = paths.pop()
      info = self._get_info(path)
      paths += self._detect_paths(info)
      data += info
    return self._preprocessing(data)


if __name__ == "__main__":
  # Basic example of IPMA CRAWLER
  
  # instance of IPMA Crawler
  # use IPMACrawler(verbose=True) to supress messages
  crawler = IPMACrawler()

  # colleting information
  table = crawler.collect_information()

  # save information as excel file
  table.to_excel("data.xlsx")

