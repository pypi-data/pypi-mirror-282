import os
import py7zr

class PublicZip:
    """
    公共ZIP处理类，提供压缩和解压功能。
    
    参数:
    input_file: 输入文件路径，用于压缩或解压的源文件。
    output_file: 输出文件路径，压缩后的文件保存路径。
    freepath: 解压目标路径，解压时文件将被解压到此路径。
    """
    def __init__(self,input_file,output_file,freepath):
        self.input_file = input_file  #目标文件路径
        self.output_file = output_file  #压缩文件路径
        self.freepath = freepath  #解压路径

    def extract_7z(self,input_file, output_dir):
        """
        解压7z格式的压缩文件。
        
        参数:
        input_file: 输入的7z文件路径。
        output_dir: 解压的目标目录。
        """
        with py7zr.SevenZipFile(input_file, 'r') as archive:
            archive.extractall(output_dir)

    def check_file_exists(self,filepath):
        """
        检查文件是否存在。
        
        参数:
        filepath: 文件路径。
        
        返回:
        存在返回True，不存在返回False。
        """
        return os.path.exists(filepath)

    def compress_to_7z(self,input_dir, output_file):
        """
        压缩目录到7z格式。
        
        参数:
        input_dir: 需要压缩的目录路径。
        output_file: 压缩后的文件路径。
        """
        with py7zr.SevenZipFile(output_file, 'w') as archive:
            archive.writeall(input_dir, os.path.basename(input_dir))

    def compress(self):
        """
        压缩输入目录到指定的7z文件。
        
        如果输出文件已存在，则会提示文件已存在，不会重新压缩。
        """
        if self.check_file_exists(self.output_file):
            print(f"文件 '{self.output_file}' 已存在。")
        else:
            print(f"正在压缩目录: {self.input_file}")
            self.compress_to_7z(self.input_file, self.output_file)
            print("压缩完成")
        # 示例用法

    def extract(self):    
        """
        解压指定的7z文件到指定目录。
        
        如果输入文件不存在，则会提示文件不存在。
        """
        if self.check_file_exists(self.input_file):
            print(f"文件 '{self.input_file}' 存在。")
        else:
            print(f"文件 '{self.input_file}' 不存在。")
            print(f"解压文件路径: {self.output_file}")
            self.extract_7z(self.output_file, self.freepath)
            print("解压完成")