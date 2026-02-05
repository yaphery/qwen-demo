"""配置文件 - Configuration file"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Qwen API 配置
API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 模型配置
DEFAULT_MODEL = "qwen-plus"
MAX_TOKENS = 1500
TEMPERATURE = 0.7

# 系统提示词
SYSTEM_PROMPT = "你是一个有帮助的AI助手。"
