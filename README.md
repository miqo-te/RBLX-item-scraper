
# RBLX-item-scraper
### ⚠️ Repo is archived & probably doesn't work anymore. Even if it worked, I don't suggest using it as the method used to scrape info is very unpractical.

This was designed to check the price of a roblox **limited** item every few minutes with a custom delay option available. It will notify you by sending a message to your discord server using a webhook.

## Python & Chrome required

[Python3](https://www.python.org/downloads/) is required to run. Make sure you use the correct python version. e.g. if you install the requirements.txt for `Python 3.11`, you should use the same version to run the `core.py`. The code utilises [Chrome](https://www.google.com/chrome/) to scrape information correctly, make sure it is installed to the default path.
    
## Usage / Instructions

#### IMPORTANT: Before you start

Note that you should change the settings to be towards your liking in `settings.json` and to change `webhook_url` in `settings.json` to the webhook url from your Discord server's webhook. Find out [how to set up a webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). In this file you can also change the URL to the item you wish to price scrape. Do not change any files other than `settings.json`

#### MacOS / Linux:
1. Open `terminal` by searching for it or opening it via <kbd>⌘</kbd> + <kbd>SPACE</kbd> and typing `terminal`
2. Run `cd [PATH TO THE FOLDER]`
* Choose View > Show Path Bar, or press the <kbd>⌃</kbd> key to show the path bar momentarily.
3. Run `pip3 install -r requirements.txt`
4. Run `python3 core.py`

#### Windows:
1. Open `cmd` by searching for it or opening it via <kbd>WIN</kbd> + <kbd>R</kbd> and typing `cmd`
2. Run `cd [PATH TO THE FOLDER]`
3. Run `pip3 install -r requirements.txt`
4. Run `python3 core.py`
