import json #標準のjsonモジュールとconfig.pyの読み込み
import MeCab
import random

CK="###"
CS="###"
AT="###"
AS="###"
twitter = OAuth1Session(CK, CS, AT, AS) #認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
url2 ="https://api.twitter.com/1.1/statuses/update.json"

tweets_data =[]
word1=[] #単語リスト
word2=[]
zyosi=[]
zyodousi =[]
tx=[]
ty=[]
tz =[]
t_text=""
dfile = 'C:/Users/sake_/py/twi.txt'#tweetfile
hukusifile = 'C:/Users/sake_/py/twi_huku.txt'#hukusifile

params ={'count' : 10,'screen_name' : '###'} #取得数
res = twitter.get(url,params = params)


if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        tweets_data.append(line['text'])

else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)

with open(dfile, mode='w') as f:     #ツイートをtxtに書きこみ
   f.write('\n'.join(tweets_data))

with open(dfile) as f:
    print(f.read())


#形容詞分け
mecab = MeCab.Tagger("-Ochasen")

with open(dfile, 'r',) as f:

    reader = f.readline()
    while reader:
        #Mecabで形態素解析を実施
        node = mecab.parseToNode(reader)

        while node:
            word_type = node.feature.split(",")

            #取得する単語は、"
            if word_type[0] == "助詞":
                zyosi.append(node.surface)
            elif word_type[0] == "助動詞":
                zyodousi.append(node.surface)
            elif word_type[0] == "名詞" and word_type[1] == "一般":
                word1.append(node.surface)
            elif word_type[0] in ["名詞","動詞", "形容詞", "副詞"]:
                word2.append(node.surface)
                
            node = node.next

        reader = f.readline()


with open(hukusifile, mode='w') as f:     #ツイートをtxtに書きこみ
    f.write('\n'.join(words))

tx = (random.sample(word1, 1))    
tx_2 = (random.sample(word2, 1))  
ty = (random.sample(zyosi, 1))
tz = (random.sample(zyodousi, 1))
    
t_text = "".join(tx)+"".join(ty)+"".join(tx_2)+"".join(tz)

print(t_text)

params = {"status" : t_text}
ress = twitter.post(url2, params = params) #post送信

if ress.status_code == 200: #正常投稿出来た場合
    print("Success.")
else: #正常投稿出来なかった場合
    print("Failed. : %d"% ress.status_code)
