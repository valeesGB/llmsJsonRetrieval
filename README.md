
# LLMs JSON Retrieval

**LLMs JSON Retrieval** is a Python-based tool designed to automate the extraction of structured JSON data from text or web content using Large Language Models(LLMs) in local using Ollama. It handles the pipeline of fetching data, querying an LLM, and validating the output against defined schemas.

## 🚀 Features

- **Web Content Fetching**: Retrieve content from URLs using `wgetter.py`.
- **LLM Integration**: Seamlessly interface with Large Language Models via `llmcall.py`.
- **Structured Data**: Define target JSON schemas and data models in `json_structures.py`.
- **Validation**: Ensure LLM outputs are valid and strictly follow the defined structure using `validation_structure.py`.
- **Project Management**: Built with modern Python tooling using `uv` for fast and reliable dependency management.

## 📂 Project Structure

```text
├── cleaning_folders.py      # Utility script to clean up temporary folders/files
├── firstprototype.py        # Initial prototype script (deprecated/for reference)
├── json_retrieval.py        # Main logic for orchestrating the retrieval process
├── json_structures.py       # Definitions of JSON schemas/Pydantic models
├── llmcall.py               # wrapper for LLM API calls (e.g., OpenAI, Anthropic)
├── validation_structure.py  # Logic to validate the LLM's JSON output
├── wgetter.py               # Module for downloading/fetching web content
├── pyproject.toml           # Project configuration and dependencies
└── uv.lock                  # Lock file for dependencies
```

## 🛠️ Prerequisites

- **Python**: Version 3.10 or higher (implied by modern tooling).
- **uv**: This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/valeesGB/llmsJsonRetrieval.git
   cd llmsJsonRetrieval
   ```

2. **Install dependencies using `uv`:**
   ```bash
   uv sync
   ```
   *Alternatively, if you are not using `uv`, you can install dependencies via pip (if a requirements.txt is generated) or manually based on `pyproject.toml`.*

## ⚙️ Configuration

Set the following variables in `json_retreval.py`:
   ```env
   image_folder = 'your_image_folder'
   raw_text_folder = 'your_folder_for_raw_text'
   json_folder = 'your_json_folder'
   ocr_model = "you_ocr_model" #By default it is deepseek-ocr
   logic_model = "your_logic_model" #It is the model responsible for formatting and outputting the json
   ```

## 🏃 Usage

To run the main retrieval process:

```bash
uv run json_retrieval.py
```

## 🤝 Contributing

Contributions are welcome! If you have ideas for improving the model architecture, optimizing the reward function, or fixing bugs, feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Author**: [valeesGB](https://github.com/valeesGB)
