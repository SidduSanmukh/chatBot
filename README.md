# ChatBot

A versatile chatbot application built with Python, leveraging multiple AI models including Google Generative AI (Gemini) and Hugging Face models. This project demonstrates integration with LangChain for seamless AI interactions, supporting both streaming and non-streaming responses.

## Features

- **Multi-Model Support**: Integrate with Google Gemini and Hugging Face models
- **Streaming Responses**: Real-time streaming of AI responses for better user experience
- **Modular Architecture**: Organized into chat models and embedding models for extensibility
- **Environment Configuration**: Secure API key management using `.env` files
- **LangChain Integration**: Utilizes LangChain for robust AI model interactions

## Installation

### Prerequisites

- Python 3.13 or higher
- A virtual environment manager (recommended: `venv` or `uv`)

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd chatBot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```
   Or if using `uv`:
   ```bash
   uv pip install -e .
   ```

## Configuration

Create a `.env` file in the root directory with your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

- **Google API Key**: Obtain from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Hugging Face Token**: Get from [Hugging Face Settings](https://huggingface.co/settings/tokens)

## Usage

### Running the Google Gemini Chatbot

```bash
python chatModels/chatBot.py
```

This will start an interactive chat session using Google Gemini 2.5 Flash model with streaming responses.

### Running the Hugging Face Chatbot

```bash
python chatModels/huggingFaceModels/huggingFace.py
```

This uses the DeepSeek-V4-Pro model from Hugging Face for chat interactions.

### Main Entry Point

```bash
python main.py
```

Currently prints a simple greeting. Expand this for more functionality.

## Project Structure

```
chatBot/
├── main.py                 # Main entry point
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Additional requirements (if any)
├── README.md               # This file
├── chatModels/             # Chat model implementations
│   ├── chatBot.py          # Google Gemini chatbot
│   └── huggingFaceModels/
│       └── huggingFace.py  # Hugging Face chatbot
└── embeddingModels/        # Placeholder for embedding models
```

## Dependencies

- `google-generativeai`: Google Generative AI SDK
- `langchain`: Framework for LLM applications
- `langchain-google-genai`: LangChain integration for Google AI
- `langchain-huggingface`: LangChain integration for Hugging Face
- `mistralai`: Mistral AI integration (for future use)
- `python-dotenv`: Environment variable management

## Development

### Adding New Models

1. Create a new file in `chatModels/` or subfolders
2. Implement the chatbot logic using LangChain or direct API calls
3. Ensure environment variables are properly loaded
4. Update this README with usage instructions

### Testing

Run the chatbots manually and verify responses. Add unit tests for core functionality as the project grows.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter issues:

1. Check that your `.env` file is correctly configured
2. Ensure all dependencies are installed
3. Verify your API keys are valid and have appropriate permissions
4. Check the terminal output for error messages

For questions or contributions, please open an issue on the repository.
