"""
List Available Models Example
This script shows how to list all available Ollama models
"""
import ollama

def main():
    # Get list of all available models
    models = ollama.list()

    print("Available Ollama Models:")
    print("-" * 50)

    # Display each model
    for model in models['models']:
        print(f"Name: {model.model}")
        print(f"Size: {model.size / (1024**3):.2f} GB")
        print(f"Modified: {model.modified_at}")
        print("-" * 50)

if __name__ == '__main__':
    main()
