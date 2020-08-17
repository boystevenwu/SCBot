# SCBot
星际老男孩论坛自动化浏览工具


# Intro
main.py 运行后将打开登录界面，后转至论坛第一页\
程序通过预设的参数进行筛选，并会忽略已观看历史\
观看超过阈值或者有蓝色大V回复则会持续打开\
可以通过 addCard.py 添加这些 url 至历史中\
结束运行时会跳转回论坛第一页

# Usage
```python
python >= 3.5
import selenium
import json
```
操作系统：Windows 10 - 原生环境，macOS - 需自行下载driver，Linux - 尚未试验\
开源包会自带 Chromedriver，可自行调整至新版本或其他浏览器driver


# config.json
在user_id处输入论坛用户名，在password处输入登录密码\
\
初始筛选机制参数由上到下分别为：\
查询前两页的帖子\
观看数在3000以上\
并且超过15回复 或3点赞 或1收藏会开启并录入至历史\
观看数超过12000的帖子会持续开启

## License
[MIT](https://choosealicense.com/licenses/mit/)
