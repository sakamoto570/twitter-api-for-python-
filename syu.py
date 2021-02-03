import json #標準のjsonモジュールとconfig.pyの読み込み
import MeCab
import random
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK="kBJNR9IoZVrSoggyxfYDqJ7Yy"
CS="o7AyBcE06Hly7crq5DS5E8v2eFOoKnWo0rxAcILj0EAgmOwnqW"
AT="1025957662037487616-VrnMlG28WOwsF831nvYJFUGLYgSOJQ"
AS="sskAIJPBiXH5XXMwtMLTmWmL0uj14vAw5kFz7utGR55BU"
twitter = OAuth1Session(CK, CS, AT, AS) #認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
url2 ="https://api.twitter.com/1.1/statuses/update.json"

tweets_data =[]
words=[] #単語リスト
tx=[]
t_text=""
dfile = 'C:/Users/sake_/Desktop/Tweet20180727.txt'#tweetfile
hukusifile = 'C:/Users/sake_/Desktop/tweethuku.txt'#hukusifile
keiyousifile = 'C:/Users/sake_/Desktop/tweetkei.txt'
dousifile = 'C:/Users/sake_/Desktop/tweetdou.txt'

h_d={"名詞":"meishi","副詞":"hukushi","形容詞":"keiyousi","動詞":"doushi"}

#params ={'count' : 5} #取得数
res = twitter.get(url)#params = params)



if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        #print(line['text'])
        tweets_data.append(line['text'])

else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)

with open(dfile, mode='w') as f:     #ツイートをtxtに書きこみ
    f.write('\n'.join(tweets_data))

#with open(dfile) as f:
    #print(f.read())


#形容詞分け
mecab = MeCab.Tagger("-Ochasen")

with open(dfile, 'r',) as f:

    reader = f.readline()
    while reader:
        #Mecabで形態素解析を実施
        node = mecab.parseToNode(reader)

        while node:
            word_type = node.feature.split(",")[0]

            #取得する単語は、"名詞", "動詞", "形容詞", "副詞"
            if word_type in ["名詞", "動詞", "形容詞", "副詞"]:

                words.append(node.surface)

            node = node.next

        reader = f.readline()

with open(hukusifile, mode='w') as f:     #ツイートをtxtに書きこみ
    f.write('\n'.join(words))

tx = (random.sample(words, 3))

for x in tx:
    t_text += x

print(t_text)

params = {"status" : t_text}
ress = twitter.post(url2, params = params) #post送信

if ress.status_code == 200: #正常投稿出来た場合
    print("Success.")
else: #正常投稿出来なかった場合
    print("Failed. : %d"% ress.status_code)
