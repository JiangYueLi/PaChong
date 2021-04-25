import os
import requests
import re

start_url = "http://www.kanunu8.com/book3/6879/"
content = requests.get(start_url).content.decode('GB2312')

def get_toc(content):
    toc_url_list = []
    toc_block =re.findall('正文(.*?)</tbody>',content,re.S)[0]
    toc_url = re.findall('href="(.*?)"',toc_block,re.S)
    for url in toc_url:
        toc_url_list.append(start_url+url)
    return toc_url_list

def get_article(html):
    chapter_name = re.findall('size="4">(.*?)<',html,re.S)[0]
    text_block = re.findall('<p>(.*?)</p>',html,re.S)[0]
    text_block = text_block.replace('<br />','')
    return chapter_name,text_block

def save(chapter,article):
    os.makedirs('动物农场',exist_ok=True)
    with open(os.path.join('动物农场',chapter+'.txt'),'w',encoding='utf-8') as f:
        f.write(article)

if __name__ == '__main__':
   for html in get_toc(content):
       content1 = requests.get(html).content.decode('GB2312')
       chapter1,article1 = get_article(content1)
       save(chapter1,article1)
