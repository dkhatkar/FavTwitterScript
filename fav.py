import twitter
import sys

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

f = open('last_used.conf', 'r')
id = f.readline()
m = open('new_favs.txt', 'w')
f.close()

statuses = api.GetSearch(str(sys.argv[1]), per_page=sys.argv[2], since_id=id)
#statuses = api.GetSearch('#manutd', per_page=200, since_id=id)
count = 0
for s in statuses:
	friend = api.GetUser(s.user.screen_name)
	
	if friend.followers_count == 0:
		follow_ratio = 1
	else:
		follow_ratio = friend.friends_count / friend.followers_count
	if follow_ratio > 0:
		#api.CreateFriendship(s.user.screen_name)
		status = api.GetStatus(s.id)
		if friend.id not in api.GetFriendIDs('khatinthekar'):
			if status.favorited == False:
				print str(follow_ratio) + " Ratio"
				print str(status.user.screen_name) + " favorited"
				api.CreateFavorite(status)
				count += 1
			m.write(str(status.id) + "\n")
			id = s.id

print "Favorited: " + str(count) + " tweets"
f = open('last_used.conf', 'w')
print id
f.write(str(id))
f.close()
m.close()
