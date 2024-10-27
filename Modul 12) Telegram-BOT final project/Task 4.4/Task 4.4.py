import lxml.html
from lxml import etree

tree = etree.parse('index.html', lxml.html.HTMLParser())
title = tree.xpath('/html/body/tag1/tag2/text()')  # забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке, её название и инструкции по отображению в браузере)

print(title)  # выводим полученный заголовок страницы


