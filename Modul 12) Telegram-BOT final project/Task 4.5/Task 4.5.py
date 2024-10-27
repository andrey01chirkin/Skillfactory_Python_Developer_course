import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
tree = lxml.html.document_fromstring(html)
ul = tree.findall('.//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <a>)
    date = li.find('time')
    print(date.get('datetime')[:10], a.text)  # из этого тега забираем текст, это и будет нашим названием