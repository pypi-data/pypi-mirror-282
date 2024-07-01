# apat_frame
目录结构：
apat_frame/
│
├── test_package/
│   ├── __init__.py
│   ├── plugins/
│   │   ├── __init__.py
│   │   └── allure.7z
│   │   └── appium.7z
│   └──  test_utils/
│       ├── __init__.py
│       ├── assertinfo/
│       │   ├── expect_image/
│       │   ├── runtime_image/
│       │   └── assertinfo.json
│       ├── dbconnect/
│       │   ├── async_dbsetting/
│       │   ├── app1/
                ├── __init__.py
                └──testcaseModel.py
│       │   ├── sync_dbsetting/
│       │   ├── sync_dbddl.py
│       │   ├── db.json
│       │   ├── async_dbddl.py
│       │   └── __init__.py
│       ├── log/
│       │   ├── request/
│       │   │   └── request_log.json
│       │   └── __init__.py
│       ├── testreport/
│       │   └── __init__.py
│       └── tools/
│           ├── commonpath.py
│           ├── compare.py
│           ├── RequestAndResponse.py
│           ├── setup.py
│           ├── zip.py
│           └── __init__.py
├── default_database.db
├── MANIFEST.in
├── setup.py
└── README.md

目录说明：
    apat_frame 是项目的根目录。
    test_package 目录包含了测试相关的包。
    __init__.py 文件用于标记该目录作为Python包。
    plugins 子目录存放了可能用于测试框架的插件，如allure和appium的压缩包，这些可能是用于生成测试报告的Allure框架和进行移动应用测试的Appium工具。
    test_utils 包含了一系列测试辅助工具。
    assertinfo 用于存放预期图像与运行时图像以进行图像比对测试，以及存储断言信息的JSON配置文件。
    dbconnect 提供了同步和异步数据库连接设置、数据库DDL操作脚本（创建表等）以及数据库配置文件(db.json)。
    log 包含请求日志相关的文件夹和初始化文件，用于记录API请求响应日志。
    testreport 初始化文件预示着该部分可能用于生成或管理测试报告。
    tools 目录下有多个实用脚本，比如处理路径的commonpath.py、数据比较的compare.py、处理HTTP请求与响应的RequestAndResponse.py、打包解压工具zip.py等。
    default_database.db 可能是项目默认使用的数据库文件，用于存储测试所需的固定数据或测试过程中的临时数据。
    MANIFEST.in 文件指导构建过程应包含哪些非源代码文件，例如数据文件或配置文件。
    setup.py 是Python项目的安装脚本，用于定义项目的元数据和安装依赖。
    README.md 是项目的说明文档，通常包括项目介绍、安装指南、使用示例等内容。


版本信息：1.0.14
更新内容：数据库同步操作时，访问类型应为字典


版本信息：1.0.13
更新内容：提供数据库类封装以及图片像素对比方法

版本信息：1.0.12
更新内容：
    1、提供数据库同步操作

版本信息：1.0.11
更新内容：
    1、数据库操作语句提供根据网络判断时区功能、提供用户自定义数据库连接串、提供封装类方法
    2、tools中提供compare方法

版本信息：1.0.0
版本描述：该库将提供一个全面的、通用的自动化测试框架，旨在完成webUI自动化、接口自动化以及移动端自动化测试。
版本详情：
    app_plugin中安装appium库，web_plugin中安装playwright和aiohttp库，然后通过test_utils进行pytest集成与二次封装和单元测试。后续依赖库playwright、aiohttp、playwright、pytest需要更新的时候，对组件进行整体覆盖，然后跑单元测试，单元测试通过后再进行发布；test_utils中还包含各类工具。
    测试用例字段：
    code-编号：以当前时间戳生成
    name-名称：用例名称
    desccription-描述：用例描述，可为空
    category1-分类：用例大分类，不可为空，分为webui、interface、mobile
    category2-分类：用例小分类，可为空，自定义分类
    status-状态：用例状态
    script-脚本：用例脚本，不可为空
    expected-预期结果：用例预期结果，可为空
    actual-实际结果：用例实际结果，可为空
    result-结果：用例结果，可为空
    create_time-创建时间：用例创建时间，可为空
    update_time-更新时间：用例更新时间，可为空
    creator-创建人：用例创建人，可为空
    updater-更新人：用例更新人，可为空


    对于任意测试用例，都存在编号、名称、用例大分类
    当该用例属于webui和移动端Ui时，script字段中存入json格式为
    {
        "script": "",
        "kargs": {
            "number": "",
            "password": "",
            ...

        }
    }
    当该用例属于接口自动化用例时，script字段中存入json格式为
    {
        "method": "",
        "url": "",
        "kwargs": {
            "Content-Type": "application/json",
            ...
        }
    }
