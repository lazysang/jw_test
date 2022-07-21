# 一、运行脚本
## 1.python环境
`python版本要求3.7+`

## 2.安装依赖
``` shell
pip install -r requirements.txt
```
## 3.下载浏览器驱动
Google浏览器驱动下载地址
http://chromedriver.storage.googleapis.com/index.html
根据浏览器版本下载对应版本的浏览器驱动存放到项目根目录

## 4.运行程序
``` shell
python run.py
```
# 二、脚本介绍
## 1.目录结构
``` text

platform-ui-test/
├── common/
├── modules/
├── reports/
├── scripts/
├── test_data/
├── test_dir/
└── run.py
```

- `common/`公共方法目录
- `modules/`模块目录，存放每个模块的方法
- `reports/`存放测试报告目录
- `scripts/`存放测试其他测试脚本
- `test_data/`测试数据目录
- `test_dir/`存放测试脚本目录
- `run.py`运行测试用例主文件