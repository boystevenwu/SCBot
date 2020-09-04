# SCBot
星际老男孩论坛自动化浏览工具


# Intro
main.py 运行后将打开登录界面，后转至论坛第一页\
程序通过预设的参数进行筛选，并会忽略已观看历史\
观看超过阈值或者有蓝色大V回复则会持续打开\
可以通过 addCard.py 添加这些 url 至历史中\
结束运行时会跳转回论坛第一页，默认使用 Chrome

# Usage
```python
python >= 3.5
import selenium
import json
```
操作系统：Windows 10 - 需自行下载 driver，macOS - brew cask install $driver，Linux - 尚未试验\
开源包未自带 Chromedriver，需自行下载或使用其他浏览器 driver\
发现 Chromedriver 必须和 Chrome 版本本体匹配，需要在安装时检查一下


# config.json
在 user_id 处输入论坛用户名，在 password 处输入登录密码\
\
初始筛选机制参数由上到下分别为：\
查询前两页的帖子\
观看数在3000以上\
并且超过15回复 或3点赞 或1收藏会开启并录入至历史\
观看数超过12000的帖子会持续开启

## License
[MIT](https://choosealicense.com/licenses/mit/)
