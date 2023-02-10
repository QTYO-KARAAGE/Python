# この表の上の線にマウスを合わせて、全体選択をします。
# このコードを、w20_kadai2.pyに保存してください。

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

# open the next file
fname2 = 'img_sora.jpg'
print('Open file:', fname2)  # img_sora.jpg
img = plt.imread(fname2)  # 画像ファイルオープン
print(img.ndim)  # 3
print(img.shape)  #  (960, 1706, 3)
print(img.shape[0])  # 960
print(img.shape[1])  # 1706
print(img.shape[2])  # 3
print(img.shape[0] * img.shape[1] * img.shape[2])  # 4913280
print(img.size)  #  4913280

print(img)  # 実際の画像の3次元データです。...は省力の意味
    # [[[75 66 61]
    #   [76 67 62]
    #   [78 69 64]
    #   ...
    #   [68 56 44]
    #   [64 52 40]
    #   [64 52 40]]
    #
    #  [[83 76 70]
    #   [84 77 71]
    #   [85 78 72]
    #   ...
    #   [67 55 43]
    #   [66 54 42]
    #   [66 54 42]]
    #
    #  [[78 75 70]
    #   [77 74 69]
    #   [76 73 68]
    #   ...
    #   [64 52 40]
    #   [67 55 43]
    #   [67 55 43]]
    #
    #  ...
    #
    #  [[ 6  6  6]
    #   [ 6  6  6]
    #   [ 7  7  7]
    #   ...
    #   [ 7  7  7]
    #   [ 6  6  6]
    #   [ 6  6  6]]
    #
    #  [[ 6  6  6]
    #   [ 6  6  6]
    #   [ 6  6  6]
    #   ...
    #   [ 7  7  7]
    #   [ 7  7  7]
    #   [ 7  7  7]]
    #
    #  [[ 6  6  6]
    #   [ 6  6  6]
    #   [ 6  6  6]
    #   ...
    #   [ 7  7  7]
    #   [ 8  8  8]
    #   [ 8  8  8]]]


plt.imshow(img, cmap='gray', vmin=0, vmax=255,
           interpolation='none', aspect='equal')
print(fname2, 'の表示')  # img_sora.jpg
plt.show()

print("\n\n\n")
print("カラーをグレイスケールに変換")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)  # (960, 1706)
print(img.ndim)  # 2
print(img.shape[0])  # 960
print(img.shape[1])  # 1706
print(img.shape[0] * img.shape[1])  # 1637760
print(img.size)  #  1637760

print(img)  # 実際の画像の2次元データです。...は省力の意味
    # [[66 67 69 ... 54 50 50]
    #  [75 76 77 ... 53 52 52]
    #  [74 73 72 ... 50 53 53]
    #  ...
    #  [ 6  6  7 ...  7  6  6]
    #  [ 6  6  6 ...  7  7  7]
    #  [ 6  6  6 ...  7  8  8]]

plt.imshow(img, cmap='gray', vmin=0, vmax=255,
           interpolation='none', aspect='equal')
print(fname2, 'のグレイスケールの表示')  #  img_sora.jpg
plt.show()
