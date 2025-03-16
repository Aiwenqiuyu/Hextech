import os
import json
import openai
import requests
from openai import OpenAI
# 旧的导入方式
# from langchain.tools import WebScraper

# 新的导入方式
#from langchain_community.tools import WebScraper
# 或者
from langchain_community.tools.playwright import WebScraper
# 测试qwen访问
class Test:
    def __init__(self):
        pass
    
    def test_qwen(self, prompt, model="qwen-plus"):
        """
        使用阿里云百炼API发送请求并获取回复
        
        参数:
            prompt (str): 发送给模型的提示文本
            model (str): 使用的模型名称，默认为qwen-plus
            
        返回:
            str: 模型的回复文本
        """
        client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key="sk-0093051937df469db157c1dfb848c5cf", 
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        try:
            # 创建聊天完成请求
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
                stream=False,
                temperature=0.7,
                max_tokens=1000,
                top_p=0.8
            )
            
            # 提取回复文本
            reply = completion.choices[0].message.content
            return reply
            
        except Exception as e:
            return f"访问API失败: {str(e)}"
    
    def test_langchain_web(self,url:str):
        # 创建一个 WebScraper 实例
        scraper = WebScraper()

        # 指定要抓取的网页 URL
        url = url

        # 使用 WebScraper 获取网页数据
        result = scraper.scrape(url)

        # 打印抓取到的数据
        return result

if __name__ == '__main__':
    test = Test()
    print(test.test_qwen("你好，请问有什么可以帮助您的吗？"))
    print(test.test_langchain_web("https://www.baidu.com"))