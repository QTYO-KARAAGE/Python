import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib

wb = openpyxl.load_workbook("陽性者数.xlsx")
sheet = wb["陽性者数(2021)"]

result = list()
count = 0

for i in range (1, 223):
    count = count + sheet.cell(row = i, column = 2).value
    result.append(count)

plt.plot(result)
plt.title("2021年4月1日から11月8日までの累計陽性者の推移")
plt.xlabel('日付')
plt.ylabel('陽性者数[人]')
plt.xticks([0, 30, 61, 91, 122, 153, 183, 221], ['4/1', '5/1', '6/1', '7/1', '8/1', '9/1', '10/1', '11/8'])
plt.grid()
plt.savefig('covid_2021_4_1_to_2021_11_8_count.svg')
plt.show()

wb.close()