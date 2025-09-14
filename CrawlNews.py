"""网易新闻爬取-v1.0"""
# 导入所需库
import os  
import sys  
from pathlib import Path
from flask import Flask, jsonify,send_file
from flask_cors import CORS
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 初始化Flask应用
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 新闻爬虫类
class CrawlNews():
    def __init__(self,target_url: str = "https://news.163.com/"):
        self.target_url = target_url
    
    def OpenNewsWebsite(self):
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        edge_service = Service(executable_path="D:\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(
            service = edge_service,
            options = edge_options
        )
        driver.get(self.target_url)

        self.driver = driver

    def GetNews(self):
        self.driver.implicitly_wait(100)
        content = self.driver.find_elements(By.CSS_SELECTOR,"p,a")
        news = []
        for index in content:
            text = index.text.strip()
            if text and text not in news and len(text) >= 18:
                news.append(text)
            if len(news) == 10:
                break

        self.news = news

    def write_news(self):
        file_path = Path('News.txt')
        news_content = '\n'.join([f"{i+1}. {item}" for i, item in enumerate(self.news)])
        file_path.write_text(news_content, encoding='utf-8')

    def close(self):
        self.driver.quit()

# 新闻爬取接口
@app.route('/crawl_news',methods = ['GET'])
def crawl_news():
    try:
        bwc = CrawlNews()
        bwc.OpenNewsWebsite()
        bwc.GetNews()
        bwc.write_news()
        bwc.close() 

        return jsonify({
            'success':True,
            'message':'新闻爬取成功',
            'news':bwc.news
        })
    except Exception:
        traceback.print_exc()
        return jsonify({
            'success':False,
            'message':f'新闻爬取失败:{Exception}',
            'news':[]
        })
    
# 运行
if __name__ == "__main__":
    app.run(host = 'localhost',port = 5000,debug = True)