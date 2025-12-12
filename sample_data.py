"""
示例数据生成器
Sample Data Generator for Course Standardization
"""

from data_model import Course
from typing import List


def get_sample_courses() -> List[Course]:
    """
    生成示例课程数据
    在实际应用中，这些数据应该从本地数据库中读取
    """
    sample_courses = [
        Course(
            course_id="CS001",
            course_name="数据结构与算法",
            course_code="CS-101",
            credits=4.0,
            hours=64,
            course_type="必修",
            semester="2024春季",
            department="计算机科学与技术学院",
            instructor="张教授",
            description="本课程介绍基本的数据结构和算法设计方法，包括线性表、树、图等数据结构以及排序、查找等算法。",
            prerequisites=["程序设计基础"],
            capacity=120,
            enrolled=115
        ),
        Course(
            course_id="CS002",
            course_name="数据库系统",
            course_code="CS-201",
            credits=3.0,
            hours=48,
            course_type="必修",
            semester="2024春季",
            department="计算机科学与技术学院",
            instructor="李教授",
            description="介绍数据库系统的基本概念、设计方法、SQL语言以及数据库管理系统的实现原理。",
            prerequisites=["数据结构与算法"],
            capacity=100,
            enrolled=95
        ),
        Course(
            course_id="CS003",
            course_name="人工智能导论",
            course_code="CS-301",
            credits=3.0,
            hours=48,
            course_type="选修",
            semester="2024春季",
            department="计算机科学与技术学院",
            instructor="王教授",
            description="介绍人工智能的基本概念、技术和应用，包括机器学习、深度学习、自然语言处理等。",
            prerequisites=["数据结构与算法", "线性代数"],
            capacity=80,
            enrolled=78
        ),
        Course(
            course_id="MATH001",
            course_name="高等数学",
            course_code="MATH-101",
            credits=5.0,
            hours=80,
            course_type="必修",
            semester="2024春季",
            department="数学学院",
            instructor="赵教授",
            description="介绍微积分、极限、导数、积分等基础数学知识。",
            prerequisites=None,
            capacity=150,
            enrolled=145
        ),
        Course(
            course_id="MATH002",
            course_name="线性代数",
            course_code="MATH-102",
            credits=3.0,
            hours=48,
            course_type="必修",
            semester="2024春季",
            department="数学学院",
            instructor="孙教授",
            description="介绍矩阵理论、线性方程组、向量空间等线性代数的基础知识。",
            prerequisites=["高等数学"],
            capacity=150,
            enrolled=142
        ),
        Course(
            course_id="CS004",
            course_name="计算机网络",
            course_code="CS-202",
            credits=3.5,
            hours=56,
            course_type="必修",
            semester="2024秋季",
            department="计算机科学与技术学院",
            instructor="周教授",
            description="介绍计算机网络的基本原理、协议和应用，包括TCP/IP、HTTP、路由算法等。",
            prerequisites=["数据结构与算法"],
            capacity=100,
            enrolled=88
        ),
        Course(
            course_id="CS005",
            course_name="软件工程",
            course_code="CS-203",
            credits=3.0,
            hours=48,
            course_type="必修",
            semester="2024秋季",
            department="计算机科学与技术学院",
            instructor="吴教授",
            description="介绍软件开发的全生命周期、需求分析、设计模式、测试方法等软件工程实践。",
            prerequisites=["数据结构与算法"],
            capacity=90,
            enrolled=85
        ),
        Course(
            course_id="CS006",
            course_name="机器学习",
            course_code="CS-302",
            credits=4.0,
            hours=64,
            course_type="选修",
            semester="2024秋季",
            department="计算机科学与技术学院",
            instructor="郑教授",
            description="深入学习机器学习的理论和实践，包括监督学习、无监督学习、强化学习等。",
            prerequisites=["人工智能导论", "线性代数", "概率论与数理统计"],
            capacity=60,
            enrolled=60
        ),
        Course(
            course_id="ENG001",
            course_name="大学英语",
            course_code="ENG-101",
            credits=2.0,
            hours=32,
            course_type="必修",
            semester="2024春季",
            department="外国语学院",
            instructor="刘教师",
            description="提高学生的英语听说读写能力，为专业学习和未来工作打下基础。",
            prerequisites=None,
            capacity=200,
            enrolled=195
        ),
        Course(
            course_id="CS007",
            course_name="Web开发技术",
            course_code="CS-303",
            credits=3.0,
            hours=48,
            course_type="选修",
            semester="2024秋季",
            department="计算机科学与技术学院",
            instructor="陈教授",
            description="介绍现代Web开发技术，包括HTML、CSS、JavaScript、前端框架和后端开发。",
            prerequisites=["数据库系统"],
            capacity=70,
            enrolled=65
        )
    ]
    
    return sample_courses


def get_departments() -> List[str]:
    """获取所有院系列表"""
    return [
        "计算机科学与技术学院",
        "数学学院",
        "外国语学院"
    ]


def get_semesters() -> List[str]:
    """获取所有学期列表"""
    return ["2024春季", "2024秋季"]


def get_course_types() -> List[str]:
    """获取课程类型列表"""
    return ["必修", "选修"]
