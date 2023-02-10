# この表の上の線にマウスを合わせて、全体選択をします。
# このコードを、kadaiXX.py等に保存してください。

# 指示:
# 以下の画像ファイルをTeamsからDLし、ソースコードと同じフォルダに置いて下さい。
# img-lena-gray-h256-w250.bmp
# img_sora.jpg

# 必要な3つのモジュールのインストール:
# pip install numpy --proxy http://cproxy.okinawa-ct.ac.jp:8080/
# pip install matplotlib --proxy http://cproxy.okinawa-ct.ac.jp:8080/
# pip install opencv-python --proxy http://cproxy.okinawa-ct.ac.jp:8080/

# 要求：
# １．#？___の部分は実行した結果（テキスト）をWordファイル貼ってください。
# 2．#[実行したスクリーンショット] の部分は、実行したスクリーンショットをWordファイル
# に貼って下さい。
# 　3.空白___の部分を埋めて下さい。
import cv2
import numpy as np
import matplotlib.pyplot as plt


fname1='img-lena-gray-h256-w250.bmp'
print('Open file:', fname1)#img-lena-gray-h256-w250.bmp
img = plt.imread(fname1)#画像ファイルオープン
'''
#例題1
roi=img[0:101:1,0:101:1] #h(0-to-100)-w(0-to-100) step by 1
plt.imshow(roi, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none',aspect='equal')
print('行0から100まで、列0から100までの範囲の画像表示')
result = cv2.imwrite('img-lena-gray-h(0-100)-w(0-100).bmp',roi)
plt.show()

roi=img[100::1,200::1] #h(100-to-end)-w(200-to-end) step by 1
plt.imshow(roi, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none',aspect='equal')
print('行100から終わりまで、列200から終わりまでの範囲の画像表示')
result = cv2.imwrite('img-lena-gray-h(100-end)-w(200-end).bmp',roi)
plt.show()

#例題3
#256//2 = 128 (integer)
#XXX//2 means that XXX divide by 2, then get only integer part
roi=img[256//2-10:256//2+10:1,::1] #h(118-to-138)-w(0-to-end) step by 1
plt.imshow(roi, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none',aspect='equal')
print('行118から137まで、列0から終わりまでの範囲の画像表示')
result = cv2.imwrite('img-lena-gray-h(118-138)-w(0-end).bmp',roi)
plt.show()
'''
#課題3
roi=img[0::,0:200:] #h(0-to-end)-w(0-to-199) step by 1
plt.imshow(roi, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none',aspect='equal')
print('行0から終わりまで、列0から199までの範囲の画像表示')
result = cv2.imwrite('img-lena-gray-h(0-end)-w(0-199).bmp',roi)
plt.show()

#課題4
h=img.shape[0]
print("h=",h)#?_____
w=img.shape[1]
print("w=",w)#?_____

#XXX//2 means that XXX divide by 2, then get only integer part
roi=img[h//2::,0:w//2-1:] #h(h//2-to-end)-w(0-to-w//2) step by 1
plt.imshow(roi, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none',aspect='equal')
print('行h//2から終わりまで、列0からw//2-1までの範囲の画像表示')
result = cv2.imwrite('img-lena-gray-h(h／2-end)-w(0-w／2).bmp',roi)
plt.show()

