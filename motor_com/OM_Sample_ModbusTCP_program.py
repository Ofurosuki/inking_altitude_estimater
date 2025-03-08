from ctypes import BigEndianStructure
import socket
import array
import time
import sys
from socket import inet_aton
import param



def decimal_to_hexadecimal(value):
    byte_array = value.to_bytes(4, byteorder='big')
    print(hex(byte_array[0]))
    print(hex(byte_array[1]))
    print(hex(byte_array[2]))
    print(hex(byte_array[3]))
    return byte_array
    

def main():
    # トランザクションID用カウンタ
    # [pos_0,pos_1,pos_2,pos_3]=decimal_to_hexadecimal(8500)
    # print(pos_0)
    # print(pos_1)
    # print(hex(pos_2))
    # print(hex(pos_3))
    # return
    pos_0=0x00
    pos_1=0x00
    pos_2=0x00
    pos_3=0x00
    val = 0

    # IPアドレス
    address = "192.168.1.20"

    # ポート番号
    port = 502

    # バッファサイズ
    BUFSIZE = 4096

    # リモートI/O(R-OUT)から28レジスタの値を取得するクエリ
    frm_Mon =   [   
                    0x00, 0x00,             # プロトコルID :0x0000
                    0x00, 0x06,             # 伝文長 :6 byte
                    0x00,                   # ユニットID :0
                    0x03,                   # FUNCTION CODE:0x03
                    0x01, 0x1C,             # レジスタアドレス:0x011C(リモートI/O R-OUT ~)
                    0x00, 0x1C              # 読み出し数 :28
                ]           
    
    # 運転データの位置を書き換えるクエリ
    frm_WrOpeData_Pos = [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O（IN）
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x01,         # ライトリクエスト   0x0001 (書き込み要求)
                            0x0C, 0x01,         # ライトパラメータID 0x0C01 (運転データ No.0 位置)
                            0x03, 0xE8,         # ライトデータ(下位) 1000 Step
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    # ライトリクエストをOFFするクエリ
    frm_WrOpeData_Pos_WrRqoff = [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O（IN）
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト   0x0000
                            0x0C, 0x01,         # ライトパラメータID 0x0C01 (運転データ No.0 位置)
                            0x27, 0x10,         # ライトデータ(下位) 1000 Step
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    # 運転データの速度を書き換えるクエリ
    frm_WrOpeData_Spd = [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O（IN）
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x01,         # ライトリクエスト   0x0001 (書き込み要求)
                            0x0C, 0x02,         # ライトパラメータID 0x0C02 (運転データ No.0 速度)
                            0x00, 0x64,         # ライトデータ(下位) 100 Hz
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    # ライトリクエストをOFFするクエリ
    frm_WrOpeData_Spd_WrRqoff = [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O（IN）
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト   0x0000 
                            0x0C, 0x02,         # ライトパラメータID 0x0C02 (運転データ No.0 速度)
                            0x00, 0x64,         # ライトデータ(下位) 100 Hz
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    # 固定 IO の START を ON するクエリ
    frm_FixedIn_Start =     [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x08,         # 固定I/O（IN）START ON
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト
                            0x00, 0x00,         # ライトパラメータID
                            0x00, 0x00,         # ライトデータ(下位)
                            0x00, 0x00          # ライトデータ(上位)
                        ]
    
    
    # 固定 IO の START を OFF するクエリ
    frm_FixedIn_Stop =     [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数 :40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O（IN）START OFF
                            0x00, 0x00,         # ダイレクトデータ運転　運転方式
                            0x00, 0x00,         # ダイレクトデータ運転　位置（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　位置（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　速度（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（下位）
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート（上位）
                            0x00, 0x00,         # ダイレクトデータ運転　運転電流
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト
                            0x00, 0x00,         # ライトパラメータID
                            0x00, 0x00,         # ライトデータ(下位)
                            0x00, 0x00          # ライトデータ(上位)
                        ]
    
    # ダイレクトデータ運転を実行するクエリ
    frm_ExeOpe =        [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数:40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x01, 0x00,         # 固定I/O (IN) TRIG ON
                            0x00, 0x01,         # ダイレクトデータ運転　運転方式                :2 相対位置決め（指令位置基準）#modified 0x02 to 0x01
                            pos_2, pos_3,         # ダイレクトデータ運転　位置 (下位)             :8500 step  0x2134
                            #0x27, 0x20,
                            pos_0, pos_1,         # ダイレクトデータ運転　位置 (上位)
                            #0x05, 0xDC,         # ダイレクトデータ運転　速度 (下位)             :2000 Hz
                            0x86,0xA0,
                            0x00, 0x01,         # ダイレクトデータ運転　速度 (上位)
                            0x07, 0xD0,         # ダイレクトデータ運転　起動・変速レート (下位)  :1.5 kHz/s
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート (上位)
                            0x05, 0xDC,         # ダイレクトデータ運転　停止レート (下位)       :1.5 kHz/s
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート (上位)
                            0x03, 0xE8,         # ダイレクトデータ運転　運転電流                :100.0 %
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト
                            0x00, 0x00,         # ライトパラメータID
                            0x00, 0x00,         # ライトデータ(下位)
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    # ダイレクトデータ運転のトリガをOFFするクエリ
    frm_ExeOpe_TrgOFF =        [
                            0x00, 0x00,         # プロトコルID :0x0000
                            0x00, 0x2F,         # 伝文長 :47 byte
                            0x00,               # ユニットID :0
                            0x10,               # FUNCTION CODE:0x10
                            0x01, 0x04,         # レジスタアドレス:0x0104 (リモートI/O R-IN ~)
                            0x00, 0x14,         # 書き込みレジスタ数 :20
                            0x28,               # バイト数:40
                            0x00, 0x00,         # リモートI/O
                            0x00, 0x00,         # 運転データNoの選択
                            0x00, 0x00,         # 固定I/O (IN) TRIG OFF
                            0x00, 0x01,         # ダイレクトデータ運転　運転方式                :2 相対位置決め（指令位置基準）
                            pos_2, pos_3,         # ダイレクトデータ運転　位置 (下位)             :8500 step  0x2134
                            pos_0, pos_1,         # ダイレクトデータ運転　位置 (上位)
                            0x05, 0xDC,         # ダイレクトデータ運転　速度 (下位)             :2000 Hz
                            0x00, 0x00,         # ダイレクトデータ運転　速度 (上位)
                            0x07, 0xD0,         # ダイレクトデータ運転　起動・変速レート (下位)  :1.5 kHz/s
                            0x00, 0x00,         # ダイレクトデータ運転　起動・変速レート (上位)
                            0x05, 0xDC,         # ダイレクトデータ運転　停止レート (下位)       :1.5 kHz/s
                            0x00, 0x00,         # ダイレクトデータ運転　停止レート (上位)
                            0x03, 0xE8,         # ダイレクトデータ運転　運転電流                :100.0 %
                            0x00, 0x00,         # ダイレクトデータ運転　転送先
                            0x00, 0x00,         # 予約(reserved)
                            0x00, 0x00,         # リードパラメータID
                            0x00, 0x00,         # ライトリクエスト
                            0x00, 0x00,         # ライトパラメータID
                            0x00, 0x00,         # ライトデータ(下位)
                            0x00, 0x00          # ライトデータ(上位)
                        ]

    print("***************************************")
    print("* Modbus TCP sample program for AZ series *")
    print("* Python *")
    print("* *")
    print("***************************************")
    print("\nDriver IP Address >" + address)
    print("\nDriver Port >" + str(port))

    # ソケット
    client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #TCP/IP
    
    # client  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #UDP/IP

    # タイムアウトを設定
    client.settimeout(5)

    # ドライバと接続
    try:
        client.connect((address, int(port)))
        
    except OSError as msg:
        client.close()
        client = None

    # 接続失敗時は終了
    if client is None:
        print("could not open socket.")
        print("  IPAddress: " + address)
        print("  Port: " + str(port))
        input()
        sys.exit()

    frm_count = 0

    # 'q'または'Q'が入力されるまでループ
    while True:

        frm_count_array = frm_count.to_bytes(2, "big")
        wkfrm = array.array('B', [])
        wkfrm.extend(frm_count_array)
        wkfrm.extend(frm_Mon)

        # クエリ送信
        client.sendto(wkfrm,(address,port))
        rcvData  = client.recv(BUFSIZE)
        #print(rcvData)
        
        feedbackPos = int.from_bytes(array.array('B', [rcvData[19], rcvData[20], rcvData[17], rcvData[18] ]), byteorder='big', signed=True)
        #print("Position:",feedbackPos)
        
        print("\n")
        print("1:Monitor")
        print("2:Set Operation Data")
        print("3:Operate")
        print("4:Execute Direct Data Operation(Absolute)")
        print("5:Execute Direct Data Operation (Relative)")
        print("Q:Quit program")
        print(f"Current Position: {feedbackPos}")
        val = input()


        # Program Stop
        if val =='q' or val =='Q':
            break

        # モーターの検出位置を読み出し、ターミナルに表示する
        elif val == '1':
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_Mon)

            # クエリ送信
            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            #print(rcvData)
            
            feedbackPos = int.from_bytes(array.array('B', [rcvData[19], rcvData[20], rcvData[17], rcvData[18] ]), byteorder='big', signed=True)
            print("Position:",feedbackPos)
            frm_count += 1

        # 運転データ No.0 の位置、速度を書き換え
        elif val == '2':
            # 運転データ No.0 の位置 
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_WrOpeData_Pos)

            # クエリ送信
            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1
            time.sleep(0.1)

            # ライトリクエストをOFFする
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_WrOpeData_Pos_WrRqoff)

            # クエリ送信
            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1            
            time.sleep(0.1)

            # 運転データ No.0 の速度 
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_WrOpeData_Spd)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1
            time.sleep(0.1)

            # ライトリクエストをOFFする
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_WrOpeData_Spd_WrRqoff)

            # クエリ送信
            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1


        # 固定 IO の START を ON する
        elif val == '3':
            # 固定 IO の START を ON するクエリ
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_FixedIn_Start)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1
            time.sleep(0.1)
            
            # 固定 IO の START を OFF するクエリ
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_FixedIn_Stop)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1

        # ダイレクトデータ運転を実行する
        elif val == '4':
            print(f"input step number(absolute) between {param.lower_lim} and {param.upper_lim}")
            step = input()
            if int(step)<param.lower_lim or int(step)>param.upper_lim:
                print("\x1b[41mInput value is out of range \x1b[49m")
                continue
            
            # ダイレクトデータ運転を実行するクエリ
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            pos_0, pos_1,pos_2,pos_3 = decimal_to_hexadecimal(int(step))
            print("pos:",step)
            frm_ExeOpe[19]=pos_2
            frm_ExeOpe[20]=pos_3
            frm_ExeOpe[21]=pos_0
            frm_ExeOpe[22]=pos_1
            wkfrm.extend(frm_ExeOpe)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1
            time.sleep(0.1)

            # ダイレクトデータ運転のトリガをOFFするクエリ
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_ExeOpe_TrgOFF)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)

           # print(rcvData)
           # print("rcvData[0]:",rcvData[7])
            frm_count += 1
        elif val == '5':
            while True:
                print("input step number(relative)")
                step = input()
                frm_count_array = frm_count.to_bytes(2, "big")
                wkfrm = array.array('B', [])
                wkfrm.extend(frm_count_array)
                wkfrm.extend(frm_Mon)

                # クエリ送信
                client.sendto(wkfrm,(address,port))
                rcvData  = client.recv(BUFSIZE)
                #print(rcvData)
                
                feedbackPos = int.from_bytes(array.array('B', [rcvData[19], rcvData[20], rcvData[17], rcvData[18] ]), byteorder='big', signed=True)
                if(feedbackPos+int(step)>param.lower_lim and feedbackPos+int(step)<param.upper_lim):
                    break
                else:
                    print("\x1b[41mInput value is out of range \x1b[49m")
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            pos_0, pos_1,pos_2,pos_3 = decimal_to_hexadecimal(feedbackPos+int(step))
            print(f"target pos:{feedbackPos+int(step)}")
            #continue
            #print("pos:",step)
            frm_ExeOpe[19]=pos_2
            frm_ExeOpe[20]=pos_3
            frm_ExeOpe[21]=pos_0
            frm_ExeOpe[22]=pos_1
            wkfrm.extend(frm_ExeOpe)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)
            print(rcvData)
            frm_count += 1
            time.sleep(0.1)

            # ダイレクトデータ運転のトリガをOFFするクエリ
            # 送信用のクエリ作成
            frm_count_array = frm_count.to_bytes(2, "big")
            wkfrm = array.array('B', [])
            wkfrm.extend(frm_count_array)
            wkfrm.extend(frm_ExeOpe_TrgOFF)

            client.sendto(wkfrm,(address,port))
            rcvData  = client.recv(BUFSIZE)

           # print(rcvData)
           # print("rcvData[0]:",rcvData[7])
            frm_count += 1
            

        else:
            continue

        if frm_count > 65535:
            frm_count = 0

    client.close()
    
if __name__=="__main__":
    main()