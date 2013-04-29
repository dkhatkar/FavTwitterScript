import twitter

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

f = open('new_favs.txt', 'r')

for line in f:
	line = line.strip()
	print line 
	s = api.GetStatus(line)
	api.DestroyFavorite(s)
