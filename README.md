# LangGraph: Build Stateful Agentic AI Graph

A sophisticated AI chatbot application built with LangGraph, offering multiple LLM integrations and customizable use cases through an intuitive Streamlit interface.

## 🚀 Features

- **Multiple LLM Support**: Integration with Groq, OpenAI, HuggingFace, and Ollama
- **Flexible Architecture**: Modular design with state management and graph-based processing
- **Interactive UI**: User-friendly Streamlit interface with real-time chat functionality
- **Stateful Conversations**: Maintains conversation context using LangGraph's state management
- **Extensible Design**: Easy to add new chatbot types and functionalities

## 🛠️ Tech Stack

- **LangChain & LangGraph**: Core AI framework for building stateful agents
- **Streamlit**: Web interface for user interaction
- **Python 3.10+**: Programming language
- **FAISS**: Vector database for efficient similarity search
- **Tavily**: Web search integration

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langgrph
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

## 🚦 Usage

### Running the Application

```bash
python app.py
```

This will start the Streamlit application. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`).

### Using the Interface

1. **Select LLM Provider**: Choose from Groq, OpenAI, HuggingFace, or Ollama
2. **Configure Model**: Select specific model options (e.g., llama3-8b-8192, gemma2-9b-it for Groq)
3. **Choose Use Case**: Pick from Basic Chatbot, Advanced Chatbot, or Custom Chatbot
4. **Enter API Key**: Provide the required API key for your selected LLM
5. **Start Chatting**: Type your message and interact with the AI

## 🏗️ Project Structure

```
langgrph/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── src/
    ├── main.py                     # Core application logic
    ├── graph/
    │   └── graph_builder.py        # LangGraph construction and management
    ├── LLMS/
    │   └── groqllm.py             # LLM integrations
    ├── nodes/
    │   └── basic_chatbot_node.py   # Graph node implementations
    ├── state/
    │   └── state.py               # State management for conversations
    ├── tools/                      # Custom tools and utilities
    └── ui/
        ├── uiconfig.ini           # UI configuration
        ├── uiconfig.py            # UI settings management
        └── streamlitui/
            ├── display_message.py # Message display components
            └── loadui.py          # UI loading and configuration
```

## 🔧 Configuration

The application can be configured through the `src/ui/uiconfig.ini` file:

- **PAGE_TITLE**: Customize the application title
- **LLM_OPTIONS**: Available LLM providers
- **USECASE_OPTIONS**: Supported chatbot types
- **GROQ_MODEL_OPTIONS**: Available Groq models

## 🤖 Supported Use Cases

### Basic Chatbot
A straightforward conversational AI that can answer questions and engage in general dialogue.

### Advanced Chatbot
Enhanced chatbot with additional capabilities and more sophisticated response generation.

### Custom Chatbot
Flexible chatbot configuration allowing for specialized use cases and custom behaviors.

## 🧩 Extending the Application

### Adding New LLM Providers

1. Create a new LLM integration in `src/LLMS/`
2. Update the configuration in `uiconfig.ini`
3. Modify the LLM selection logic in `main.py`

### Adding New Chatbot Types

1. Create a new node in `src/nodes/`
2. Update the graph builder in `src/graph/graph_builder.py`
3. Add the new use case to the configuration

### Custom Tools Integration

Add new tools in the `src/tools/` directory and integrate them into your graph nodes.

## 📋 Requirements

- Python 3.10 or higher
- Valid API keys for chosen LLM providers
- Internet connection for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- UI powered by [Streamlit](https://streamlit.io/)
- Inspired by the growing ecosystem of AI agent frameworks

---

**Happy Coding! 🎉**