# この表の上の線にマウスを合わせて、全体選択をします。
# このコードを、kadai1.py等に保存してください。

# 必要な事前ファイル:
# 以下の画像ファイルをTeamsからDLし、
# ソースコードと同じフォルダに置いて下さい。
    # img-lena-gray-h256-w250.bmp
    # img_sora.jpg

# 必要な3つのモジュールのインストール:
    # pip install numpy --proxy http://cproxy.okinawa-ct.ac.jp:8080/
    # pip install matplotlib --proxy http://cproxy.okinawa-ct.ac.jp:8080/
    # pip install opencv-python --proxy http://cproxy.okinawa-ct.ac.jp:8080/

# 要求：
    # 1．#？___の部分は実行した結果（テキスト）をWordファイル貼ってください。
    # 2．#[実行したスクリーンショット] の部分は、
    # 実行したスクリーンショットをWordファイル貼って下さい。
    # 3. 空白 ____ の部分を埋めて下さい。


import cv2
import numpy as np
import matplotlib.pyplot as plt

fname1 = 'img-lena-gray-h256-w250.bmp'
print('Open file:', fname1)  #  img-lena-gray-h256-w250.bmp
img = plt.imread(fname1)  # 画像ファイルオープン
print(img.ndim)  # 2
print(img.shape)  # (256, 250)
print(img.shape[0])  #  256
print(img.shape[1])  # 250
print(img.shape[0] * img.shape[1])  # 64000
print(img.size)  #  64000

print(img)  # 実際の画像の2次元データです。...は省力の意味
    # [[162 162 162 ... 119 114 116]
    #  [162 162 162 ... 119 114 116]
    #  [162 162 159 ... 122 117 117]
    #  ...
    #  [ 48  57  52 ...  47  48  53]
    #  [ 46  50  50 ...  49  51  50]
    #  [ 44  55  54 ...  42  46  54]]

plt.imshow(img, cmap='gray', vmin=0, vmax=255,
           interpolation='none', aspect='equal')
print(fname1, 'の表示')  # img-lena-gray-h256-w250.bmp
plt.show()
