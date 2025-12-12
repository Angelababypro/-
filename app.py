"""
课程标准化数据展示系统
Course Standardization Data Display System
使用 Streamlit 实现前端展示
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_loader import DataLoader


# 页面配置
st.set_page_config(
    page_title="课程标准化数据展示系统",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 初始化数据加载器
@st.cache_resource
def get_data_loader():
    """获取数据加载器实例"""
    return DataLoader()


def show_statistics(data_loader):
    """显示统计信息"""
    stats = data_loader.get_statistics()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("课程总数", stats['total_courses'])
    
    with col2:
        st.metric("总容量", stats['total_capacity'])
    
    with col3:
        st.metric("已报名人数", stats['total_enrolled'])
    
    with col4:
        st.metric("平均报名率", f"{stats['enrollment_rate']:.1f}%")


def show_charts(data_loader):
    """显示图表"""
    stats = data_loader.get_statistics()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 院系课程分布
        st.subheader("院系课程分布")
        dept_data = pd.DataFrame(
            list(stats['departments_count'].items()),
            columns=['院系', '课程数量']
        )
        fig = px.pie(
            dept_data, 
            values='课程数量', 
            names='院系',
            title='各院系课程数量分布'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 课程类型分布
        st.subheader("课程类型分布")
        type_data = pd.DataFrame(
            list(stats['course_types_count'].items()),
            columns=['课程类型', '课程数量']
        )
        fig = px.bar(
            type_data,
            x='课程类型',
            y='课程数量',
            title='课程类型统计',
            color='课程类型'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 课程报名情况
    st.subheader("课程报名情况")
    courses_df = data_loader.get_courses_dataframe()
    
    # 提取数值型报名率
    courses_df['报名率数值'] = courses_df['报名率'].str.rstrip('%').astype(float)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='容量',
        x=courses_df['课程名称'],
        y=courses_df['容量'],
        marker_color='lightblue'
    ))
    fig.add_trace(go.Bar(
        name='已报名',
        x=courses_df['课程名称'],
        y=courses_df['已报名'],
        marker_color='darkblue'
    ))
    
    fig.update_layout(
        title='各课程容量与报名情况对比',
        xaxis_title='课程',
        yaxis_title='人数',
        barmode='group'
    )
    st.plotly_chart(fig, use_container_width=True)


def show_course_list(data_loader, filters):
    """显示课程列表"""
    # 应用筛选条件
    courses = data_loader.filter_courses(
        department=filters.get('department'),
        semester=filters.get('semester'),
        course_type=filters.get('course_type')
    )
    
    # 应用搜索
    search_keyword = filters.get('search', '')
    if search_keyword:
        courses = [c for c in courses if 
                   search_keyword.lower() in c.course_name.lower() or
                   search_keyword.lower() in c.course_code.lower() or
                   search_keyword.lower() in c.instructor.lower()]
    
    if not courses:
        st.warning("没有找到符合条件的课程")
        return
    
    # 转换为DataFrame显示
    df = pd.DataFrame([course.to_dict() for course in courses])
    
    # 显示课程数量
    st.info(f"找到 {len(courses)} 门课程")
    
    # 显示数据表格
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "课程ID": st.column_config.TextColumn("课程ID", width="small"),
            "课程名称": st.column_config.TextColumn("课程名称", width="medium"),
            "学分": st.column_config.NumberColumn("学分", format="%.1f"),
            "学时": st.column_config.NumberColumn("学时"),
            "报名率": st.column_config.TextColumn("报名率", width="small"),
        }
    )
    
    # 详细信息展开
    with st.expander("查看课程详细信息"):
        selected_course_name = st.selectbox(
            "选择课程",
            [c.course_name for c in courses]
        )
        
        selected_course = next(c for c in courses if c.course_name == selected_course_name)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**课程ID:** {selected_course.course_id}")
            st.write(f"**课程名称:** {selected_course.course_name}")
            st.write(f"**课程代码:** {selected_course.course_code}")
            st.write(f"**学分:** {selected_course.credits}")
            st.write(f"**学时:** {selected_course.hours}")
            st.write(f"**课程类型:** {selected_course.course_type}")
        
        with col2:
            st.write(f"**学期:** {selected_course.semester}")
            st.write(f"**院系:** {selected_course.department}")
            st.write(f"**授课教师:** {selected_course.instructor}")
            st.write(f"**容量:** {selected_course.capacity}")
            st.write(f"**已报名:** {selected_course.enrolled}")
            st.write(f"**报名率:** {selected_course.get_enrollment_rate():.1f}%")
        
        st.write(f"**课程描述:**")
        st.write(selected_course.description or "暂无描述")
        
        if selected_course.prerequisites:
            st.write(f"**先修课程:** {', '.join(selected_course.prerequisites)}")


def main():
    """主函数"""
    st.title("📚 课程标准化数据展示系统")
    st.markdown("---")
    
    # 初始化数据加载器
    data_loader = get_data_loader()
    
    # 侧边栏 - 导航和筛选
    with st.sidebar:
        st.header("导航")
        page = st.radio(
            "选择页面",
            ["📊 数据概览", "📋 课程列表", "🔍 课程搜索"]
        )
        
        st.markdown("---")
        st.header("筛选条件")
        
        # 筛选条件
        department = st.selectbox(
            "院系",
            ["全部"] + data_loader.get_departments()
        )
        
        semester = st.selectbox(
            "学期",
            ["全部"] + data_loader.get_semesters()
        )
        
        course_type = st.selectbox(
            "课程类型",
            ["全部"] + data_loader.get_course_types()
        )
        
        search_keyword = st.text_input("搜索关键词", "")
        
        st.markdown("---")
        st.info("💡 **提示:** 本系统仅包含前端展示功能，数据库连接需在本地配置。")
    
    # 构建筛选器字典
    filters = {
        'department': None if department == "全部" else department,
        'semester': None if semester == "全部" else semester,
        'course_type': None if course_type == "全部" else course_type,
        'search': search_keyword
    }
    
    # 根据选择的页面显示不同内容
    if page == "📊 数据概览":
        st.header("数据概览")
        show_statistics(data_loader)
        st.markdown("---")
        show_charts(data_loader)
        
    elif page == "📋 课程列表":
        st.header("课程列表")
        show_course_list(data_loader, filters)
        
    elif page == "🔍 课程搜索":
        st.header("课程搜索")
        st.write("使用左侧的筛选条件和搜索框来查找课程")
        show_course_list(data_loader, filters)
    
    # 页脚
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>课程标准化数据展示系统 | 基于 Streamlit 构建</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
