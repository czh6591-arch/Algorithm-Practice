# 在线算法练习平台

一个基于 FastAPI + SQLite 的在线算法练习平台，支持用户注册登录、头像上传、OCR文字识别、代码提交和复杂度分析等功能。

## 功能特性

### 用户系统
- 用户注册/登录功能
- 密码长度至少8位校验
- 支持自定义个人头像（尺寸要求 >= 64x64，自动压缩至64x64）
- 支持通过图片OCR识别更新个人简介（支持常用汉字、英文、数字、标点）
- 支持直接文字输入更新个人简介

### 算法练习题
- **必须登录才能进入练习**，未登录用户只能查看题目列表，无法查看题目详情和提交代码
- 题目分为简单、中等、困难三个难度级别
- 每个难度级别至少3道题目（共9道）
- 题目详情包含：题目描述、输入输出格式、示例、数据范围
- 中等和困难题目额外展示算法复杂度要求
- 支持Python3代码提交和测试
- 每道题包含至少4个短测试用例和2个长测试用例
- 实时显示测试结果和错误信息
- 自动算法复杂度分析
- 如果复杂度过高，显示警告提示
- 实时显示每道题的通过率

### 算法教程
- 排序算法栏目：快速排序、归并排序、堆排序、插入排序
- 数据结构栏目：二叉搜索树、哈希表、图的表示、栈和队列
- 进阶算法栏目：动态规划入门、贪心算法、图论算法、字符串匹配
- 每个专栏包含标题、正文和视频引用

## 技术栈

- **后端框架**: FastAPI
- **数据库**: SQLite
- **前端**: HTML + CSS + JavaScript
- **代码执行**: Python subprocess
- **图片处理**: Pillow
- **OCR识别**: pytesseract
- **认证**: JWT + OAuth2

## 快速开始

### 环境要求

- Python 3.8+
- pip 包管理器

### 安装步骤

1. 克隆项目到本地

2. 安装依赖
```bash
cd 1-仓库初始模板
pip install -r requirements.txt
```

3. 安装 Tesseract OCR（用于图片文字识别）
- Windows: 下载安装 [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- macOS: `brew install tesseract`
- Linux: `sudo apt-get install tesseract-ocr`

4. 运行服务
```bash
python -m app.main
```

5. 访问网站
打开浏览器访问 `http://localhost:8000`

## API 接口

### 用户认证
- `POST /register` - 用户注册
- `POST /token` - 用户登录
- `GET /users/me` - 获取当前用户信息

### 用户管理
- `PUT /users/avatar` - 上传头像
- `PUT /users/bio` - 通过图片OCR更新简介
- `PUT /users/bio/text` - 通过文字更新简介

### 题目管理
- `GET /problems` - 获取题目列表
- `GET /problems/{id}` - 获取题目详情
- `POST /problems/{id}/submit` - 提交代码

### 教程管理
- `GET /tutorials` - 获取教程列表
- `GET /tutorials/{id}` - 获取教程详情

## 项目结构

```
app/
├── __init__.py
├── main.py          # 主应用入口
├── database.py      # 数据库操作
├── models.py        # 数据模型
├── security.py      # 安全认证
├── ocr.py           # OCR文字识别
├── code_executor.py # 代码执行和复杂度分析
├── init_data.py     # 初始化数据
├── routers/         # API路由
│   ├── auth.py
│   ├── users.py
│   ├── problems.py
│   └── tutorials.py
├── templates/       # HTML模板
│   ├── index.html
│   ├── problem.html
│   ├── profile.html
│   └── tutorials.html
└── static/          # 静态资源
    └── avatars/     # 头像存储
```

## 使用说明

1. **注册账户**: 点击右上角"注册"按钮，输入用户名、邮箱和密码（至少8位）
2. **登录**: 使用注册的账户登录系统
3. **浏览题目**: 在首页查看所有算法题目，可按难度筛选
4. **做题**: 点击题目进入详情页，编写Python代码并提交
5. **查看结果**: 提交后显示测试用例通过情况和复杂度分析结果
6. **更新个人信息**: 进入个人中心，上传头像或更新简介
7. **学习教程**: 在算法教程板块学习各种算法知识

## 注意事项

- 代码执行有5秒超时限制
- 头像图片尺寸需大于等于64x64
- OCR识别支持简体中文、繁体中文、英文、数字和常见标点
- 测试用例分为短测试用例（<10%上界）和长测试用例（>75%上界）