## Disclaimer!
As many people keep creating issues:
do not run "pip install telegram"
it is not meantioned anywhere!

## Telegram Plugin for Start-GPT

A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal.
Making Start-GPT a more user-friendly application to interact with.


## SETUP
First setup a telegram bot by following the instructions here: https://core.telegram.org/bots#6-botfather

To get the chat_id just start start-gpt and follow the instructions in the terminal.

Then set the following variables in your .env:
```
TELEGRAM_API_KEY=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-telegram-bot-chat-id

ALLOWLISTED_PLUGINS=StartGPTTelegram
CHAT_MESSAGES_ENABLED=True

````
within your .env file.
Also keep in mind to use the official documentation on how to use plugins. 


<img src="https://user-images.githubusercontent.com/11997278/233675629-fb582ab6-f89f-4837-82c4-c21744427266.png" width="30%" height="30%"> <img src="https://user-images.githubusercontent.com/11997278/233675683-eea9dd74-1c5e-436a-b745-95dff17c4951.png" width="30%" height="30%">

# Running Start-GPT with this plugin

To run this plugin, zip this repo and put it under Start-GPT/plugins/
To run it, add the following to your start command:
```
For non docker:
python -m startgpt --install-plugin-deps

For Docker:
docker-compose run --rm start-gpt --install-plugin-deps
```

# Start-GPT-Plugins

Plugins for Start-GPT

Clone this repo into the plugins direcory of [Start-GPT](https://github.dev/khulnasoft/Start-GPT)

For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

| Plugin   | Description                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------|
| Telegram | StartGPT is capable of asking/prompting the user via a Telegram Chat bot and also responds to commands and messages. |

