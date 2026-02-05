"""使用示例 - Usage Examples"""
from chat import QwenChat


def example_simple_chat():
    """简单对话示例"""
    print("=" * 50)
    print("示例1: 简单对话")
    print("=" * 50)
    
    chat = QwenChat()
    
    # 第一轮对话
    print("\n用户: 你好")
    response = chat.chat("你好")
    print(f"AI: {response}")
    
    # 第二轮对话（保留上下文）
    print("\n用户: 1+1等于几？")
    response = chat.chat("1+1等于几？")
    print(f"AI: {response}")


def example_with_system_prompt():
    """自定义系统提示词示例"""
    print("\n" + "=" * 50)
    print("示例2: 自定义系统提示词")
    print("=" * 50)
    
    # 使用自定义系统提示词初始化
    system_prompt = "你是一个专业的Python编程助手，请用简洁的方式回答问题。"
    chat = QwenChat(system_prompt=system_prompt)
    
    print("\n用户: 如何在Python中读取文件？")
    response = chat.chat("如何在Python中读取文件？")
    print(f"AI: {response}")


def example_reset():
    """重置对话示例"""
    print("\n" + "=" * 50)
    print("示例3: 重置对话")
    print("=" * 50)
    
    chat = QwenChat()
    
    print("\n用户: 我叫张三")
    response = chat.chat("我叫张三")
    print(f"AI: {response}")
    
    print("\n用户: 我叫什么名字？")
    response = chat.chat("我叫什么名字？")
    print(f"AI: {response}")
    
    # 重置对话
    print("\n[重置对话]")
    chat.reset()
    
    print("\n用户: 我叫什么名字？")
    response = chat.chat("我叫什么名字？")
    print(f"AI: {response}")


if __name__ == "__main__":
    print("注意: 这些示例需要有效的 API Key 才能运行")
    print("请确保已在 .env 文件中配置 DASHSCOPE_API_KEY\n")
    
    try:
        # 运行示例（如果API Key配置正确）
        example_simple_chat()
        example_with_system_prompt()
        example_reset()
    except Exception as e:
        print(f"\n错误: {str(e)}")
        print("\n提示: 请检查是否正确配置了 API Key")
