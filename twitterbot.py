import tweepy
import time

auth = tweepy.OAuthHandler('',
                           '')
auth.set_access_token('',
                      '')

#aqui a api procura por 10 tweets que contenham "around the world"
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
search = 'around the world'
numero = 10
#api responde os 10 tweets com "AROUND THE WORLD"
for status in tweepy.Cursor(api.search, search).items(numero):
    try:
        print("nome do usuario: @" + status.user.screen_name)
        api.update_status("@" + status.user.screen_name + " AROUND THE WORLD ! ", in_reply_to_status_id=status.id)
        print("sucesso")
        time.sleep(60) #api entra em sleep por 60s e repete o processo
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
