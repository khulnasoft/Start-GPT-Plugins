# Start-GPT-Plugins

> ⚠️💀 **WARNING** 💀⚠️:
> Always examine the code of any plugin you use thoroughly, as plugins can execute any Python code, leading to potential malicious activities such as stealing your API keys.

> ⚙️ **WORK IN PROGRESS** ⚙️:
> The plugin API is still being refined. If you are developing a plugin, expect changes in the upcoming versions.

## New in Start-GPT 0.4.1
- Unzipped plugins are now supported! You can now clone or download plugins directly from GitHub and place them in the `plugins` directory without zipping, as long as they are in the correct (NEW) format.
- Plugins settings have been moved out of the `.env` file to a new `plugins_config.yaml` file in the root directory of Start-GPT.
- `ALLOWLISTED_PLUGINS` and `DENYLISTED_PLUGINS` `.env` settings are deprecated and will be removed in a future release.
- Plugins must now be explicitly enabled in plugins. See the [installation](#installation) section for more details.
- The plugin format has changed. For now the old zip format is still supported, but will be removed in a future release. See the [plugin format](#plugin-format) section for more details.

### Note: The Start-GPT-Plugins repo must still be Zipped

> The core Start-GPT Plugins are still in the old format, and will need to be zipped as shown in the instructions below. **THEY WILL NOT WORK UNZIPPED**. This will be fixed in a future release.

## Installation

**_⚠️This is a work in progress⚠️_**

Here are the steps to configure Start-GPT Plugins. 

1. **Install Start-GPT**

   If you haven't done so, follow the installation instructions given by [Start-GPT](https://github.com/khulnasoft/Start-GPT) to install it.

1. **Download the plugins folder from the `root` of `Start-GPT` directory**

    To download it directly from your Start-GPT directory, you can run this command on Linux or MacOS:

    ```bash
    curl -L -o ./plugins/Start-GPT-Plugins.zip https://github.com/khulnasoft/Start-GPT-Plugins/archive/refs/heads/master.zip
    ```

    Or in PowerShell:

    ```pwsh
    Invoke-WebRequest -Uri "https://github.com/khulnasoft/Start-GPT-Plugins/archive/refs/heads/master.zip"     -OutFile "./plugins/Start-GPT-Plugins.zip"
    ```

1. **Execute the dependency install script for plugins**

    This can be run via:

    Linux or MacOS:

    ```bash
    ./run.sh --install-plugin-deps
    ```

   Windows:

    ```pwsh
   .\run.bat --install-plugin-deps
    ```

    Or directly via the CLI:

    ```bash
    python -m startgpt --install-plugin-deps
    ````

1. **Enable the plugins** 

    To activate a plugin, the user should create or edit the `plugins_config.yaml` file located in the root directory of Start-GPT. All plugin options can be configured in this file. 
    
    For example, if the `astro` plugin needs to be enabled, the following line should be added to the `plugins_config.yaml` file:
    ```yaml
    StartGPTSpacePlugin:
        config: {}
        enabled: true
    ```

1. **Alernate option to enable the plugins** (May cease to function at any point as the .env support for plugins may change)
   
   In your .env file add the lines below. If your plugins_config.yaml does not exist it should generate correctly when you run Start-GPT based on what you populate below.
   ```
   ################################################################################
   ### ALLOWLISTED PLUGINS
   ################################################################################

   #ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
   ALLOWLISTED_PLUGINS=StartGPTReddit

   DENYLISTED_PLUGINS=StartGPTBluesky,StartGPTTelegram,StartGPTEmailPlugin,StartGPTNewsSearch,PlannerPlugin,StartGPTSceneXPlugin,StartGPTTwitter,StartGPTWikipediaSearch,StartGPTWolframAlphaSearch,StartGPTSpacePlugin,StartGPTBaiduSearch,StartGPTBingSearch
   ```
   
## Plugins

There are two categories of plugins: **first party** and **third party**.

 **First-party plugins** are a curated list of widely-used plugins, and are included in this repo. They and are installed by default when the plugin platform is installed. See the [First Party Plugins](#first-party-plugins) section below for a comprehensive list.

 **Third-party plugins** need to be added individually. They may be useful for your specific needs. See the [Third Party Plugins](#third-party-plugins) section below for a short list of third-party plugins, and for information on how to add your plugin. Note: The Start-GPT community has developed numerous third-party plugins and this list doesn't include them all. See the [Community-contributed plugins directory](#community-contributed-plugins-directory) section below for a more comprehensive list.

### Community contributed plugins directory

Community member and contributor, **[@dylanintech](https://github.com/dylanintech/)**, maintains a [**growing directory**](https://autoplugins.vercel.app/) of **Start-GPT plugins and their contributors. To get your plugin listed in that directory, add your info to the `data` array in `plugins.tsx` of [his repo](https://github.com/dylanintech/autoplugins) and submit a PR. 

### First Party Plugins

You can see the first-party plugins below. These are included in this Start-GPT-Plugins repo and are installed by default when the plugin platform is installed.

| Plugin       | Description     | Location |
|--------------|-----------|--------|
| Astro Info   | This gives Start-GPT info about astronauts.                                                           | [startgpt_plugins/astro](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/astro)           |
| API Tools        | This allows Start-GPT to make API calls of various kinds.                                                           | [startgpt_plugins/api_tools](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/api_tools)           |
| Baidu Search |  This search plugin integrates Baidu search engines into Start-GPT. | [startgpt_plugins/baidu_search](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/baidu_search)|
| Bing Search      | This search plugin integrates Bing search engines into Start-GPT.                                                  | [startgpt_plugins/bing_search](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/bing_search)       |
| Bluesky | Enables Start-GPT to retrieve posts from Bluesky and create new posts. | [startgpt_plugins/bluesky](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/bluesky)|
| Email            | Revolutionize email management with the Start-GPT Email Plugin, leveraging AI to automate drafting and intelligent replies. | [startgpt_plugins/email](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/email)                 |
| News Search      | This search plugin integrates News Articles searches, using the NewsAPI aggregator into Start-GPT.                 | [startgpt_plugins/news_search](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/news_search)   |
| Planner          | Simple Task Planner Module for Start-GPT  | [startgpt_plugins/planner](https://github.com/khulnasoft/Start-GPT-Plugins/blob/master/src/startgpt_plugins/planner/) |
| Random Values    | Enable Start-GPT to generate various random numbers and strings.                                                    | [startgpt_plugins/random_values](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/random_values) |
| SceneX           | Explore image storytelling beyond pixels with the Start-GPT SceneX Plugin.                                        | [startgpt_plugins/scenex](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/scenex)               |
| SerpApi          | Search on a broad range of search engines supported by SerpApi and get rich information from the results.        | [startgpt_plugins/serpapi](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/serpapi)|
| Telegram |  A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal. | [startgpt_plugins/telegram](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/telegram) |
| Twitter          | Start-GPT is capable of retrieving Twitter posts and other related content by accessing the Twitter platform via the v1.1 API using Tweepy.               | [startgpt_plugins/twitter](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/twitter)           |
| Wikipedia Search | This allows Start-GPT to use Wikipedia directly.                                                                    | [startgpt_plugins/wikipedia_search](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/wikipedia_search) |
| WolframAlpha Search | This allows StartGPT to use WolframAlpha directly.                                                                                         | [startgpt_plugins/wolframalpha_search](https://github.com/khulnasoft/Start-GPT-Plugins/tree/master/src/startgpt_plugins/wolframalpha_search)|


### Third Party Plugins

Third-party plugins are created by contributors and are not included in this repository. For more information about these plugins, please visit their respective GitHub pages.

Here is a non-comprehensive list of third-party plugins. If you have a plugin you'd like to add to this list, please submit a PR.

| Plugin       | Description     | Repository |
|--------------|-----------------|-------------|
| Alpaca-Trading | Trade stocks and crypto, paper or live with Start-GPT | [danikhan632/Start-GPT-AlpacaTrader-Plugin](https://github.com/danikhan632/Start-GPT-AlpacaTrader-Plugin)|
| StartGPTReddit | Reddit Access | [NeonN3mesis/StartGPTReddit](https://github.com/NeonN3mesis/StartGPTReddit)|
| StartGPT User Input Request | Allow Start-GPT to specifically request user input in continous mode | [HFrovinJensen/Start-GPT-User-Input-Plugin](https://github.com/HFrovinJensen/Start-GPT-User-Input-Plugin)|
| BingAI | Enable Start-GPT to fetch information via BingAI, saving time, API requests while maintaining accuracy. This does not remove the need for OpenAI API keys | [gravelBridge/StartGPT-BingAI](https://github.com/gravelBridge/StartGPT-BingAI)|
| Crypto | Trade crypto with Start-GPT | [isaiahbjork/Start-GPT-Crypto-Plugin](https://github.com/isaiahbjork/Start-GPT-Crypto-Plugin)|
| Discord | Interact with your Start-GPT instance through Discord | [gravelBridge/StartGPT-Discord](https://github.com/gravelBridge/StartGPT-Discord)|
| Dolly StartGPT Cloner | A way to compose & run multiple Start-GPT processes that cooperate, till core has multi-agent support | [pr-0f3t/Start-GPT-Dolly-Plugin](https://github.com/pr-0f3t/Start-GPT-Dolly-Plugin)|
| Google Analytics | Connect your Google Analytics Account to Start-GPT. | [isaiahbjork/Start-GPT-Google-Analytics-Plugin](https://github.com/isaiahbjork/Start-GPT-Google-Analytics-Plugin)|
| IFTTT webhooks | This plugin allows you to easily integrate IFTTT connectivity using Maker | [AntonioCiolino/StartGPT-IFTTT](https://github.com/AntonioCiolino/StartGPT-IFTTT)|
| iMessage | Send and Get iMessages using Start-GPT | [danikhan632/Start-GPT-Messages-Plugin](https://github.com/danikhan632/Start-GPT-Messages-Plugin)|
| Instagram | Instagram access | [jpetzke/StartGPT-Instagram](https://github.com/jpetzke/StartGPT-Instagram)|
| Mastodon  | Simple Mastodon plugin to send toots through a Mastodon account | [ppetermann/StartGPTMastodonPlugin](https://github.com/ppetermann/StartGPTMastodonPlugin)|
| MetaTrader | Connect your MetaTrader Account to Start-GPT. | [isaiahbjork/Start-GPT-MetaTrader-Plugin](https://github.com/isaiahbjork/Start-GPT-MetaTrader-Plugin) |
| Mindware | The App Store for StartGPT. With one API key, unlock access to a growing list of plugins. | [open-mindware/StartGPT-Mindware](https://github.com/open-mindware/StartGPT-Mindware) |
| Notion      | Notion plugin for Start-GPT.  | [doutv/Start-GPT-Notion](https://github.com/doutv/Start-GPT-Notion) |
| Slack | This plugin allows to receive commands and send messages to slack channels | [adithya77/Start-GPT-slack-plugin](https://github.com/adithya77/Start-GPT-slack-plugin)
| Spoonacular | Find recipe insiprations using Start-GPT | [minfenglu/Start-GPT-Spoonacular-Plugin](https://github.com/minfenglu/Start-GPT-Spoonacular-Plugin)
| System Information      | This plugin adds an extra line to the prompt, serving as a hint for the AI to use shell commands likely supported by the current system. By incorporating this plugin, you can ensure that the AI model provides more accurate and system-specific shell commands, improving its overall performance and usefulness. | [hdkiller/Start-GPT-SystemInfo](https://github.com/hdkiller/Start-GPT-SystemInfo) |
| TiDB Serverless   | Connect your TiDB Serverless database to Start-GPT, enable get query results from database | [pingcap/Start-GPT-TiDB-Serverless-Plugin](https://github.com/pingcap/Start-GPT-TiDB-Serverless-Plugin)
| Todoist-Plugin | Allow Start-GPT to programatically interact with yor Todoist to create, update, and manage your Todoist | [danikhan632/Start-GPT-Todoist-Plugin](https://github.com/danikhan632/Start-GPT-Todoist-Plugin) |
| Weather | A simple weather plugin wrapping around python-weather | [ppetermann/Start-GPT-WeatherPlugin](https://github.com/ppetermann/Start-GPT-WeatherPlugin) |
| Web-Interaction | Enable Start-GPT to fully interact with websites! Allows Start-GPT to click elements, input text, and scroll | [gravelBridge/StartGPT-Web-Interaction](https://github.com/gravelBridge/StartGPT-Web-Interaction)|
| Website-Carbon-Footprint | Take advantage of the Website Carbon Footprint API with Start-GPT | [arananet/Start-GPT-Website-Carbon-Footprint](https://github.com/arananet/Start-GPT-Website-Carbon-Footprint)|
| WolframAlpha | Access to WolframAlpha to do math and get accurate information | [gravelBridge/StartGPT-WolframAlpha](https://github.com/gravelBridge/StartGPT-WolframAlpha)|
| YouTube   | Various YouTube features including downloading and understanding | [jpetzke/StartGPT-YouTube](https://github.com/jpetzke/StartGPT-YouTube) |
| Zapier webhooks | This plugin allows you to easily integrate Zapier connectivity | [AntonioCiolino/StartGPT-Zapier](https://github.com/AntonioCiolino/StartGPT-Zapier)|
| Project Management | Streamline your Project Management with ease: Jira, Trello, and Google Calendar Made Effortless| [minfenglu/StartGPT-PM-Plugin](https://github.com/minfenglu/StartGPT-PM-Plugin)|
| RabbitMQ | This plugin allows you to communicate with your Start-GPT instance via microservice.| [tomtom94/StartGPT-RabbitMQ](https://github.com/tomtom94/StartGPT-RabbitMQ)|

## Configuration

Plugins must be enabled in `plugins_config.yaml`. 

If you still have `ALLOWLISTED_PLUGINS` and `DENYLISTED_PLUGINS` in your `.env` file, Start-GPT will use them to create the `plugins_config.yaml` file the first time. 

This file contains a list of plugins to load. The format is as follows:

```yaml
plugin_a:
  config:
    api_key: my-api-key
  enabled: false
PluginB:
  config: {}
  enabled: true

```

The various sections are as follows:

- key: The name of the plugin. E.g. `plugin_a` or `PluginB`.

    This is used to load the plugin. It's format depends on whether the plugin is zipped or unzipped.
    
    **For zipped plugins**, the key must be the name of the plugin **class**. For example, the `weather` plugin in this repository would `WeatherPlugin`, and in the example above, `PluginB` is most likely a zipped plugin.

    **For unzipped plugins**, the key must be the name of the plugin **directory**. For example, in the example above, the `plugin_a` directory would be loaded as a plugin.

- config: The configuration for the plugin. 

    This is passed to the plugin when it is loaded. The format of this field depends on the plugin. This field is optional. Use `{}` if you do not need to pass any configuration to the plugin.

    Note that `plugins_config.yaml` file is only used by Start-GPT to decide whether to load a plugin. For specific plugin settings, please refer to the documentation provided for each plugin. Plugin developers may still rely on`.env` for other plugin specific settings. We encourage developers to migrate their settings to the `config` field in the new `plugins_config.yaml` file.

- enabled: Determines whether the plugin is loaded. 

## Creating a Plugin

Creating a plugin is a rewarding experience! You can choose between first-party or third-party plugins. First-party plugins are included in this repo and are installed by default along with other plugins when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for plugins you expect others to use and want, and third-party for things specific to you.

## Plugin Format

Plugins must follow a specific structure in order to be found and loaded successfully. The structure depends on whether a plugin is zipped or unzipped.

Zipped plugins must subclasses `StartGPTPluginTemplate`(https://github.com/khulnasoft/Start-GPT-Plugin-Template), and implement all the methods defined in StartGPTPluginTemplate.

Unzipped plugins can also subclass `StartGPTPluginTemplate`, but it is not required. They can implement only the methods they need. However, the name of the plugin's directory is used to load the plugin, so it must be unique within StartGPT's `plugins` directory.

### First Party Plugins How-To

1. Clone this plugins repo
1. Follow the structure of the other plugins, implementing the plugin interface as required
1. Write your tests
1. Add your name to the [codeowners](.github/CODEOWNERS) file
1. Add your plugin to the [Readme](README.md)
1. Add your plugin to the [startgpt-package](https://github.com/kurtosis-tech/startgpt-package/blob/main/plugins.star). You can copy the line of any of the standard plugins and just add another entry in the dictionary. Raise a PR & get it merged
1. Add your plugin to the [plugin installation integration test](.github/workflows/test-plugin-installation.yml)
1. Make a PR back to this repo!

### Third Party Plugins How-To

1. Clone [the third party template](https://github.com/khulnasoft/Start-GPT-Plugin-Template).
1. Follow the instructions in the [third party template readme](https://github.com/khulnasoft/Start-GPT-Plugin-Template).

### Migrating Third Party to First Party

We appreciate your contribution of a plugin to the project!

1. Clone this repository.
1. Make a folder for your plugin under `src/startgpt_plugins`. Use a simple descriptive name such as `notion`, `twitter`, or `web_ui`.
1. Add the files from your third-party plugin located at `src/start_gpt_plugin_template` into the folder you created.
1. Include your README from your third-party plugin in the folder you created.
1. Add your plugin to the root README with a description and a link to your plugin-specific README.
1. Add your plugin's Python package requirements to `requirements.txt`.
1. Add tests to get your plugin to 80% code coverage.
1. Add your name to the [codeowners](.github/CODEOWNERS) file.
1. Add your plugin to the [Readme](README.md).
1. Submit a pull request back to this repository!

## Get Help

For more information, visit the [discord](https://discord.gg/startgpt) server.
