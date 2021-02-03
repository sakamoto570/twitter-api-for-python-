import serial
from time import sleep


def serial_com(flag):
    with serial.Serial("COM3",9600,timeout=1) as ser:

            # シリアル通信開始直後に送信するとエラーになるのでディレイさせる
            sleep(5)

            # Byte型に変換
            flag_byte = flag.to_bytes(1,"big")

            # 送信
            print("fi")
            ser.write(flag_byte)
            print("nish")


print("finish")
if __name__ == "__main__":
    serial_com()
