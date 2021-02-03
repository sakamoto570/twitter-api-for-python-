from requests_oauthlib import OAuth1Session
import json


def get_tweetID(CK, CS, AT, AS, ID):

    # タイムライン取得用のURL
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    # user_idで取得するアカウントを指定
    # countで最新ツイートを指定
    params = {"count": 1}

    # OAuth で GET
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params=params)

    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        timeline = json.loads(req.text)
        # 最新ツイートのツイートIDを返す
        for tweet in timeline:
            return tweet["id"]

    else:
        # エラーの場合
        print("Error1: %d" % req.status_code)


if __name__ == "__main__":

    CK = "kBJNR9IoZVrSoggyxfYDqJ7Yy"                                    # Consumer Key
    CS = "o7AyBcE06Hly7crq5DS5E8v2eFOoKnWo0rxAcILj0EAgmOwnqW"                                   # Consumer Secret
    AT = "1025957662037487616-VrnMlG28WOwsF831nvYJFUGLYgSOJQ"                                 # Access Token
    AS = "sskAIJPBiXH5XXMwtMLTmWmL0uj14vAw5kFz7utGR55BU"                                   # Accesss Token Secert
    ID = "1025957662037487616"

    print(get_tweetID(CK, CS, AT, AS, ID))
