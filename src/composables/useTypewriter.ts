import { ref } from 'vue'

export function useTypewriter(speed: number = 50) {
  const displayedText = ref('')
  const isTyping = ref(false)

  const start = async (content: string) => {
    isTyping.value = true
    displayedText.value = ''
    
    for (let i = 0; i < content.length; i++) {
      displayedText.value += content[i]
      await new Promise(resolve => setTimeout(resolve, speed))
    }
    
    isTyping.value = false
  }

  const reset = () => {
    displayedText.value = ''
    isTyping.value = false
  }

  return {
    displayedText,
    isTyping,
    start,
    reset
  }
}
