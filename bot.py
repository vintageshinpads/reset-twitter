import tweepy
import json
# from progress.bar import Bar

class Twitter:

	def __init__(self):
		'''
		Enter your twitter app credentials here.
		consumer_key = 'Rqw03S7GstNhbgw30bxfBwE8U'
		consumer_secret = 'wEk3y7zZBIUzRf44R30ucwHLBoO3DLM1gXZoRMhmtM8M4qe474'
		access_token = '568978779-2lU9wHZBHlD5gpEulUIufeBbJD2mjmKRu1Gwr4hZ'
		access_token_secret = 'B5jTG4wOP8MrvTRxyLVOqSVgq5kg47BVQbqVaAfqL4K6n'
		'''
		self.consumer_key = 'Rqw03S7GstNhbgw30bxfBwE8U'
		self.consumer_secret = 'wEk3y7zZBIUzRf44R30ucwHLBoO3DLM1gXZoRMhmtM8M4qe474'
		self.access_token = '568978779-2lU9wHZBHlD5gpEulUIufeBbJD2mjmKRu1Gwr4hZ'
		self.access_token_secret = 'B5jTG4wOP8MrvTRxyLVOqSVgq5kg47BVQbqVaAfqL4K6n'
		self.keyword_list()

	def api(self):
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		self.api = tweepy.API(auth)
		print 'API Delivered.'
		return self.api

	def keyword_list(self):
		'''
		Edit your interests here.
		'''
		self.query_list = [
		'media news',
		# 'football news',
		'science news',
		'technology news'
		'music news',
		'indian news',
		'startup news',
		# 'reddit',
		# 'technology',
		# 'journalism',
		# 'football',
		# 'indian journalism',
		]

class ResetTimeLine:

	def __init__(self):
		self.t = Twitter()
		self.api = self.t.api()
		self.me = self.api.me()
		print 'Self delivered.'
		self.user_following = []
		self.get_self_followers()
		'''
		Edit here if you don't want to unfollow all your users.
		'''
		if self.user_following:
			self.unfollow_users()
		self.get_users_to_follow()
		self.follow_new_users()

	def get_self_followers(self):
		self.user_following = self.api.friends_ids(self.me.id)

	def unfollow_users(self):
		'''
		!
		unFollowBar = Bar('Unfollowing....',max=len(self.user_following))
		'''
		for u in self.user_following:
			'''
			unFollowBar.next()
			'''
                        unfollow = self.api.destroy_friendship(u)
                        # print 'User unfollowed: ', u
                        '''
                        unFollowBar.finish()
                        '''
                        # print 'All users unfollowed'

        def get_users_to_follow(self):
            self.users_to_follow = []
            for q in self.t.query_list:
                users = self.api.search_users(q)
                for u in users:
                    self.users_to_follow.append(u)

	def follow_new_users(self):
		'''
		followBar = Bar('Following....', max=len(self.users_to_follow))
		'''
		for u in self.users_to_follow:
			'''
			followBar.next()
			'''
			#user = self.api.get_user(u)
			if u._json['verified']:
				follow = self.api.create_friendship(u.id)
				if follow:
					print 'User followed: ', user.screen_name
		'''
		followBar.finish()
		'''

class WebSiteFeeds:

	def __init__(self):
		self.t = Twitter()
		self.api = self.t.api()
		self.scrap_feeds_from = []
		self.get_users_2_feed()

	def get_users_2_feed(self):
		for q in self.t.query_list:
			users = self.api.search_users(q)
			for u in users:
				if u._json['verified']:
					print u.id, u._json['entities']['url']['urls'][0]['expanded_url']
					self.scrap_feeds_from.append(u._json['entities']['url']['urls'][0]['expanded_url'])

