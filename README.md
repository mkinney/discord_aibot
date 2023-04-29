# Setting up the simplest Discord AI bot using pygpt4all

I'm using an Ubuntu Digital Ocean instance with 8gb of ram. Might need a bigger instance.

```
apt-get update
apt-get -y upgrade
```

probably want to reboot at this point

```
reboot

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
git clone <thisrepo>
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
2023-04-29 02:49:21 INFO     discord.client logging in using static token
2023-04-29 02:49:22 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: xxx).
Logged in as xxx#8784 (ID: xxx)
```

From discord you should see "XXX is here" in the channel.
It should respond to you when you type in "!hello".

If so, then kill the reply.py program.

```
wget https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin
```

Run "python example.py"
Make sure it works.
You'll get a sense of how long responses may take.

Run "python bot.py"
Again, the loggint should show it logged in ok.
From discord run "?ai Some question"

Note: If you run "python bot.py" and you get "Aborted (core dumped)", then you probably ran out of memory.
Either add more memory or add some swap. (note: this will make the bot respond slowly)
```
	free -h
	fallocate -l 8G /swapfile
	chmod 600 /swapfile
	mkswap /swapfile
	swapon /swapfile
	free -h
```
