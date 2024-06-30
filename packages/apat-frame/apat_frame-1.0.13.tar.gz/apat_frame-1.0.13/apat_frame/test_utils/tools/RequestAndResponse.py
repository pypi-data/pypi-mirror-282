import aiofiles
import re
import base64
import os
from .commonpath import commonpath
import json

class Handler:
    """
    请求处理类，用于处理和记录HTTP请求和响应。
    """
    
    def __init__(self, context):
        """
        初始化处理器，绑定上下文。
        
        :param context: 请求上下文对象，用于获取和设置请求相关的信息。
        """
        self.context = context
        self.request_data_list = []  # 用于存储请求的相关数据。

    async def edit_request(self, route, request):
        """
        在请求发送前进行修改。
        
        :param route: 请求路由对象，用于继续发送修改后的请求。
        :param request: 原始请求对象。
        """
        # 根据请求URL确定Sec-Fetch-Site的值。
        # 动态确定 Sec-Fetch-* 头的值
        sec_fetch_site = 'cross-site' if 'otherdomain.com' in request.url else 'same-origin'
        # 根据请求类型确定Sec-Fetch-Mode的值。
        sec_fetch_mode = 'navigate' if request.resource_type == 'document' else 'no-cors'
        # 根据请求类型确定Sec-Fetch-User的值。
        sec_fetch_user = '?1' if request.resource_type == 'document' else ''
        # 直接使用请求的resource_type作为Sec-Fetch-Dest的值。
        sec_fetch_dest = request.resource_type
        
        # 构造Sec-CH-UA系列头部的值。
        # 动态构造 Sec-CH-UA 请求头的值
        sec_ch_ua = '"Not A Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"'
        sec_ch_ua_mobile = '?0'
        sec_ch_ua_platform = '"macOS"'

        # 修改请求头。
        # 修改请求头
        modified_headers = {
            **request.headers,
            'Sec-Fetch-Site': sec_fetch_site,
            'Sec-Fetch-Mode': sec_fetch_mode,
            'Sec-Fetch-User': sec_fetch_user,
            'Sec-Fetch-Dest': sec_fetch_dest,
            'Sec-CH-UA': sec_ch_ua,
            'Sec-CH-UA-Mobile': sec_ch_ua_mobile,
            'Sec-CH-UA-Platform': sec_ch_ua_platform,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        # 获取所有cookies并记录请求信息。
        all_cookies = await self.context.cookies(request.url)
        request_data = {
            "request_info": {
                "url": request.url,
                "method": request.method,
                "headers": dict(request.headers),
                "cookies": all_cookies
            }
        }
        
        # 将请求信息添加到列表中。
        # 将当前请求数据添加到列表中
        self.request_data_list.append(request_data)

        # 继续处理请求，使用修改后的头部。
        # 继续请求并应用修改后的头
        await route.continue_(headers=modified_headers)

    async def get_base64_img(self, casecode):
        """
        从请求数据中提取base64编码的图片并保存到文件。
        
        :param casecode: 用例代码，用于标识和区分不同的测试用例。
        """
        # 反转请求数据列表，以便按照请求的顺序处理。
        # 将request_data_list倒序排列并保存到另一个临时变量
        list = self.request_data_list[::-1]
        image_count = 0  # 用于计数成功保存的图片数量。
        for request_data in list:
            if request_data['casecode'] == casecode:
                # 从URL中提取base64编码的图片信息。
                url_match = re.match(r"data:image/(\w+);base64,(.*)", request_data["request_info"]["url"])
                if url_match:
                    image_count += 1
                    img_type = url_match.group(1)
                    img_data = url_match.group(2)
                    # 构造图片文件名。
                    img_path = os.path.join(commonpath.get_log_path(), f'{casecode}1.jpg')
                    # 将base64编码的图片数据保存到文件。
                    async with aiofiles.open(img_path, 'wb') as file:
                        await file.write(base64.b64decode(img_data))
                    if image_count == 2:
                        break

    async def handle_request(self, route, casecode):
        """
        处理请求事件，记录请求信息。
        
        :param route: 请求路由对象，用于继续发送请求。
        :param casecode: 用例代码，用于标识和区分不同的测试用例。
        """
        request = route.request
        # 获取所有cookies并记录请求信息。
        all_cookies = await self.context.cookies(request.url)
        request_data = {
            "casecode": casecode,
            "request_info": {
                "url": request.url,
                "method": request.method,
                "headers": dict(request.headers),
                "cookies": all_cookies
            }
        }
        
        # 将请求信息添加到列表中。
        # 将当前请求数据添加到列表中
        self.request_data_list.append(request_data)
        # await route.continue_()  # 继续处理请求。

    async def handle_response(self, response):
        """
        处理响应事件，记录响应信息。
        
        :param response: 响应对象。
        """
        all_cookies = await self.context.cookies(response.url)
        # 获取响应文件的保存路径。
        response_file_path = commonpath.get_request_log_dir
        # 记录响应的URL、状态码、头信息和响应体到文件。
        async with aiofiles.open(response_file_path, 'a') as file:
            await file.write(f"context上下文: {self.context}\n")
            await file.write(f"    响应 URL: {response.url}\n")
            await file.write(f"    状态码: {response.status}\n")
            await file.write(f"    响应头: {response.headers}\n")
            try:
                response_body = await response.body()
                await file.write(f"    响应体: {response_body.decode('utf-8', errors='ignore')}\n")
            except Exception as e:
                await file.write(f"    获取响应体异常: {e}\n")
            await file.write(f"    响应时的所有 Cookies: {all_cookies}\n\n")