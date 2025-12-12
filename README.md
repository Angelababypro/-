# 课程标准化数据展示系统

基于 Streamlit 的课程标准化数据前端展示系统。本系统提供课程数据的可视化展示、搜索和筛选功能。

## 功能特点

- 📊 **数据概览**: 展示课程统计信息和可视化图表
- 📋 **课程列表**: 浏览所有课程的详细信息
- 🔍 **搜索功能**: 支持关键词搜索和多条件筛选
- 📈 **数据可视化**: 使用图表展示课程分布和报名情况
- 🎨 **友好界面**: 基于 Streamlit 的现代化 Web 界面

## 系统架构

```
├── app.py              # Streamlit 主应用
├── data_model.py       # 数据模型定义
├── data_loader.py      # 数据加载接口（可连接本地数据库）
├── sample_data.py      # 示例数据
├── requirements.txt    # Python 依赖
└── README.md          # 项目文档
```

## 安装步骤

### 1. 克隆项目

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

### 功能说明

#### 数据概览页面
- 显示课程总数、总容量、已报名人数等统计信息
- 院系课程分布饼图
- 课程类型分布柱状图
- 课程报名情况对比图

#### 课程列表页面
- 显示所有课程的详细信息表格
- 支持按院系、学期、课程类型筛选
- 可查看每门课程的详细信息

#### 课程搜索页面
- 支持关键词搜索（课程名称、课程代码、教师名称）
- 结合筛选条件进行精确查找

## 数据库集成说明

### 当前状态
系统当前使用示例数据演示功能。数据库连接需要在本地配置（出于安全考虑，数据库不包含在代码仓库中）。

### 连接本地数据库

要连接本地数据库，请修改 `data_loader.py` 文件：

#### SQLite 示例

```python
import sqlite3

class DataLoader:
    def __init__(self):
        # 连接到本地 SQLite 数据库
        self.conn = sqlite3.connect('courses.db')
        self.cursor = self.conn.cursor()
    
    def get_all_courses(self) -> List[Course]:
        self.cursor.execute("SELECT * FROM courses")
        rows = self.cursor.fetchall()
        # 将数据库记录转换为 Course 对象
        return [self._row_to_course(row) for row in rows]
```

#### MySQL 示例

```python
import mysql.connector

class DataLoader:
    def __init__(self):
        # 连接到本地 MySQL 数据库
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="courses_db"
        )
        self.cursor = self.conn.cursor()
```

#### PostgreSQL 示例

```python
import psycopg2

class DataLoader:
    def __init__(self):
        # 连接到本地 PostgreSQL 数据库
        self.conn = psycopg2.connect(
            host="localhost",
            database="courses_db",
            user="your_username",
            password="your_password"
        )
        self.cursor = self.conn.cursor()
```

### 数据库表结构

建议的课程表结构：

```sql
CREATE TABLE courses (
    course_id VARCHAR(50) PRIMARY KEY,
    course_name VARCHAR(200) NOT NULL,
    course_code VARCHAR(50) NOT NULL,
    credits DECIMAL(3,1) NOT NULL,
    hours INTEGER NOT NULL,
    course_type VARCHAR(20) NOT NULL,
    semester VARCHAR(50) NOT NULL,
    department VARCHAR(100) NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    description TEXT,
    prerequisites TEXT,
    capacity INTEGER,
    enrolled INTEGER
);
```

## 技术栈

- **Python 3.7+**: 编程语言
- **Streamlit**: Web 应用框架
- **Pandas**: 数据处理
- **Plotly**: 数据可视化
- **NumPy**: 数值计算

## 项目结构说明

### `app.py`
主应用文件，包含：
- Streamlit 页面配置
- 三个主要页面（数据概览、课程列表、课程搜索）
- 数据可视化图表
- 用户界面组件

### `data_model.py`
数据模型定义：
- `Course` 类：课程标准化数据模型
- 包含课程的所有属性和方法

### `data_loader.py`
数据加载接口：
- 提供统一的数据访问接口
- 可以轻松切换到实际数据库连接
- 包含搜索、筛选、统计等功能

### `sample_data.py`
示例数据生成器：
- 提供演示用的示例课程数据
- 可以作为数据格式参考

## 安全注意事项

⚠️ **重要提醒**：
- 数据库配置文件不应提交到代码仓库
- 使用 `.gitignore` 排除数据库文件和敏感配置
- 生产环境中应使用环境变量管理数据库凭证
- 建议使用 `.streamlit/secrets.toml` 管理敏感信息

示例 `secrets.toml`:
```toml
[database]
host = "localhost"
port = 3306
username = "your_username"
password = "your_password"
database = "courses_db"
```

## 扩展功能建议

- [ ] 添加用户认证功能
- [ ] 支持课程数据的导入/导出
- [ ] 添加更多数据可视化图表
- [ ] 实现课程排课冲突检测
- [ ] 添加学生选课模拟功能
- [ ] 支持多语言界面

## 常见问题

### 如何更改端口？
```bash
streamlit run app.py --server.port 8502
```

### 如何在后台运行？
```bash
nohup streamlit run app.py &
```

### 如何访问远程服务器上的应用？
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

## 许可证

本项目仅用于课程管理数据展示，数据库连接和敏感数据需在本地配置。

## 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。
