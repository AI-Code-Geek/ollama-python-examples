"""
Simple Ollama Generate Example
This script demonstrates text generation with Ollama
"""
import ollama

def main():
    # Generate a response to a prompt
    response = ollama.generate(
        model='llama3.2',
        prompt='Tell me a short joke about programming'
    )

    # Print the generated text
    print(response['response'])

if __name__ == '__main__':
    main()
