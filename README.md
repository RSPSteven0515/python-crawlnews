# Python CrawlNews
## Python 新闻爬虫
---
## 简介
- 这是一个完全由Python开发的轻量级网络爬虫项目。
- 主要功能就是使用Python调用Edge浏览器，进行对（https://news.163.com/）[网易新闻]的新闻标题爬虫，并返还10条新闻标题。
## 使用方法
1. 将所有项目文件下载到您的电脑本地磁盘中（建议使用D盘）
2. 创建一个专门储存这些文件的文件夹（**必做**）
3. 创建一个src文件夹，用来储存主文件CrawlNews.py（**推荐**）
4. 其余文件均储存在项目根目录即可
5. 确保您电脑的5000端口是可用且开放的
6. 查看您的Edge浏览器版本（在浏览器输入“edge://version/”）
7. 到（https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/?form=MA13LH）[微软官方Edge驱动下载页]下载您的Edge对应版本驱动
8. 把下载完成的.zip压缩包解压到D盘根目录，默认解压后的Edge驱动目录应该是D:\edgedriver_win64
9. 驱动解压完成以后，即可进入您的IDE（推荐使用VS Code），按照requirements.txt里所需的依赖，创建虚拟环境（.venv）
10. 虚拟环境创建完成以后，即可运行Python主文件（**CrawlNews.py**）
11. 运行完成以后，在浏览器，访问**https://localhost:5000/crawl_news/**
12. 稍等片刻，当弹出爬取成功的json信息后，回到项目根目录，查看News.txt，即可查看到爬取下来的当日网易新闻10条新闻标题。
## Python 版本
- 本项目使用的Python版本是Python3.13.7，如果您使用的Python版本与本项目不同，可前往（https://python.org/）[Python官网]，安装3.13.7版本解释器
## 开发人员
- 本项目由雷影编程RSP开发
- 项目的优化和更新由北京野猫（RSPSteven0515）负责
- 特别鸣谢雷影编程RSP成员yly0012166给予的大力支持！
