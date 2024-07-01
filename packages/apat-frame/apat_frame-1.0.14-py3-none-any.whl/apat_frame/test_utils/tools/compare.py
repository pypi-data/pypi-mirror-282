# 导入所需模块
from .commonpath import commonpath  # 从相对路径导入commonpath模块，用于获取通用路径
from PIL import Image  # 导入Image模块，处理图像文件
import os  # 操作系统相关功能
import aiofiles  # 异步文件操作库，提高I/O密集型任务的效率
import numpy as np  # 引入NumPy库，用于高效的数值计算，特别是图像处理中像素操作
import io  # 引入IO流模块，用于处理二进制数据如图像文件的读写

# 定义异步函数compare_images，用于比较两幅图像的像素差异并生成差异报告
async def compare_images(CaseMessage, img1_path, img2_path):
    """
    异步比较两个图像文件的相似度并生成差异图像。
    
    参数:
    - CaseMessage (dict): 用例元数据的字典，需包含'name'（用例名称）和'casecode'（用例编号）。
    - img1_path (str): 第一个图像文件的路径，通常是测试过程中捕获的图像。
    - img2_path (str): 第二个图像文件的路径，作为预期结果的参考图像。
    
    功能描述:
    1. 异步读取两个图像文件。
    2. 利用NumPy计算图像像素差异，生成差异图像。
    3. 计算并记录图像间的相似度。
    4. 根据相似度判断图像是否匹配，并准备详细的断言结果信息。
    5. 保存差异图像至指定路径。
    
    返回值:
    - data_list (list[dict]): 包含断言结果的字典列表，每个字典含有用例名、编号、相似度及图像路径等信息。
    """
    
    # 初始化结果列表，用于收集比较后的数据
    data_list = []

    # 调用commonpath模块中的函数以获取可能需要的通用路径信息
    # 注意：此处调用未直接使用返回值，可能是为了确保路径设置或作为副作用
    file_paths = commonpath()
    
    # 构建差异图像的保存路径，基于第一个图像路径并追加_diff.png
    path_parts = img1_path.split("_")  # 分割路径以插入_diff
    path_parts[-1] = "diff.png"  # 替换最后一部分为diff.png
    diff_path = "_".join(path_parts)  # 重新组合路径
    
    # 异步读取两个图像文件的二进制数据
    async with aiofiles.open(img1_path, mode='rb') as img1_file, \
            aiofiles.open(img2_path, mode='rb') as img2_file:
        # 读取图像文件的二进制数据
        img1_data = await img1_file.read()
        img2_data = await img2_file.read()
    
    # 使用BytesIO和PIL将二进制数据转换为NumPy数组
    img1_array = np.array(Image.open(io.BytesIO(img1_data)))
    img2_array = np.array(Image.open(io.BytesIO(img2_data)))
    
    # 复制img2_array以创建差异图像的基础
    diff_array = np.copy(img2_array)
    
    # 计算差异像素数量，并标记差异像素为红色
    num_diff_pixels = np.sum(img1_array != img2_array)
    # 设置差异像素颜色为红色
    diff_array[(img1_array != img2_array).any(axis=-1)] = [255, 0, 0]
    # 确保数组数据类型正确以便保存为图像
    diff_array = diff_array.astype(np.uint8)
    
    # 计算图像间的相似度（1-差异像素占比）
    deviation_rate = 1 - num_diff_pixels / (img1_array.size)
    
    # 保存差异图像到磁盘
    diff_image = Image.fromarray(diff_array)
    diff_image.save(diff_path)
    return deviation_rate
    
    # # 断言图像相似度是否达到预期（例如，至少99.95%相似）
    # try:
    #     assert deviation_rate >= 0.9995
    # except AssertionError:
    #     # 如果不满足条件，记录失败信息
    #     data = {
    #         "断言结果": "失败",
    #         "用例名": CaseMessage['name'],
    #         "用例编号": CaseMessage['casecode'],
    #         "相似度": deviation_rate,
    #         "期望图片": img2_path,
    #         "运行图片": img1_path,
    #         "对比图片": diff_path
    #     }
    #     data_list.append(data)
    # else:
    #     # 如果满足条件，记录成功信息
    #     data = {
    #         "断言结果": "成功",
    #         "用例名": CaseMessage['name'],
    #         "用例编号": CaseMessage['casecode'],
    #         "相似度": deviation_rate,
    #         "期望图片": img2_path,
    #         "运行图片": img1_path,
    #         "对比图片": diff_path
    #     }
    #     data_list.append(data)
    
    # # 最终返回包含断言结果的列表
    # return data_list













# Pillow (PIL): 这是一个强大的图像处理库，可以用来打开、操作和保存各种图像文件格式。在这里，它被用来将读取到的图像二进制数据转换成NumPy数组，这是进行像素级操作的前提。

# NumPy: 这是一个用于大规模数值计算的库，特别适合处理多维数组。在图像处理中，图像可以被视为一个三维数组（宽度x高度x颜色通道），NumPy使得高效地进行像素级运算成为可能，比如计算像素差异、统计不同像素的数量等。

# 为什么这样做
# 精确性：像素级对比是最直接的图像比较方式，能够精确到每一个像素点，非常适合那些需要高精度比对的场景，如UI测试、图像处理算法验证等。
# 灵活性：通过直接操作像素，可以自定义比较规则，比如忽略某些区域、调整颜色容差等，以适应不同的需求。
# 透明度：相比一些高级图像比较算法，像素级对比的逻辑直观易懂，便于调试和理解。
# 这样做的好处
# 控制权：提供了对图像比较过程的细粒度控制，可以根据具体需求调整比较策略。
# 性能：虽然直接处理像素可能会比某些高级算法消耗更多计算资源，但在许多情况下，尤其是图像尺寸不是非常大的时候，这种直接方法的执行速度仍然是可接受的，且借助NumPy这样的库能有效提升效率。
# 准确性：对于需要极高精度的场景，像素级对比是最直接且最准确的方法。
# 最佳实践例子
# 以下是一个简化的例子，展示如何使用Pillow和NumPy进行基本的像素对比：

# python
# from PIL import Image
# import numpy as np

# def compare_pixel_difference(image_path1, image_path2, tolerance=0):
#     """
#     比较两个图像的像素差异，如果差异像素数小于tolerance则认为图像相同。
    
#     参数:
#     - image_path1, image_path2: 图像文件路径
#     - tolerance: 允许的最大差异像素数，默认为0，意味着要求完全相同
    
#     返回:
#     - 是否相似 (bool), 差异像素数 (int)
#     """
#     # 加载图像并转换为NumPy数组
#     img1 = np.array(Image.open(image_path1))
#     img2 = np.array(Image.open(image_path2))
    
#     # 计算不同像素的数量
#     diff = np.sum(img1 != img2)
    
#     # 判断并返回结果
#     are_similar = diff <= tolerance
#     return are_similar, diff

# # 使用示例
# image1 = 'path/to/image1.png'
# image2 = 'path/to/image2.png'
# is_same, diff_count = compare_pixel_difference(image1, image2, tolerance=100)
# print(f"图像是否相似: {is_same}, 差异像素数: {diff_count}")
# 这个例子展示了如何加载两张图片，将其转换为NumPy数组后直接比较像素差异，并根据差异像素的数量判断图像是否相似。通过调整tolerance参数，可以控制对“相似”的定义，从而适应不同的比较需求。

# 在上述代码中，主要使用了Pillow库（别名PIL）和NumPy库的一些方法来处理图像数据。下面详细解释这些方法及其作用：

# Pillow (PIL) 相关方法
# 1. Image.open()
# 作用：此方法用于从给定的路径或文件对象中打开一个图像文件。它返回一个Image对象，该对象代表了图像数据，可以进一步进行处理，如显示、裁剪、旋转、转换格式等。
# 为何使用：在进行像素级比较之前，首先需要将图像文件加载到内存中。Image.open()是Pillow库中用于此目的的标准方法，它支持多种图像格式，是处理图像数据的起点。
# 2. Image.fromarray()
# 作用：此方法将一个NumPy数组转换为Image对象。这对于在进行了像素级别的操作之后，需要将修改后的数组数据再次转换回图像格式以便保存或显示时非常有用。
# 为何使用：在计算出差异像素并标记它们之后，需要将这个差异数组转换回图像格式保存为文件，因此使用Image.fromarray()完成这一转换步骤。
# NumPy 相关方法
# 1. np.array()
# 作用：此方法用于将输入数据转换为NumPy数组。当输入是Pillow的Image对象时，它会将图像数据转换为一个NumPy数组，数组的形状反映了图像的宽度、高度和颜色通道数。
# 为何使用：NumPy数组提供了高效的数学和逻辑运算，是进行像素级操作的理想数据结构。将图像转换为NumPy数组后，可以方便地进行像素值的访问和修改，这对于计算图像差异至关重要。
# 2. != 操作符
# 作用：在NumPy数组中，!=操作符用于元素级比较，它会逐元素地比较两个数组，返回一个布尔数组，其中True表示对应位置的元素不相等。
# 为何使用：在比较两幅图像的像素时，通过逐元素比较两个图像数组，可以快速找出所有不同的像素位置，这是计算图像差异的基础。
# 3. np.sum()
# 作用：此方法计算数组中所有元素的总和。当应用于布尔数组时，它实际上是在计数数组中True值的数量。
# 为何使用：在像素比较后得到的布尔差异数组上应用np.sum()，可以计算出不同像素的总数，这有助于评估两幅图像的相似度。
# 4. astype(np.uint8)
# 作用：此方法用于将数组的数据类型转换为无符号8位整数（uint8）。在图像处理中，像素值通常存储为uint8类型，因为它足够表示0到255之间的整数，涵盖了常见的RGB颜色值范围。
# 为何使用：在进行像素修改（如标记差异像素为红色）后，确保数组的数据类型与图像处理的标准相符是很重要的，这样才能正确保存和显示图像。
# 综上所述，使用这些方法是因为它们结合了Pillow的图像处理能力和NumPy的高效数值计算能力，使得在Python中进行像素级图像比较变得直接且高效。