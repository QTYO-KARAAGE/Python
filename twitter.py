#Twitterで自動的にツイートしてくれるプログラム
import tweepy
import os

#APIとアクセストークンの取得
api_key = os.getenv('api_key')
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

#自動でツイートする際の準備
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#ツイート内容をダブルクォーテーション内に入れる。
api.update_status("hoge")

#ツイートに成功した際に、出力する。
print("Success!") 