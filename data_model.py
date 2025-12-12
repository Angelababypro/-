"""
数据模型定义
Course Standardization Data Model
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Course:
    """课程标准化数据模型"""
    course_id: str
    course_name: str
    course_code: str
    credits: float
    hours: int
    course_type: str  # 必修/选修
    semester: str
    department: str
    instructor: str
    description: Optional[str] = None
    prerequisites: Optional[List[str]] = None
    capacity: Optional[int] = None
    enrolled: Optional[int] = None
    
    def get_enrollment_rate(self) -> float:
        """计算课程报名率"""
        if self.capacity and self.capacity > 0:
            return (self.enrolled or 0) / self.capacity * 100
        return 0.0
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            '课程ID': self.course_id,
            '课程名称': self.course_name,
            '课程代码': self.course_code,
            '学分': self.credits,
            '学时': self.hours,
            '课程类型': self.course_type,
            '学期': self.semester,
            '院系': self.department,
            '授课教师': self.instructor,
            '课程描述': self.description or '',
            '先修课程': ', '.join(self.prerequisites) if self.prerequisites else '',
            '容量': self.capacity or 0,
            '已报名': self.enrolled or 0,
            '报名率': f"{self.get_enrollment_rate():.1f}%"
        }
