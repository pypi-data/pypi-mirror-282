# 导入必要的模块
from tortoise.models import Model  # Tortoise ORM的基类Model
from tortoise import fields, Tortoise  # Tortoise ORM的核心模块，用于字段定义和ORM初始化
from .async_dbsetting.app1.testcaseModel import CaseManageModel  # 引入CaseManageModel类
from datetime import datetime  # 日期时间处理模块，虽然本代码未直接使用但可能用于模型定义中

# 定义辅助函数：将模型实例转换为字典，排除私有属性（以_开头的属性）
def model_to_dict(instance):
    """将模型实例转换为字典，忽略以_开头的属性"""
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

# 定义异步数据库操作类 AsyncDBDDL
class AsyncDBDDL:
    """异步数据库DDL（数据定义语言）操作类"""

    # 初始化方法，接收数据库URL作为参数
    def __init__(self, url):
        """初始化方法，设置数据库连接URL"""
        self.url = url  # 保存数据库URL到实例变量中

    # 异步方法：初始化Tortoise ORM并配置数据库连接
    async def init_tortoise(self):
        """初始化Tortoise ORM，配置数据库连接和模型映射"""
        await Tortoise.init(  # 异步初始化Tortoise ORM
            {
                'connections': {  # 数据库连接配置
                    'default': self.url,  # 设置默认数据库连接URL
                },
                'apps': {  # 应用程序及模型映射配置
                    'test_utils_dbconnect': {  
                        'models': ['apat_frame.test_utils.dbconnect.async_dbsetting.app1'],  # 模型所在的模块路径
                        'default_connection': 'default',  # 指定该应用的默认数据库连接
                    }
                },
                'timezone': 'Asia/Shanghai',  # 设置ORM使用的时区
            },
        )
        # 可选步骤：根据模型自动生成数据库表结构
        # await Tortoise.generate_schemas()

    # 异步方法：查询CaseManageModel的所有记录
    async def selectall_operations(self):
        """查询CaseManageModel的所有记录并转换为字典列表"""
        instances = await CaseManageModel.all()  # 获取所有记录
        return model_to_dict(instances)  # 转换并返回记录列表

    # 异步方法：根据过滤条件查询CaseManageModel的记录
    async def select_operations(self, filter_key, value):
        """根据指定条件筛选CaseManageModel的记录并转换为字典列表"""
        instances = await CaseManageModel.filter(**{filter_key: value})  # 根据条件筛选记录
        return model_to_dict(instances)  # 转换并返回记录列表

    # 异步方法：更新CaseManageModel的记录
    async def update_operations(self, code, new_values):
        """根据code更新CaseManageModel的记录"""
        instance = await CaseManageModel.get(code=code)  # 根据code获取记录实例
        for key, value in new_values.items():  # 遍历新值并更新实例属性
            setattr(instance, key, value)
        await instance.save()  # 保存更新到数据库

    # 异步方法：删除CaseManageModel的特定记录
    async def delete_operations(self, code):
        """根据code删除CaseManageModel的记录"""
        instance = await CaseManageModel.get(code=code)  # 获取待删除记录
        await instance.delete()  # 执行删除操作

    # 异步方法：插入一个新的CaseManageModel记录
    async def insert_operations(self, code, name, description, category1, category2, status, script, expected, actual, result, creator, updater):
        """向CaseManageModel插入新记录"""
        await CaseManageModel.create(  # 创建新记录
            code=code, 
            name=name, 
            description=description, 
            category1=category1, 
            category2=category2, 
            status=status, 
            script=script, 
            expected=expected, 
            actual=actual, 
            result=result, 
            creator=creator, 
            updater=updater
        )
        return "success"  # 插入成功后返回"success"字符串