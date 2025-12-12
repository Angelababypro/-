# 使用指南 / Usage Guide

## 快速开始 / Quick Start

### 1. 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 运行应用 / Run Application

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，地址为：`http://localhost:8501`

The application will open automatically in your browser at: `http://localhost:8501`

## 功能说明 / Features

### 📊 数据概览 / Data Overview

显示课程统计信息和可视化图表：
- 课程总数、总容量、报名人数
- 院系课程分布饼图
- 课程类型分布柱状图
- 课程报名情况对比

Shows course statistics and visualization charts:
- Total courses, capacity, enrollment
- Department distribution pie chart
- Course type distribution bar chart
- Enrollment comparison

### 📋 课程列表 / Course List

浏览所有课程的详细信息：
- 课程基本信息表格
- 支持按院系、学期、课程类型筛选
- 查看课程详细信息

Browse all course details:
- Course information table
- Filter by department, semester, course type
- View detailed course information

### 🔍 课程搜索 / Course Search

搜索和筛选课程：
- 关键词搜索（课程名称、代码、教师）
- 多条件组合筛选
- 实时搜索结果

Search and filter courses:
- Keyword search (name, code, instructor)
- Multiple filter conditions
- Real-time search results

## 数据源配置 / Data Source Configuration

### 当前状态 / Current Status

系统当前使用 `sample_data.py` 中的示例数据。

The system currently uses sample data from `sample_data.py`.

### 连接本地数据库 / Connect to Local Database

要连接本地数据库，请修改 `data_loader.py`：

To connect to a local database, modify `data_loader.py`:

#### SQLite 示例 / SQLite Example

```python
import sqlite3

class DataLoader:
    def __init__(self):
        self.conn = sqlite3.connect('courses.db')
        self.cursor = self.conn.cursor()
    
    def get_all_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        rows = self.cursor.fetchall()
        return [self._row_to_course(row) for row in rows]
```

#### MySQL 示例 / MySQL Example

```python
import mysql.connector

class DataLoader:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="courses_db"
        )
```

### 数据库表结构 / Database Schema

参考 `database_schema.sql` 文件查看完整的数据库表结构。

Refer to `database_schema.sql` for the complete database schema.

## 配置选项 / Configuration Options

### 端口配置 / Port Configuration

```bash
streamlit run app.py --server.port 8502
```

### 远程访问 / Remote Access

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### 后台运行 / Run in Background

```bash
nohup streamlit run app.py &
```

## 常见问题 / FAQ

### Q: 如何更改显示的数据？
A: 修改 `sample_data.py` 或连接到本地数据库。

### Q: How to change the displayed data?
A: Modify `sample_data.py` or connect to a local database.

### Q: 如何添加新的筛选条件？
A: 在 `data_loader.py` 中添加新的筛选方法，然后在 `app.py` 中添加对应的UI控件。

### Q: How to add new filter conditions?
A: Add new filter methods in `data_loader.py`, then add corresponding UI controls in `app.py`.

### Q: 数据库文件会被提交到Git吗？
A: 不会，`.gitignore` 已配置排除所有数据库文件。

### Q: Will database files be committed to Git?
A: No, `.gitignore` is configured to exclude all database files.

## 扩展开发 / Extension Development

### 添加新的页面 / Add New Pages

在 `app.py` 的 `main()` 函数中添加新的页面选项：

```python
page = st.radio(
    "选择页面",
    ["📊 数据概览", "📋 课程列表", "🔍 课程搜索", "📈 新页面"]
)

if page == "📈 新页面":
    show_new_page()
```

### 添加新的数据模型 / Add New Data Models

在 `data_model.py` 中定义新的数据类：

```python
@dataclass
class Teacher:
    teacher_id: str
    name: str
    department: str
```

### 添加新的可视化图表 / Add New Charts

使用 Plotly 添加新的图表：

```python
import plotly.express as px

fig = px.scatter(df, x='学分', y='学时', color='课程类型')
st.plotly_chart(fig)
```

## 技术支持 / Support

遇到问题请提交 Issue 到项目仓库。

For issues, please submit an Issue to the project repository.
