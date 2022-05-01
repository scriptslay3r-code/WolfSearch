import wolframalpha as wolf

app_id = 'REQ623-2JW2ET9K77'
client = wolf.Client(app_id)
def search(data):
	res = client.query(data)
	answer = next(res.results).text
	print(res)
	print(answer)