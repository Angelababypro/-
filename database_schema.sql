-- 课程标准化数据库表结构
-- Course Standardization Database Schema

-- 创建课程表
CREATE TABLE IF NOT EXISTS courses (
    course_id VARCHAR(50) PRIMARY KEY COMMENT '课程ID',
    course_name VARCHAR(200) NOT NULL COMMENT '课程名称',
    course_code VARCHAR(50) NOT NULL COMMENT '课程代码',
    credits DECIMAL(3,1) NOT NULL COMMENT '学分',
    hours INTEGER NOT NULL COMMENT '学时',
    course_type VARCHAR(20) NOT NULL COMMENT '课程类型（必修/选修）',
    semester VARCHAR(50) NOT NULL COMMENT '学期',
    department VARCHAR(100) NOT NULL COMMENT '院系',
    instructor VARCHAR(100) NOT NULL COMMENT '授课教师',
    description TEXT COMMENT '课程描述',
    prerequisites TEXT COMMENT '先修课程（用逗号分隔）',
    capacity INTEGER COMMENT '课程容量',
    enrolled INTEGER COMMENT '已报名人数',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
);

-- 创建索引以提高查询性能
CREATE INDEX idx_department ON courses(department);
CREATE INDEX idx_semester ON courses(semester);
CREATE INDEX idx_course_type ON courses(course_type);
CREATE INDEX idx_instructor ON courses(instructor);
CREATE INDEX idx_course_name ON courses(course_name);

-- 示例数据插入语句
INSERT INTO courses (course_id, course_name, course_code, credits, hours, course_type, semester, department, instructor, description, prerequisites, capacity, enrolled) VALUES
('CS001', '数据结构与算法', 'CS-101', 4.0, 64, '必修', '2024春季', '计算机科学与技术学院', '张教授', '本课程介绍基本的数据结构和算法设计方法，包括线性表、树、图等数据结构以及排序、查找等算法。', '程序设计基础', 120, 115),
('CS002', '数据库系统', 'CS-201', 3.0, 48, '必修', '2024春季', '计算机科学与技术学院', '李教授', '介绍数据库系统的基本概念、设计方法、SQL语言以及数据库管理系统的实现原理。', '数据结构与算法', 100, 95),
('CS003', '人工智能导论', 'CS-301', 3.0, 48, '选修', '2024春季', '计算机科学与技术学院', '王教授', '介绍人工智能的基本概念、技术和应用，包括机器学习、深度学习、自然语言处理等。', '数据结构与算法,线性代数', 80, 78),
('MATH001', '高等数学', 'MATH-101', 5.0, 80, '必修', '2024春季', '数学学院', '赵教授', '介绍微积分、极限、导数、积分等基础数学知识。', NULL, 150, 145),
('MATH002', '线性代数', 'MATH-102', 3.0, 48, '必修', '2024春季', '数学学院', '孙教授', '介绍矩阵理论、线性方程组、向量空间等线性代数的基础知识。', '高等数学', 150, 142),
('CS004', '计算机网络', 'CS-202', 3.5, 56, '必修', '2024秋季', '计算机科学与技术学院', '周教授', '介绍计算机网络的基本原理、协议和应用，包括TCP/IP、HTTP、路由算法等。', '数据结构与算法', 100, 88),
('CS005', '软件工程', 'CS-203', 3.0, 48, '必修', '2024秋季', '计算机科学与技术学院', '吴教授', '介绍软件开发的全生命周期、需求分析、设计模式、测试方法等软件工程实践。', '数据结构与算法', 90, 85),
('CS006', '机器学习', 'CS-302', 4.0, 64, '选修', '2024秋季', '计算机科学与技术学院', '郑教授', '深入学习机器学习的理论和实践，包括监督学习、无监督学习、强化学习等。', '人工智能导论,线性代数,概率论与数理统计', 60, 60),
('ENG001', '大学英语', 'ENG-101', 2.0, 32, '必修', '2024春季', '外国语学院', '刘教师', '提高学生的英语听说读写能力，为专业学习和未来工作打下基础。', NULL, 200, 195),
('CS007', 'Web开发技术', 'CS-303', 3.0, 48, '选修', '2024秋季', '计算机科学与技术学院', '陈教授', '介绍现代Web开发技术，包括HTML、CSS、JavaScript、前端框架和后端开发。', '数据库系统', 70, 65);

-- 查询示例

-- 1. 查询所有课程
-- SELECT * FROM courses;

-- 2. 按院系查询
-- SELECT * FROM courses WHERE department = '计算机科学与技术学院';

-- 3. 按学期查询
-- SELECT * FROM courses WHERE semester = '2024春季';

-- 4. 查询必修课
-- SELECT * FROM courses WHERE course_type = '必修';

-- 5. 搜索课程（模糊查询）
-- SELECT * FROM courses WHERE course_name LIKE '%数据%' OR instructor LIKE '%张%';

-- 6. 统计各院系的课程数量
-- SELECT department, COUNT(*) as course_count FROM courses GROUP BY department;

-- 7. 计算平均报名率
-- SELECT AVG(enrolled * 100.0 / capacity) as avg_enrollment_rate FROM courses WHERE capacity > 0;

-- 8. 查询报名率高于90%的课程
-- SELECT course_name, instructor, (enrolled * 100.0 / capacity) as enrollment_rate 
-- FROM courses 
-- WHERE capacity > 0 AND (enrolled * 100.0 / capacity) > 90
-- ORDER BY enrollment_rate DESC;
