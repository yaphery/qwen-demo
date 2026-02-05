<script setup lang="ts">
import { ref, nextTick } from 'vue'
import ChatMessage from './ChatMessage.vue'

interface Message {
  id: string
  content: string
  isUser: boolean
  isLoading?: boolean
}

const messages = ref<Message[]>([
  {
    id: '1',
    content: '你好！我是通义千问，有什么可以帮助你的？',
    isUser: false
  }
])
const inputValue = ref('')
const isRequesting = ref(false)
const chatHistoryEl = ref<HTMLElement>()

let messageCounter = 1

const scrollToBottom = async () => {
  await nextTick()
  if (chatHistoryEl.value) {
    chatHistoryEl.value.scrollTop = chatHistoryEl.value.scrollHeight
  }
}

const addMessage = (content: string, isUser: boolean, isLoading = false) => {
  const newMessage: Message = {
    id: String(++messageCounter),
    content,
    isUser,
    isLoading
  }
  messages.value.push(newMessage)
  scrollToBottom()
  return newMessage
}

const updateMessage = (id: string, content: string) => {
  const message = messages.value.find(msg => msg.id === id)
  if (message) {
    message.content = content
    message.isLoading = false
  }
}

const askQwen = async () => {
  const prompt = inputValue.value.trim()
  if (!prompt) {
    alert('请输入问题！')
    return
  }

  inputValue.value = ''
  addMessage(prompt, true)
  isRequesting.value = true

  const loadingMsg = addMessage('', false, true)

  try {
    const response = await fetch('http://localhost:3000/api/ask-qwen', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    })

    if (!response.ok) {
      throw new Error(`请求失败：${response.status}`)
    }

    const data = await response.json()
    updateMessage(loadingMsg.id, data.answer)
  } catch (error) {
    const errorMsg = error instanceof Error ? error.message : '未知错误'
    updateMessage(loadingMsg.id, `请求出错：${errorMsg}`)
  } finally {
    isRequesting.value = false
  }
}

const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' && !isRequesting.value) {
    askQwen()
  }
}
</script>

<template>
  <div class="chat-container">
    <div class="chat-header">
      <h1>通义千问 - 前端聊天 Demo</h1>
    </div>
    <div ref="chatHistoryEl" class="chat-history">
      <ChatMessage
        v-for="msg in messages"
        :key="msg.id"
        :content="msg.content"
        :is-user="msg.isUser"
        :is-loading="msg.isLoading"
        @content-update="scrollToBottom"
      />
    </div>
    <div class="input-area">
      <input
        v-model="inputValue"
        type="text"
        class="msg-input"
        placeholder="输入你的问题（支持中文），比如：介绍一下前端开发"
        :disabled="isRequesting"
        @keydown="handleKeydown"
      />
      <button
        class="send-btn"
        :disabled="isRequesting"
        @click="askQwen"
      >
        {{ isRequesting ? '思考中...' : '发送' }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  max-width: 1400px;
  width: 100%;
  height: 90vh;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  background: white;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  overflow: hidden;
}

.chat-header {
  padding: 16px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

.chat-header h1 {
  margin: 0;
  font-size: 22px;
  font-weight: 600;
}

.chat-history {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  background-color: #f5f7fa;
}

.input-area {
  display: flex;
  gap: 10px;
  padding: 16px 20px;
  background: white;
  border-top: 1px solid #eee;
  flex-shrink: 0;
}

.msg-input {
  flex: 1;
  height: 48px;
  padding: 0 15px;
  border: 1px solid #ddd;
  border-radius: 24px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s;
}

.msg-input:focus {
  border-color: #667eea;
}

.msg-input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.send-btn {
  width: 100px;
  height: 48px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: opacity 0.3s;
}

.send-btn:hover:not(:disabled) {
  opacity: 0.9;
}

.send-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* 滚动条样式 */
.chat-history::-webkit-scrollbar {
  width: 6px;
}

.chat-history::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.chat-history::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.chat-history::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
