import qrcode                                   #ライブラリのインポート
img = qrcode.make('https://www.yahoo.co.jp/')   #QRコードの作成
img.save('qrcode.png')                          #画像の保存

