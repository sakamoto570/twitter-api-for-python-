
# import
import get_tweetid_module
import get_user_timeline_module
import serial_module
from time import sleep

# TwitterAPIに必要なCK,CS,AT,ASを設定
# 同時にTwitterアカウントも指定
CK = "#####"                                    # Consumer Key
CS = "######"                                   # Consumer Secret
AT = "########"                                 # Access Token
AS = "######"                                   # Accesss Token Secert
ID = "#######"                                  # ID

# 取得したツイート格納用配列の定義
timeline = []

# 最終ツイートのIDを取得する
since_id = get_tweetid_module.get_tweetID(CK, CS, AT, AS, ID)
flag = 3
while True:

    # API制限回避用にディレイを入れる
    sleep(30)

    # since_id以降のツイートを取得してtimelineに格納
    timeline = get_user_timeline_module.get_user_timeline(CK, CS, AT, AS, ID, since_id)

    # timelineから指定文字列を検索
    # 検索結果に応じてArduinoにシリアル通信
    # ACオン
    for i in timeline:
        if "on" in i:
            flag = 1
            serial_module.serial_com(flag)
            print("bbb")
            break

    # ACオフ
    for i in timeline:
        if "off" in i:
            flag = 0
            serial_module.serial_com(flag)
            print("aaa")
            break

    # プログラム停止
    for i in timeline:
        if "stop" in i:
            flag = -1
            break

    if flag == -1:
        break

    # 最終ツイートのIDを更新
    since_id = get_tweetid_module.get_tweetID(CK, CS, AT, AS, ID)

    # timelineを初期化
    timeline.clear()
