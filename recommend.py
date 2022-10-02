import numpy as np
import pandas as pd
import random
import time
import json
from urllib.request import urlopen

class Anime(object):
	def __init__(self):
		url = 'https://api.jikan.moe/v4/random/anime'
		response = urlopen(url)
		data_json = json.loads(response.read())
		df = pd.json_normalize(data_json['data'])
		self.name = df['title_english'][0]
		if self.name == None:
			self.name = df['title'][0]
		self.type = df['type'][0]
		self.status = df['status'][0]
		self.image = df['images.jpg.image_url'][0]

test = Anime()
print('name : ' + test.name + '\ntype : ' + test.type + '\nstatus : ' + test.status)
print(test.image)
