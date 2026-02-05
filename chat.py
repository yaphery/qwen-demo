"""简单的通义千问聊天Demo - Simple Qwen Chat Demo"""
from openai import OpenAI
import config


class QwenChat:
    """通义千问聊天类"""
    
    def __init__(self, api_key=None, model=None, system_prompt=None):
        """
        初始化聊天客户端
        
        Args:
            api_key: API密钥，如果为None则从配置文件读取
            model: 模型名称，如果为None则使用默认模型
            system_prompt: 系统提示词，如果为None则使用默认提示词
        """
        self.api_key = api_key or config.API_KEY
        self.model = model or config.DEFAULT_MODEL
        self.system_prompt = system_prompt or config.SYSTEM_PROMPT
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=config.BASE_URL
        )
        self.conversation_history = []
    
    def chat(self, user_message):
        """
        发送消息并获取回复
        
        Args:
            user_message: 用户消息
            
        Returns:
            AI回复的内容
        """
        # 构建消息列表
        messages = []
        
        # 只在首次对话时添加系统提示词
        if not self.conversation_history:
            messages.append({"role": "system", "content": self.system_prompt})
        
        # 添加对话历史
        messages.extend(self.conversation_history)
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": user_message})
        
        # 调用API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=config.MAX_TOKENS,
            temperature=config.TEMPERATURE
        )
        
        # 获取回复
        assistant_message = response.choices[0].message.content
        
        # 更新对话历史
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def reset(self):
        """重置对话历史"""
        self.conversation_history = []


def main():
    """主函数 - 简单的命令行聊天界面"""
    print("=" * 50)
    print("通义千问聊天Demo")
    print("=" * 50)
    print("输入 'quit' 或 'exit' 退出")
    print("输入 'reset' 重置对话")
    print("=" * 50)
    
    # 创建聊天实例
    chat = QwenChat()
    
    while True:
        try:
            # 获取用户输入
            user_input = input("\n你: ").strip()
            
            if not user_input:
                continue
            
            # 处理特殊命令
            if user_input.lower() in ['quit', 'exit']:
                print("再见！")
                break
            
            if user_input.lower() == 'reset':
                chat.reset()
                print("对话已重置")
                continue
            
            # 获取AI回复
            response = chat.chat(user_input)
            print(f"\nAI: {response}")
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误: {str(e)}")


if __name__ == "__main__":
    main()
