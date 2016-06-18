import requests, json, os, time


class Currency:
	def get(self):
		data = self.get_data()
		return {
			'timestamp': data['timestamp'],
			'rates': {
				'BRL': data['rates']['BRL']
			}
		}

	def update_currency(self):
		url = "https://openexchangerates.org/api/latest.json?app_id=" + os.environ['OPENEXCHANGERATES_APP_ID'] + "&base=USD"
		resp = requests.get(url)
		respJson = resp.json()
		f = open('cache.json', 'w')
		f.write(json.dumps(respJson))
		return respJson


	def get_data(self):
		update = False

		if os.path.isfile('cache.json')==False:
			update = True
		else:
			file_ts = os.stat('cache.json').st_mtime
			now_ts = time.time()

			if now_ts-file_ts > float(os.environ['API_CACHE_TIMEOUT_MINS'])*60:
				update = True

		if(update):
			return self.update_currency()
		else:
			with open('cache.json') as data_file:
				cache = json.load(data_file)

			return cache
