# Setting up the simplest Discord AI bot using pygpt4all

On Ubuntu 22.04 with 14gb ram, 4 procs, and the ich9 chipset in Virtualbox to run the 13b model

TIP: If you have vagrant, you can simply run "vagrant up", then "vagrant ssh", then "sudo su - dbots" update the value in .env file.

```
apt-get update
apt-get -y install python3.10-venv python3-pip
useradd -m -s /bin/bash dbots

passwd dbots
su - dbots
```

Edit a file called ".env" and add this line:
`export DISCORD_TOKEN='xxx'`

Edit .bashrc and add this line to the bottom:
`source ./.env`

```
git clone https://github.com/mkinney/discord_aibot.git
cd discord_aibot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Go to https://discord.com/developers/applications and create a "New Application"
Go into Oauth2 and copy the Client ID
Go to https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot
but replace the X's with the client id

Go into Bot, View Token (or reset)
Copy the token value into the .env file
Note: Any changes to the .env file will need to be reloaded. Simplest way is to exit from the dbot user, then re-su again.

Ensure the Bot has "Presence intent", "Server members intent", and "Message Content Intent" enabled.
Note: You probably do not want a public bot.

Run "python reply.py"

You should see something like this:

```
$ python reply.py
2023-04-29 05:44:50 INFO     discord.client logging in using static token
2023-04-29 05:44:51 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: xxx).
Logged in as daibot#xxx (ID: xxx)
```

From discord you should see "XXX is here" in the channel.
It should respond to you when you type in "!hello".

If so, then kill the reply.py program.

```
wget http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin
```

Run "python example.py"
Make sure it works.
You'll get a sense of how long responses may take.

Run "python bot.py"
Again, the output should show it logged in ok.
From discord run "?ai Some question"

Note: If you run "python bot.py" and you get "Aborted (core dumped)", then you probably ran out of memory. (I got this when I used a 4gb ram instance.)
Either add more memory or add some swap.

Here's what it looks like in testing:

<img width="283" alt="Screen Shot 2023-04-28 at 8 43 09 PM" src="https://user-images.githubusercontent.com/2219838/235283566-1ff8b63a-5a7d-4d6c-a197-271f997d5622.png">

