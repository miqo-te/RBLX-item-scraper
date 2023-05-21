
# RBLX-item-scraper

This was designed to check the price of a roblox **limited** item every few minutes with a custom delay option available. It will notify you by sending a message to your discord server using a webhook.



## Author

- [@silentswrd](https://github.com/silentswrd)


## Python3 & Chrome required

[Python3](https://www.python.org/downloads/) is required to run. If you use Python2 or don't have Python installed please upgrade to avoid conflict. The code utilises [Chrome](https://www.google.com/chrome/) to scrape information correctly, make sure it is installed to the default path.
    
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
## Contributing

Contributions are always welcome!

Visit [@silentswrd on Ko-fi](https://ko-fi.com/silentswrd)

Tips make it easier for me to work on current and upcoming projects and help me with the cost to maintain them.
## License

Attribution-NonCommercial 2023 silencedswrd

This work is licensed under the Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/3.0/.

You are free to:

- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material.

Under the following terms:

- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- NonCommercial: You may not use the material for commercial purposes.