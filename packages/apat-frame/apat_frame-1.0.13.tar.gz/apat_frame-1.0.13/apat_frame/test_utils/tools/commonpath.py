import os
from pathlib import Path

class commonpath:
    """
    该类用于管理项目中使用的各种路径。
    """
    """
    This class is used to store all the paths used in the project.
    """
    # 初始化方法，用于设置各种路径
    def __init__(self):
        # 定义Allure命令行工具bin目录的路径
        self.allure_bin_path = os.path.join(Path(__file__).parents[2], 'plugins', 'allure', 'bin', 'allure')
        # 定义Playwright驱动程序（针对Mac）目录的路径
        self.playwright_driver_path_for_mac = os.path.join(Path(__file__).parents[2], 'plugins', 'ms-playwright')
        # 定义Chromium浏览器目录（针对Mac）的路径
        self.chromium_path = os.path.join(self.playwright_driver_path_for_mac, 'chromium-1117', 'chrome-mac')

        # 定义Appium插件目录的路径
        self.appium_path = os.path.join(Path(__file__).parents[2], 'plugins', 'appium')
        # 定义Allure插件目录的路径
        self.allure_path = os.path.join(Path(__file__).parents[2], 'plugins', 'allure')
        
        # 定义plugins目录的路径
        self.plugins_path = os.path.join(Path(__file__).parents[2], 'plugins')
        
        # 定义日志目录的存储路径
        self.log_path = os.path.join(Path(__file__).parents[2], 'test_utils', 'logs')
        # 定义请求日志文件的路径
        self.request_log_dir =os.path.join(self.log_path, 'request_log.json')

        # 定义Chromium浏览器7z压缩文件的路径
        self.chromium_7z_dir = os.path.join(self.playwright_driver_path_for_mac, 'chromium-1117', 'chrome-mac', 'Chromium.app.7z.001')

        # 定义异步数据库设置目录的路径
        self.async_dbsetting_path = os.path.join(Path(__file__).parents[2], 'test_utils', 'dbconnect', 'async_dbsetting')

    # 获取异步数据库设置目录的路径
    def get_async_dbsetting_path(self):
        return self.async_dbsetting_path

    # 获取请求日志文件的路径
    def get_request_log_dir(self):
        return self.request_log_dir

    # 获取Appium插件的路径
    def get_appium_path(self):
        return self.appium_path
    # 获取Appium 7z压缩文件的路径
    def get_appium_7z_path(self):
        return os.path.join(self.plugins_path,'appium.7z')

    # 获取日志牡蛎的存储路径
    def get_log_path(self):
        return self.log_path

    # 获取Allure插件目录的路径
    def get_allure_path(self):
        return self.allure_path
    # 获取Allure 7z压缩文件的路径
    def get_allure_7z_path(self):
        return os.path.join(self.plugins_path,'allure.7z')

    # 获取plugins目录的路径
    def get_plugins_path(self):
        return self.plugins_path

    # 获取Allure命令行工具bin目录的路径
    def get_allure_bin(self):
        return self.allure_bin_path

    # 获取Playwright驱动程序（针对Mac）的路径
    def get_playwright_driver_path_for_mac(self):
        return self.playwright_driver_path_for_mac

    # 获取Chromium浏览器的路径
    def get_chromium_path(self):
        return self.chromium_path

if __name__ == '__main__':
    # 初始化commonpath实例，并设置环境变量PLAYWRIGHT_BROWSERS_PATH
    commonpath = commonpath()
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = commonpath.get_playwright_driver_path_for_mac()
    # 由于示例的限制，以下代码可能未被执行或展示完整的使用场景
    import time