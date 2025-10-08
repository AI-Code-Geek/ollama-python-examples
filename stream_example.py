"""
Simple Ollama Streaming Example
This script demonstrates streaming responses from Ollama
"""
import ollama

def main():
    # Stream the response chunk by chunk
    stream = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': 'Explain quantum computing in simple terms'
            }
        ],
        stream=True
    )

    # Print each chunk as it arrives
    print("Streaming response:")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    print()  # New line at the end

if __name__ == '__main__':
    main()
