import matplotlib.pyplot as plt
import japanize_matplotlib

temp = dict(); months = list()
temp[2021] = [16.8,18.5,20.8,21.7,25.8,27.1,28.8,28.7,28.8,26.0,21.8,18.9]
temp[2020] = [18.7,18.7,20.1,19.8,24.8,28.1,29.3,29.4,27.7,25.8,23.4,19.2]
temp[2019] = [18.1,20.0,19.9,22.3,24.2,26.5,28.9,29.2,28.0,26.0,23.1,20.0]
temp[2018] = [17.2,16.9,19.9,21.6,25.6,27.8,28.3,28.5,28.4,23.9,23.1,20.4]
temp[2017] = [18.4,17.1,18.3,21.6,24.2,26.6,29.9,30.4,28.9,27.0,22.8,18.0]

for i in range(1,13):
    months.append("%d月" % i)

# plotを重ねて呼び出すことも可能
plt.plot(months,temp[2017])
plt.plot(months,temp[2018])
plt.plot(months,temp[2019])
plt.plot(months,temp[2020])
plt.plot(months,temp[2021])


# 見た目を整える
plt.title("沖縄の月別平均気温")
plt.xlabel('月'); plt.ylabel('気温[℃]')
plt.legend(["2017年","2018年","2019年","2020年","2021年"])
plt.axis(xmin=-0.5,xmax=11.5,ymin=0,ymax=35)
plt.grid()
plt.savefig("temp.svg")
plt.show()