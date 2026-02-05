# qwen-demo
通义千问聊天 Demo

一个简单的通义千问（Qwen）聊天应用示例。

## 功能特点

- 简单易用的命令行聊天界面
- 支持对话历史管理
- 支持重置对话
- 使用 OpenAI 兼容接口

## 安装

1. 克隆仓库
```bash
git clone https://github.com/yaphery/qwen-demo.git
cd qwen-demo
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置 API Key
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 DashScope API Key
```

获取 API Key: https://dashscope.console.aliyun.com/apiKey

## 使用方法

运行聊天程序：
```bash
python chat.py
```

### 命令说明

- 直接输入文本进行对话
- 输入 `reset` 重置对话历史
- 输入 `quit` 或 `exit` 退出程序

## 示例代码

```python
from chat import QwenChat

# 创建聊天实例
chat = QwenChat()

# 发送消息
response = chat.chat("你好，请介绍一下自己")
print(response)

# 继续对话（保留上下文）
response = chat.chat("你能做什么？")
print(response)

# 重置对话
chat.reset()

# 使用自定义系统提示词
chat_custom = QwenChat(system_prompt="你是一个Python专家")
response = chat_custom.chat("如何读取文件？")
print(response)
```

## 配置说明

在 `config.py` 中可以自定义：
- `DEFAULT_MODEL`: 使用的模型（默认: qwen-plus）
- `MAX_TOKENS`: 最大生成token数（默认: 1500）
- `TEMPERATURE`: 温度参数（默认: 0.7）
- `SYSTEM_PROMPT`: 系统提示词

## 许可证

MIT
