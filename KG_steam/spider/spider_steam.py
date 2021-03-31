# -*- coding: utf-8 -*-

# 爬取数据 数据格式为: 游戏名字符串 游戏类型列表 游戏logo图片

# 导入相应的包 requests和bs4可以简单的爬取相应的数据
import requests
from bs4 import BeautifulSoup

#设置page_num = 20，爬取steam上面最热门的500个游戏

def spider_steam():
    name_cnt = 1
    picture_cnt = 1
    for page_num in range(1, 7):
        # 对应的url链接
        url = "https://store.steampowered.com/search/?filter=globaltopsellers&page=" + str(page_num) + "&os=win"
        # 简单的设置一下http请求头，设置zh-CN
        head = {"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", 'user-agent': 'Mozilla/5.0'}
        # 生成对应的soup
        response = requests.get(url, headers = head)
        content = response.text
        soup = BeautifulSoup(content, 'lxml')
        # 生成游戏名称的taglist
        raw_games_name_list = soup.find_all('span', class_ = 'title')
        # 准备一个游戏对应的logo的list
        raw_games_img_url_list = []
        # 生成对应游戏logo图片的链接
        for e in soup.find_all('div', class_ = 'col search_capsule'):
            raw_games_img_url_list.append(e.img['src'])
        # 准备一个游戏主页面的内容list
        raw_games_content_url_list = []
        for e in soup.find('div', id = 'search_resultsRows').find_all('a'):
            raw_games_content_url_list.append(e['href'])
        # 进一步爬取content-url
        game_tag_list = []
        for content_url in raw_games_content_url_list:
            response1 = requests.get(content_url, headers = head)
            content1 = response1.text
            soup1 = BeautifulSoup(content1, 'lxml')
            # 得到游戏对应的类型
            tmp = []
            try:
                for e in soup1.find('div', class_ = 'glance_tags popular_tags').find_all('a'):
                    tmp.append(e.get_text().strip(' '))
                game_tag_list.append(''.join(tmp))
                print(content_url)
            except:
                game_tag_list.append(''.join(tmp))
                print('no game popular tag')
        # 写入数据 序号 游戏名称 游戏tag
        with open('raw_data/games_info.txt', 'a+') as f:
            for i in range(0, len(raw_games_name_list)):
                try:
                    f.write(str(name_cnt + 1) + ' ' + raw_games_name_list[i].get_text().strip(' ') + ' ' + game_tag_list[i] + '\n')
                    name_cnt += 1
                except:
                    f.write(str(name_cnt + 1) + " can not gdk\n")
                    name_cnt += 1
        # 创建对应的游戏logo图片
        for i in range(len(raw_games_img_url_list)):
            r = requests.get(raw_games_img_url_list[i])
            with open('raw_data/picture/' + str(picture_cnt + 1) + ".jpg", "wb") as f:
                f.write(r.content)
            picture_cnt += 1
if __name__ == '__main__':
    spider_steam()