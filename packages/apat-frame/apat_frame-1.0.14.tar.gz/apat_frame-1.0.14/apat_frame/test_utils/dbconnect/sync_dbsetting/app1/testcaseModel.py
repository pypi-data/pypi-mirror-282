# 导入SQLAlchemy库中与列定义相关的模块以及声明性基类和SQL函数
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base  # 用于声明ORM基类

# 使用declarative_base()创建一个基类，ORM模型将继承自这个基类
Base = declarative_base()

# 定义CaseManageModel类，该类继承自Base，对应数据库中的'casemanage'表
class CaseManageModel(Base):
    __tablename__ = 'casemanage'  # 指定表名
    
    # 定义表的各列，包括数据类型和约束条件
    code = Column(String(255), primary_key=True)  # 编码，主键，字符串类型，最大长度255
    name = Column(String(255))  # 名称，字符串类型，最大长度255
    description = Column(Text)  # 描述，文本类型
    category1 = Column(String(50))  # 第一类别，字符串类型，最大长度50
    category2 = Column(String(50), nullable=True)  # 第二类别，可为空，字符串类型，最大长度50
    status = Column(Integer, nullable=True)  # 状态，整数类型，可为空
    script = Column(Text)  # 脚本，文本类型
    expected = Column(Text)  # 期望结果，文本类型
    actual = Column(Text)  # 实际结果，文本类型
    result = Column(Text)  # 测试结果，字符串类型，最大长度50，可为空
    create_time = Column(DateTime, server_default=func.now())  # 创建时间，默认为当前时间
    update_time = Column(DateTime, onupdate=func.now())  # 更新时间，每次更新时自动设置为当前时间
    creator = Column(String(50), nullable=True)  # 创建者，字符串类型，最大长度50，可为空
    updater = Column(String(50), nullable=True)  # 更新者，字符串类型，最大长度50，可为空

