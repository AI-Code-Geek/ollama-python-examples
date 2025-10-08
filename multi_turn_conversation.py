"""
Multi-turn Conversation Example
This script demonstrates maintaining context across multiple messages
"""
import ollama

def main():
    # Initialize conversation history
    messages = []

    # First message
    messages.append({
        'role': 'user',
        'content': 'My name is Alice and I love hiking'
    })

    response = ollama.chat(
        model='llama3.2',
        messages=messages
    )

    print("Assistant:", response['message']['content'])
    messages.append(response['message'])

    # Second message - model should remember context
    messages.append({
        'role': 'user',
        'content': 'What is my name and what do I enjoy?'
    })

    response = ollama.chat(
        model='llama3.2',
        messages=messages
    )

    print("\nAssistant:", response['message']['content'])

if __name__ == '__main__':
    main()
