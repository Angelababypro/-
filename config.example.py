"""
配置文件示例
将此文件复制为 config.local.py 并填入实际的数据库配置
config.local.py 不会被提交到代码仓库（已在 .gitignore 中排除）
"""

# 数据库配置示例

# SQLite 配置
SQLITE_CONFIG = {
    'database': 'courses.db'  # SQLite 数据库文件路径
}

# MySQL 配置
MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'courses_db',
    'charset': 'utf8mb4'
}

# PostgreSQL 配置
POSTGRESQL_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'courses_db'
}

# 选择使用的数据库类型
# 可选值: 'sample', 'sqlite', 'mysql', 'postgresql'
DATABASE_TYPE = 'sample'  # 默认使用示例数据

# 应用配置
APP_CONFIG = {
    'page_title': '课程标准化数据展示系统',
    'page_icon': '📚',
    'layout': 'wide'
}
