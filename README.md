# Stody Bot
 ## **a *'nerdy'* discord bot me and [funky](https://github.com/FunkySplash48) made**

# "Abilities"
Spits out random useless facts randomly  
Can solve basic maths sums  
Gives information about elements based on atomic number, mass, name
# Installation and Setup
## Setup a new discord application
Go to the discord developer portal and make a new application.  
Make a bot for the application  
## Installing
Clone the repo, make a virtual env(optional)  
Install the packages  
```pip install -r requirements.txt```
## Bot token
Replace ```client.run('TOKEN')``` on line 127 with your discord application token

# Usage
the fun part(no this bot sucks)

## Commands
```
nerd evaluate [Sum]
> nerd eval 2^2+4/9

nerd info [Element]
> nerd info Na
> nerd info sodium
> nerd info 11

nerd fact [Optional fact index]
> nerd fact 23
```

## Note
you can change the bot prefix in ```client = commands.Bot(command_prefix='nerd ')``` line 8  
and also change element and fact datasheets
