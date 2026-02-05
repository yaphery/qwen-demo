<script setup lang="ts">
import { watch } from 'vue'
import { useTypewriter } from '../composables/useTypewriter'

interface Props {
  content: string
  isUser: boolean
  isLoading?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  isLoading: false
})

const emit = defineEmits<{
  contentUpdate: []
}>()

const { displayedText, start, reset } = useTypewriter(30)

// 监听内容变化，触发打字机效果
watch(() => [props.content, props.isLoading] as const, ([newContent, newIsLoading]) => {
  if (!props.isUser && !newIsLoading && newContent) {
    reset()
    start(newContent)
  }
}, { immediate: true })

// 监听打字机文本变化，通知父组件滚动
watch(displayedText, () => {
  if (!props.isUser && displayedText.value) {
    emit('contentUpdate')
  }
})
</script>

<template>
  <div :class="['message', isUser ? 'user-message' : 'ai-message']">
    <template v-if="isLoading">
      <div class="loading-container">
        <span class="loading-text"> 通义千问思考中</span>
        <span class="dots">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </span>
      </div>
    </template>
    <template v-else>
      <div class="message-content">{{ isUser ? content : displayedText }}</div>
    </template>
  </div>
</template>

<style scoped>
.message {
  margin: 10px 0;
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 8px;
  line-height: 1.6;
  word-break: break-word;
}

.message-content {
  white-space: pre-wrap;
}

.user-message {
  background: #4285f4;
  color: white;
  margin-left: auto;
}

.ai-message {
  background: #f1f3f4;
  color: #333;
  margin-right: auto;
}

.loading-container {
  display: flex;
  align-items: center;
  gap: 8px;
}

.loading-text {
  color: #999;
  font-style: italic;
}

.dots {
  display: flex;
  gap: 4px;
}

.dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: #999;
  animation: bounce 1.4s infinite;
}

.dot:nth-child(1) {
  animation-delay: -0.32s;
}

.dot:nth-child(2) {
  animation-delay: -0.16s;
}

@keyframes bounce {
  0%, 80%, 100% {
    opacity: 0.3;
    transform: translateY(0);
  }
  40% {
    opacity: 1;
    transform: translateY(-10px);
  }
}
</style>
