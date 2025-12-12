"""
数据加载接口
Data Loader Interface - can be adapted to connect to local database
"""

from typing import List, Optional
from data_model import Course
from sample_data import get_sample_courses, get_departments, get_semesters, get_course_types
import pandas as pd


class DataLoader:
    """
    数据加载器
    
    在实际应用中，可以修改此类来连接本地数据库
    例如: SQLite, MySQL, PostgreSQL 等
    
    使用方法:
    1. 修改 __init__ 方法来建立数据库连接
    2. 修改各个方法来执行实际的数据库查询
    3. 保持方法签名不变，这样不需要修改前端代码
    """
    
    def __init__(self):
        """
        初始化数据加载器
        
        在实际应用中，可以在这里建立数据库连接:
        例如: self.conn = sqlite3.connect('courses.db')
        """
        # 目前使用示例数据
        self._courses = get_sample_courses()
    
    def get_all_courses(self) -> List[Course]:
        """
        获取所有课程
        
        实际应用中的SQL示例:
        SELECT * FROM courses
        """
        return self._courses
    
    def get_courses_dataframe(self) -> pd.DataFrame:
        """获取课程数据的DataFrame格式"""
        data = [course.to_dict() for course in self._courses]
        return pd.DataFrame(data)
    
    def search_courses(self, keyword: str) -> List[Course]:
        """
        搜索课程
        
        实际应用中的SQL示例:
        SELECT * FROM courses 
        WHERE course_name LIKE %keyword% 
        OR course_code LIKE %keyword%
        OR instructor LIKE %keyword%
        """
        keyword = keyword.lower()
        results = []
        for course in self._courses:
            if (keyword in course.course_name.lower() or
                keyword in course.course_code.lower() or
                keyword in course.instructor.lower() or
                keyword in course.department.lower()):
                results.append(course)
        return results
    
    def filter_courses(
        self, 
        department: Optional[str] = None,
        semester: Optional[str] = None,
        course_type: Optional[str] = None
    ) -> List[Course]:
        """
        按条件筛选课程
        
        实际应用中的SQL示例:
        SELECT * FROM courses 
        WHERE department = ? AND semester = ? AND course_type = ?
        """
        results = self._courses
        
        if department:
            results = [c for c in results if c.department == department]
        
        if semester:
            results = [c for c in results if c.semester == semester]
        
        if course_type:
            results = [c for c in results if c.course_type == course_type]
        
        return results
    
    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        """
        根据ID获取课程
        
        实际应用中的SQL示例:
        SELECT * FROM courses WHERE course_id = ?
        """
        for course in self._courses:
            if course.course_id == course_id:
                return course
        return None
    
    def get_departments(self) -> List[str]:
        """获取所有院系"""
        return get_departments()
    
    def get_semesters(self) -> List[str]:
        """获取所有学期"""
        return get_semesters()
    
    def get_course_types(self) -> List[str]:
        """获取课程类型"""
        return get_course_types()
    
    def get_statistics(self) -> dict:
        """
        获取统计数据
        
        实际应用中可以使用SQL聚合函数
        """
        total_courses = len(self._courses)
        total_capacity = sum(c.capacity or 0 for c in self._courses)
        total_enrolled = sum(c.enrolled or 0 for c in self._courses)
        
        departments_count = {}
        for course in self._courses:
            departments_count[course.department] = departments_count.get(course.department, 0) + 1
        
        course_types_count = {}
        for course in self._courses:
            course_types_count[course.course_type] = course_types_count.get(course.course_type, 0) + 1
        
        return {
            'total_courses': total_courses,
            'total_capacity': total_capacity,
            'total_enrolled': total_enrolled,
            'enrollment_rate': (total_enrolled / total_capacity * 100) if total_capacity > 0 else 0,
            'departments_count': departments_count,
            'course_types_count': course_types_count
        }
