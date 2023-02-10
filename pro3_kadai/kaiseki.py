import requests
import bs4

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=91&block_no=47936&year=&month=&day=&view="

res = requests.get(url)

soup = bs4.BeautifulSoup(res.content, 'html.parser')

print(soup.select('table')[0])
