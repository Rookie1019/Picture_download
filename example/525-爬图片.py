import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://tuchong.com/3418361/19652941/#image413925555"
headers = {
    "User-Agent":UserAgent().random
}

response = requests.get(url,headers=headers)
e = etree.HTML(response.text)
i = 0
img_urls = e.xpath('//article/img/@src')
for img_url in img_urls:
    response1 = requests.get(img_url,headers=headers)
    suffix = img_url.split('.')[-1]
    i += 1
    filename = '第'+str(i)+'页'+'.'+suffix

    with open(filename,'wb') as f:
        f.write(response1.content)
        print(filename+'正在下载')

