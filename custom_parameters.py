"""
Custom Parameters Example
This script demonstrates using custom parameters like temperature and top_p
"""
import ollama

def main():
    # Generate response with custom parameters
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': 'Write a creative story opening in one sentence'
            }
        ],
        options={
            'temperature': 1.0,      # Higher = more creative (0.0 - 1.0)
            'top_p': 0.9,            # Nucleus sampling (0.0 - 1.0)
            'top_k': 40,             # Limits token selection
            'num_predict': 100,      # Max tokens to generate
        }
    )

    print("Creative response (high temperature):")
    print(response['message']['content'])
    print("\n" + "-" * 50 + "\n")

    # Generate response with conservative parameters
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': 'Write a creative story opening in one sentence'
            }
        ],
        options={
            'temperature': 0.1,      # Lower = more focused
            'top_p': 0.5,
        }
    )

    print("Conservative response (low temperature):")
    print(response['message']['content'])

if __name__ == '__main__':
    main()
