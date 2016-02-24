[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikConsolePanelStartup
A Sublime Text plugin to always show console panel at startup.

Tested working with:
- Sublime Text 2
- Sublime Text 3

![Image](/screencast.gif)

## Table of Contents
[:toc(beg='next', indent=-1)]

## Setup

### Setup via git
Clone this repository to Sublime Text's **Packages** directory (Preferences - Browse Packages...):
```
git clone https://github.com/AoiKuiyuyou/AoikConsolePanelStartup-SublimeText AoikConsolePanelStartup
```

Make sure the repository directory is renamed to **AoikConsolePanelStartup**
(without the "-SublimeText" postfix), otherwise it may not work well.

## Usage
Restart Sublime Text to see if it works.

Settings can be adjusted at
"Preferences - Package Settings - AoikConsolePanelStartup".
