"""
Simple Ollama Chat Example
This script demonstrates basic chat functionality with Ollama
"""
import ollama

def main():
    # Send a chat message
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?'
            }
        ]
    )

    # Print the response
    print(response['message']['content'])

if __name__ == '__main__':
    main()
