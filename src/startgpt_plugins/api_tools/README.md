# API Tools Plugin

The API Tools Plugin enables Start-GPT to communicate with APIs.

## Key Features:
- Supports GET, POST, PUT, DELETE, PATCH, HEAD and OPTIONS
- Tries to recover from strange values being used as parameters
- Accepts custom header values

## Installation:
As part of the StartGPT plugins package, follow the [installation instructions](https://github.com/khulnasoft/Start-GPT-Plugins) on the Start-GPT-Plugins GitHub reporistory README page.

## StartGPT Configuration
Set `ALLOWLISTED_PLUGINS=StartGPTApiTools,example-plugin1,example-plugin2,etc` in your StartGPT `.env` file.
