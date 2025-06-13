# AI-Powered Text Analysis and Chatbot

This repository contains two Streamlit-based web applications:
1. **MCQ Generator**: Generates multiple-choice questions (MCQs) from uploaded text files using text summarization and keyword extraction.
2. **Intelligent Assistant**: A chatbot powered by a local OpenAI-compatible model for answering user queries.

Both applications are designed to be user-friendly and extensible, suitable for educational tools, content analysis, or interactive AI assistants.

## Project Goals

- **MCQ Generator**: Automatically create MCQs from text documents by summarizing content, extracting keywords, and generating distractors using WordNet and ConceptNet. Users can select answers and save modified questions.
- **Intelligent Assistant**: Provide a conversational interface for users to interact with a local AI model, offering well-reasoned and helpful responses to queries.

## Tech Stack

-**Only Works on Linux Operating System (nltk dependencies)

### Frontend
- **Streamlit**: A Python framework for building interactive web applications with minimal effort.
- **HTML/CSS (implicit)**: Rendered by Streamlit for UI components.

### Backend
- **Python**: Primary language for both applications.
- **PyTorch**: Used for the BERT-based text summarization in the MCQ generator.
- **BERT Extractive Summarizer**: Summarizes text to focus on key content.
- **PKE (Python Keyphrase Extraction)**: Extracts keywords using MultipartiteRank.
- **NLTK**: Processes text for tokenization, stopwords, and WordNet-based distractors.
- **Flashtext**: Efficient keyword matching in sentences.
- **PyWSD**: Word sense disambiguation for generating relevant distractors.
- **Requests**: Fetches distractors from ConceptNet API.
- **OpenAI Client**: Interfaces with a local LLM for the chatbot.
- **Local LLM (e.g., LLaMA)**: Provides responses for the chatbot (requires separate setup).

### Other Tools
- **pip**: Manages Python dependencies.
- **Git**: Version control for the repository.

## Prerequisites

- **Python 3.8+**: Required for running the applications.
- **pip**: Python package manager.
- **Local LLM Server**: For the chatbot, a local model server (e.g., LM Studio) running at `http://localhost:1234/v1`.
- **NLTK Data**: Download required NLTK corpora (see Installation).
- **Git**: For cloning the repository.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**
   Run the following in a Python shell:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('averaged_perceptron_tagger')
   ```

5. **Set Up Local LLM (for Chatbot)**
   - Install a local LLM server (e.g., LM Studio).
   - Ensure it runs at `http://localhost:1234/v1` with a compatible model loaded.
   - No API key is required (set to "not-needed").

## Running the Applications

### MCQ Generator
1. Navigate to the `mcq_generator` directory:
   ```bash
   cd mcq_generator
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open your browser at `http://localhost:8501`.
4. Upload a `.txt` file, adjust the compression ratio, and generate MCQs.
5. Select answers and save modified questions to `modified_questions.txt`.

### Intelligent Assistant
1. Ensure the local LLM server is running at `http://localhost:1234/v1`.
2. Navigate to the `chatbot` directory:
   ```bash
   cd chatbot
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at `http://localhost:8501`.
5. Enter queries in the text input to interact with the assistant.

## Project Structure

```
project/
├── mcq_generator/
│   ├── app.py              # Main Streamlit app for MCQ generator
│   ├── file_utils.py       # File reading utilities
│   ├── mcq_generator.py    # MCQ generation logic
│   ├── ui_components.py    # Streamlit UI components
├── chatbot/
│   ├── app.py              # Main Streamlit app for chatbot
│   ├── assistant.py        # Assistant response logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## Features

### MCQ Generator
- Upload `.txt` files for MCQ generation.
- Summarize text using BERT with adjustable compression ratio.
- Extract keywords using MultipartiteRank.
- Generate distractors via WordNet and ConceptNet.
- Display MCQs with radio button selection.
- Save modified questions with selected answers.

### Intelligent Assistant
- Conversational interface with a local LLM.
- Persistent chat history using Streamlit session state.
- Streamed responses for real-time interaction.
- Configurable system prompt for assistant behavior.

## Troubleshooting

- **MCQ Generator: "No MCQs generated"**
  - Ensure the uploaded text is long enough (>20 characters per sentence).
  - Check for valid keywords in the summarized text.
  - Verify internet access for ConceptNet API.

- **Chatbot: "Connection refused"**
  - Confirm the local LLM server is running at `http://localhost:1234/v1`.
  - Check the model is loaded correctly in the LLM server.

- **Dependency Issues**
  - Recreate the virtual environment and reinstall dependencies.
  - Ensure Python version is 3.8 or higher.

## Future Improvements

- **MCQ Generator**:
  - Support other file formats (e.g., PDF, DOCX).
  - Improve distractor quality with advanced NLP models.
  - Add question difficulty levels.
- **Chatbot**:
  - Support multiple LLM backends.
  - Add voice input/output.
  - Implement context-aware memory for longer conversations.
- **Integration**:
  - Combine with IP camera project for text analysis of video transcripts.
  - Add authentication for secure access.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.



## Contact

Open an issue on GitHub for questions or feedback.
