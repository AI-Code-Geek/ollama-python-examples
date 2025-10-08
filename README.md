# Ollama Python Examples

Simple and easy-to-understand Python examples for working with Ollama.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure Ollama is running** and you have the `llama3.2` model installed:
   ```bash
   ollama pull llama3.2
   ```

## Examples

### 1. Chat Example (`chat_example.py`)
Basic chat functionality with Ollama.
```bash
python chat_example.py
```

### 2. Generate Example (`generate_example.py`)
Simple text generation using a prompt.
```bash
python generate_example.py
```

### 3. Stream Example (`stream_example.py`)
Streaming responses chunk by chunk in real-time.
```bash
python stream_example.py
```

### 4. Multi-turn Conversation (`multi_turn_conversation.py`)
Demonstrates maintaining context across multiple messages.
```bash
python multi_turn_conversation.py
```

### 5. List Models (`list_models.py`)
Lists all available Ollama models on your system.
```bash
python list_models.py
```

### 6. Custom Parameters (`custom_parameters.py`)
Shows how to use custom parameters like temperature and top_p.
```bash
python custom_parameters.py
```

## Requirements

- Python 3.7+
- Ollama installed and running
- `ollama` Python package (installed via requirements.txt)

## Notes

- All examples use the `llama3.2` model by default
- You can change the model name in each file to use different models
- Make sure Ollama service is running before executing the examples
