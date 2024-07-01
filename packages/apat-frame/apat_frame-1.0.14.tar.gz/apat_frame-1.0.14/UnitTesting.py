from apat_frame.test_utils.dbconnect.async_dbddl import AsyncDBDDL
from apat_frame.test_utils.dbconnect.sync_dbddl import SyncDBDDL
import asyncio
import logging
import unittest
import os
from apat_frame.test_utils.tools.zip import PublicZip
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


class TestPublicZip(unittest.TestCase):
    def setUp(self):
        # 初始化测试参数
        self.input_file = 'test_input.zip'
        self.output_file = 'test_output.7z'
        self.freepath = 'test_freepath'
        self.public_zip = PublicZip(self.input_file, self.output_file, self.freepath)
        
        # 创建测试用的临时文件和目录
        with open(self.input_file, 'w') as file:
            file.write('test content')
        
        os.makedirs(self.freepath, exist_ok=True)
    
    def tearDown(self):
        # 测试结束后清理临时文件和目录
        os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        os.rmdir(self.freepath)
    
    def test_compress_to_7z(self):
        # 测试压缩目录到7z格式的功能
        self.public_zip.compress_to_7z(self.input_file, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
    
    def test_compress(self):
        # 测试压缩功能
        self.assertFalse(os.path.exists(self.output_file))
        self.public_zip.compress()
        self.assertTrue(os.path.exists(self.output_file))
    
    def test_extract_7z(self):
        # 测试解压7z格式的压缩文件的功能
        self.public_zip.extract_7z(self.input_file, self.freepath)
        self.assertTrue(os.path.exists(os.path.join(self.freepath, 'test_input.zip')))
    
    def test_extract(self):
        # 测试解压功能
        self.assertTrue(os.path.exists(self.input_file))
        self.assertFalse(os.path.exists(os.path.join(self.freepath, 'test_input.zip')))
        self.public_zip.extract()
        self.assertTrue(os.path.exists(os.path.join(self.freepath, 'test_input.zip')))
    
    def test_check_file_exists(self):
        # 测试检查文件是否存在的功能
        self.assertTrue(self.public_zip.check_file_exists(self.input_file))
        self.assertFalse(self.public_zip.check_file_exists('nonexistent_file.zip'))

if __name__ == '__main__':
    unittest.main()
