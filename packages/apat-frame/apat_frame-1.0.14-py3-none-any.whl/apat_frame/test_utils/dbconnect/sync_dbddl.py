# 导入SQLAlchemy相关模块，用于数据库操作
from sqlalchemy import create_engine, exc, text
from sqlalchemy.orm import sessionmaker, scoped_session
# 导入datetime模块，用于处理日期时间
from datetime import datetime
# 导入os模块，用于获取环境变量
import os
# 导入模型类
from .sync_dbsetting.app1.testcaseModel import CaseManageModel
# 导入keyword模块，用于检查标识符是否为Python关键字
import keyword

# 将SQLAlchemy模型实例转换为字典
# 定义函数model_to_dict，用于将SQLAlchemy模型实例转换为字典
def model_to_dict(instance):
    """
    将SQLAlchemy模型实例转换为字典。

    :param instance: SQLAlchemy模型实例
    :return: 字典，包含模型实例的属性和值
    """
    # 检查传入的实例是否为None，若是则直接返回空字典
    if instance is None:
        return {}
    
    # 遍历实例对应的表的所有列，构建一个字典，键为列名，值为该列在实例中的值
    return {c.key: getattr(instance, c.key) for c in instance.__table__.columns}

# 初始化MySQL数据库引擎，并返回一个scoped_session对象
def init_sqlalchemy_mysql(url):
    """
    初始化SQLAlchemy MySQL数据库连接。

    :param url: 数据库连接URL
    :return: scoped_session对象
    """
    engine = create_engine(url)
    return scoped_session(sessionmaker(bind=engine))

# 定义SyncDBDDL类，用于数据库DDL（数据定义语言）同步操作
class SyncDBDDL:
    # 初始化方法，接收数据库连接URL
    def __init__(self, url=None):
        if not url:
            url = 'mysql+mysqlconnector://root:123456@127.0.0.1:3306/zhangyuze'
        self.url = url

    # 装饰器，用于在函数执行前后管理SQLAlchemy session
    def execute_with_session(function):
        """
        装饰器，用于自动管理SQLAlchemy session的生命周期。

        :param function: 被装饰的函数
        :return: 包装后的函数
        """
        def wrapper(self, *args, **kwargs):
            # 打印函数参数
            print(f"args: {args}")
            print(f"kwargs: {kwargs}")
            print("饰器，用于自动管理Session的生命周期")
            # 初始化session
            session_factory = init_sqlalchemy_mysql(self.url)
            session = session_factory()
            try:
                # 执行函数，并返回结果
                result = function(self, session, *args, **kwargs)
            finally:
                # 关闭session
                session.close()
                session_factory.remove()
            return result
        return wrapper

    # 查询所有测试用例
    @execute_with_session
    def selectall_operations(self, session):
        """
        查询所有测试用例，并返回转换后的字典列表。

        :param session: SQLAlchemy session
        :return: 测试用例的字典列表
        """
        instances = session.query(CaseManageModel).all()
        return [model_to_dict(instance) for instance in instances]

    # 根据条件查询测试用例
    @execute_with_session
    def select_operations(self, session, filter_column, value):
        """
        根据指定条件查询测试用例，并返回转换后的字典列表。

        :param session: SQLAlchemy session
        :param filter_column: 查询条件的列名
        :param value: 查询条件的值
        :return: 测试用例的字典列表
        """
        instances = session.query(CaseManageModel).filter(getattr(CaseManageModel, filter_column) == value).all()
        return [model_to_dict(instance) for instance in instances]

    # 更新测试用例信息
    @execute_with_session
    def update_operations(self, session, code, updates):
        """
        更新指定测试用例的信息。

        :param session: SQLAlchemy session
        :param code: 测试用例代码
        :param updates: 包含更新键值对的字典
        """
        instance = session.query(CaseManageModel).get(code)
        if instance:
            for key, value in updates.items():
                setattr(instance, key, value)
            session.commit()
        else:
            raise ValueError(f"No instance found with code {code}")

    # 删除测试用例
    @execute_with_session
    def delete_operations(self, session, code):
        """
        删除指定测试用例。

        :param session: SQLAlchemy session
        :param code: 测试用例代码
        """
        instance = session.query(CaseManageModel).get(code)
        if instance:
            session.delete(instance)
            session.commit()
        else:
            raise ValueError(f"No instance found with code {code}")

    # 插入新的测试用例
    @execute_with_session
    def insert_operations(self, session, **kwargs):
        """
        插入新的测试用例。

        :param session: SQLAlchemy session
        :param kwargs: 包含新测试用例信息的键值对
        :return: 插入结果
        """
        new_instance = CaseManageModel(**kwargs)
        session.add(new_instance)
        session.commit()
        return "success"

    # 根据SQL查询测试用例
    @execute_with_session
    def select_operations_bysql(self, session, **kwargs):
        """
        根据提供的SQL查询测试用例。

        :param session: SQLAlchemy session
        :param kwargs: 包含SQL查询参数的字典
        :return: 查询结果列表
        """
        # 初始化变量，默认值设定
        select_vals = '*'
        select_table = 'casemanage'
        select_condition = ''
        group_column = ''
        order_clause = ''
        limit_number = None

        # 处理关键字参数
        for key, value in kwargs.items():
            if key == 'select_vals':
                select_vals = ', '.join(value) if isinstance(value, list) else value
            elif key == 'select_table':
                select_table = value
            elif key == 'select_condition':
                select_condition = str(value)
            elif key == 'group_column':
                group_column = value
            elif key == 'order':
                order_clause = value
            elif key == 'limit_number':
                limit_number = value
            else:
                print(f"{key} is not a recognized keyword argument.")

        # 检查表名和列名是否安全
        def is_safe_identifier(identifier):
            """
            检查给定的标识符是否为安全的表名或列名。

            :param identifier: 待检查的标识符
            :return: 是否安全
            """
            if identifier == '*':
                return True
            return identifier.isidentifier() and not keyword.iskeyword(identifier)

        table_and_columns_safety_check = f"Checking table '{select_table}' with columns '{select_vals}', safety: "
        if not is_safe_identifier(select_table):
            table_and_columns_safety_check += "Table name is unsafe."
        else:
            column_safety = all(is_safe_identifier(col.strip()) for col in select_vals.split(','))
            table_and_columns_safety_check += "safe" if column_safety else "Column name(s) are unsafe."

        print(table_and_columns_safety_check)

        if not is_safe_identifier(select_table) or not all(is_safe_identifier(col.strip()) for col in select_vals.split(',')):
            raise ValueError("Table name or column name contains unsafe characters.")

        # 构建SQL查询语句
        executesql = f'SELECT {select_vals} FROM {select_table}'
        if select_condition:
            executesql += f' WHERE {select_condition}'
        if group_column:
            executesql += f' GROUP BY {group_column}'
        if order_clause:
            executesql += f' {order_clause}'
        if limit_number is not None:
            executesql += f' LIMIT {limit_number}'

        # 执行SQL并获取所有数据
        try:
            select_result = session.execute(text(executesql)).mappings()
            result_list = []
            chunk = select_result.fetchmany(10)
            while chunk:
                result_list.extend(chunk)
                chunk = select_result.fetchmany(10)
            return result_list
        except Exception as e:
            print(f"An error occurred while executing the SQL: {e}")
            return None


