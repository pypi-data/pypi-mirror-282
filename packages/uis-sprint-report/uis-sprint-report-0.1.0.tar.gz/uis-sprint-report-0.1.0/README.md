# Project Overview

This project leverages the capabilities of the LangChain library to interact with GitLab issues and generate sprint report presentations. The system retrieves issue data from a specified GitLab group, processes the information, and summarizes the status of sprint goals in a PowerPoint presentation.

## Features

- Retrieve issues from GitLab using a specific label and iteration ID.
- Analyze and categorize issues based on sprint goals.
- Generate summaries and status reports for sprint goals.
- Create PowerPoint presentations to visually present the sprint report.

## Prerequisites

Before you can run this project, you need to have Python installed on your machine. Python 3.6 or higher is recommended. You also need to ensure that Git is installed if you need to clone the repository.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://gitlab.developers.cam.ac.uk/ee345/demo.git
   cd demo
   ```

2. **Install Required Libraries**:
   Ensure you have `pip` installed and then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and Setup Ollama Model**:
   Download the Ollama model from [Ollama Download](https://ollama.com/download) and [Mistral Model](https://ollama.com/library/mistral). Follow the instructions on the Ollama website for setting up the model.

## Usage

To run the script, use the following command. Replace the placeholder values with actual data like the GitLab access token and other parameters as required:

```bash
python main.py --token YOUR_GITLAB_ACCESS_TOKEN --gitlab_url https://gitlab.developers.cam.ac.uk/api/v4 --iteration_id=368 --goals "Front End Error Reporting,Gain access to account data (held in Entra ID and in our own systems) to start to understand user breakdown/profiles between Raven/Azure"
```

### Parameters Description

- `--token`: GitLab access token for authentication. This is necessary to access the GitLab API securely.
- `--gitlab_url`: The base URL of your GitLab instance API. Default is `https://gitlab.developers.cam.ac.uk/api/v4`.
- `--group_id`: The ID of the GitLab group from which issues are to be fetched. Default is `5`.
- `--labels`: URL-encoded string of labels used to filter issues by specific criteria. Default is `team%3A%3AIdentity`.
- `--iteration_id`: The ID of the specific iteration to filter issues relevant to a particular sprint. Leave empty if not using iteration-based filtering.
- `--goals`: A comma-separated list of sprint goals to analyze. Each goal should be clearly defined.
- `--presentation_name`: The name of the output PowerPoint file where the sprint report will be saved. Default is `demo.pptx`.
- `--chunk_size`: The size of text chunks in characters when splitting documents for processing. Default is `500`.
- `--chunk_overlap`: The overlap of text chunks in characters when splitting documents. Default is `0`.
- `--search_type`: The type of search to perform when retrieving documents. Default is `mmr` which stands for Maximal Marginal Relevance.
- `--search_kwargs`: Additional keyword arguments in JSON format to configure the search behavior. Default is `{"k": 8}`, where `k` is the number of documents to retrieve.
- `--cache_folder`: The directory to use for caching data such as embeddings. Default is `cache`.
- `--model`: The language model to use, specified by name. Default is `mistral`.
- `--max_tokens`: The maximum number of tokens to generate from the language model in a single request. Default is `1500`.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
