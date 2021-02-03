from requests_oauthlib import OAuth1Session
import json


def get_user_timeline(CK, CS, AT, AS, ID, since_id):

    # 取得したツイート格納用の配列
    tweet_list = []

    # タイムライン取得用のURL
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    # user_idでアカウントIDを指定
    # countで取得ツイート数を上限まで上げる
    # since_idで取得するツイートの範囲を限定
    params = {"count": 200, "since_id": since_id}

    # OAuth で GET
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        timeline = json.loads(req.text)
        # sinceID以降のツイートをリストにまとめて返す
        for tweet in timeline:
            tweet_list.append(tweet["text"])
    else:
        # エラーの場合
        print("Error: %d" % req.status_code)

    #ツイート格納用の配列を返す
    return tweet_list


if __name__ == "__main__":

    CK = "###"                                    # Consumer Key
    CS = "####"                                   # Consumer Secret
    AT = "######"                                 # Access Token
    AS = "####"                                   # Accesss Token Secert
    ID = "##"
    #since_id = ***

    #print(get_user_timeline(CK, CS, AT, AS, ID, since_id))
