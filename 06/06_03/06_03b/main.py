from collections import deque

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://youtube.com")
history_stack.append("https://linkedin.com")

latest_history = history_stack[-1]
print(latest_history)

history_stack.pop()
print(history_stack)
