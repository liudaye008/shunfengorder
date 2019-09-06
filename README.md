# shunfengorder
顺丰快递信息爬虫，一次输入20条订单号一起输出结果

### 输入
excel表格第一列的前20条输入有效订单号，就能够执行此程序

### 运行
python3 shunfeng.py

### 驱动插件  
chrome的webdriver： http://chromedriver.storage.googleapis.com/index.html  
Firefox驱动下载地址为：https://github.com/mozilla/geckodriver/releases/  

从网上下载对应版本的chromedriver之后，里面的内容仅为一个.exe文件，
将其解压在chrome的安装目录下(C:\Program Files (x86)\Google\Chrome\Application\)，然后再配置环境变量

1. 进入我的电脑->属性->高级系统设置->环境变量
2. 修改path在最后面添加 ;C:\Program Files (x86)\Google\Chrome\Application\
3. OK。安装与配置就到此结束。剩下的就是使用python来写代码了。

> 下载chromedriver的时候，一定要下载与你电脑上chrome版本相对应的版本。
