# この表の上の線にマウスを合わせて、全体選択をします。
# このコードを、w20_kadai5_6.pyに保存してください。

# 必要な事前ファイル:
# ・特になし。

# 必要な3つのモジュールのインストール:
# pip install numpy --proxy http://cproxy.okinawa-ct.ac.jp:8080/
# pip install matplotlib --proxy http://cproxy.okinawa-ct.ac.jp:8080/
# pip install opencv-python --proxy http://cproxy.okinawa-ct.ac.jp:8080/

# 要求：
# １．#？___の部分は実行した結果（テキスト）をWordファイル貼ってください。
# 2．#[実行したスクリーンショット] の部分は、実行したスクリーンショットをWordファイル
# に貼って下さい。
#　3.空白___の部分を埋めて下さい。


import cv2
import numpy as np
import matplotlib.pyplot as plt


#######################################################
#例題1　画像のパターンを生成する。
h = 8
w = 7
img = np.zeros((h, w), np.uint8)
print("img.shape=",img.shape)
print("img.size=",img.size)
print("img.ndim=",img.ndim)
print(img)#____
    # [[0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]
    #  [0 0 0 0 0 0 0]]

'''
#img[row             , column         ]
#img[start:end:step  , start:end:step ]
img[    0 : 1 : 1    ,    2 : 4 : 1    ]=200
img[      : 3 : 1    ,    5 :   : 1    ]=128
print(img)#?____
    # [[  0   0 200 200   0 128 128]
    #  [  0   0   0   0   0 128 128]
    #  [  0   0   0   0   0 128 128]
    #  [  0   0   0   0   0   0   0]
    #  [  0   0   0   0   0   0   0]
    #  [  0   0   0   0   0   0   0]
    #  [  0   0   0   0   0   0   0]
    #  [  0   0   0   0   0   0   0]]

ax = plt.gca()#現在のaxesはgca(get current axesの略?)で取得できる。
ax.set_xticks(np.arange(-.5, img.shape[1], 1))
ax.set_yticks(np.arange(-.5, img.shape[0], 1))
ax.set_xticklabels(np.arange(0, img.shape[1]+1, 1))
ax.set_yticklabels(np.arange(0, img.shape[0]+1, 1))
ax.grid(color='red', linestyle='-', linewidth=1)

for r in range(h):
    for c in range(w):
        ax.text(c, r, str(img[r,c]), fontsize=14,ha="center", va="center", color="w")

plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()#display to window until click X to close.

#例題2
# Lの字をで100の明るさで書きなさい。(以下のパターンになるように！)

img = np.zeros((h, w), np.uint8)#clear to zeros
print(img)
img[    0 :   : 1    ,    0 : 1 : 1    ]=100
img[    7 : 8 : 1    ,    1 :   : 1    ]=100

#画像のパターン
print(img)
    # [[100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100   0   0   0   0   0   0]
    #  [100 100 100 100 100 100 100]]

ax = plt.gca()#現在のaxesはgca(get current axesの略?)で取得できる。
ax.set_xticks(np.arange(-.5, img.shape[1], 1))
ax.set_yticks(np.arange(-.5, img.shape[0], 1))
ax.set_xticklabels(np.arange(0, img.shape[1]+1, 1))
ax.set_yticklabels(np.arange(0, img.shape[0]+1, 1))
ax.grid(color='red', linestyle='-', linewidth=1)

for r in range(h):
    for c in range(w):
        ax.text(c, r, str(img[r,c]), fontsize=14,ha="center", va="center", color="w")

plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()#display to window until be closed.
'''
'''
#課題5
# 上記例題２のLを、太さ2ピクセル（画素）で160の明るさで書きなさい。(以下のパターンになるように！)
img = np.zeros((h, w), np.uint8)#clear to be zeros

img[0::,0:2:]=160
img[6::,2::]=160
#画像のパターン
print(img)
    # [[160   160   0   0   0   0   0]
    #  [160   160   0   0   0   0   0]
    #  [160   160   0   0   0   0   0]
    #  [160   160   0   0   0   0   0]
    #  [160   160   0   0   0   0   0]
    #  [160   160   0   0   0   0   0]
    #  [160   160 160 160 160 160 160]
    #  [160   160 160 160 160 160 160]]

ax = plt.gca()#現在のaxesはgca(get current axesの略?)で取得できる。
ax.set_xticks(np.arange(-.5, img.shape[1], 1))
ax.set_yticks(np.arange(-.5, img.shape[0], 1))
ax.set_xticklabels(np.arange(0, img.shape[1]+1, 1))
ax.set_yticklabels(np.arange(0, img.shape[0]+1, 1))
ax.grid(color='red', linestyle='-', linewidth=1)

for r in range(h):
    for c in range(w):
        ax.text(c, r, str(img[r,c]), fontsize=14,ha="center", va="center", color="w")

plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()#display to window until be closed.
'''

#課題6
# ラージMの字を120の明るさで書きなさい。(以下のパターンになるように！)
img = np.zeros((h, w), np.uint8)#clear to be zeros
print(img)
img[0::,:1:]=120
img[1:2:,1:6:4]=120
img[2:3:,2:5:2]=120
img[3:4:,3:4:] =120
img[0::,6::]=120
#画像のパターン
print(img)#____
    # [[120   0   0   0   0   0   120]
    #  [120   120 0   0   0   120 120]
    #  [120   0   120 0   120 0   120]
    #  [120   0   0   120 0   0   120]
    #  [120   0   0   0   0   0   120]
    #  [120   0   0   0   0   0   120]
    #  [120   0   0   0   0   0   120]
    #  [120   0   0   0   0   0   120]]

ax = plt.gca()#現在のaxesはgca(get current axesの略?)で取得できる。
ax.set_xticks(np.arange(-.5, img.shape[1], 1))
ax.set_yticks(np.arange(-.5, img.shape[0], 1))
ax.set_xticklabels(np.arange(0, img.shape[1]+1, 1))
ax.set_yticklabels(np.arange(0, img.shape[0]+1, 1))
ax.grid(color='red', linestyle='-', linewidth=1)

for r in range(h):
    for c in range(w):
        ax.text(c, r, str(img[r,c]), fontsize=14,ha="center", va="center", color="w")

plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()#display to window until be closed.
