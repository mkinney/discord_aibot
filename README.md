# Setting up the simplest Discord AI bot using pygpt4all

## Set up bot in discord

- Go to https://discord.com/developers/applications and create a "New Application"
- Go into Oauth2 and copy the Client ID
- Go to https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot but replace the X's with the client id
- Go into Bot, View Token (or reset). Copy that token value. It will be used later.
- Ensure the Bot has "Presence intent", "Server members intent", and "Message Content Intent" enabled. (You probably do not want a public bot.)

## Dealing with the token
- Copy the .env_example file to .env
- Edit the .env file and change the xxx value for the token created in the Discord bot setup step above

## Where do you want to run the bot?

You have a few options:
1) Use a windows or mac computer that has sufficient cpu/memory to run the bot in the background, or
2) Use a linux virtual machine to run in the background.

## Windows based bot

- Clone this repository
- With a "Command prompt" in that cloned repository directory run the following:

```
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

## Linux based bot

On Ubuntu 22.04 with 14gb ram, 4 procs, and the ich9 chipset in Virtualbox to run the 13b model

TIP: If you have vagrant, you can simply run "vagrant up", then "vagrant ssh", then "sudo su - dbots", "cd discord_aibot", run the alias "act" to activate the python virtual environemnt.

```
apt-get update
apt-get -y install python3.10-venv python3-pip
useradd -m -s /bin/bash dbots
su - dbots
```

```
git clone https://github.com/mkinney/discord_aibot.git
cd discord_aibot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Test that the bot is setup ok in Discord by temporarily running a simple reply bot.

Run "python reply.py"

You should see something like this from the bot side:

```
$ python reply.py
2023-04-29 05:44:50 INFO     discord.client logging in using static token
2023-04-29 05:44:51 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: xxx).
Logged in as daibot#xxx (ID: xxx)
```

From discord you should see "XXX is here" in the channel.

<img width="333" alt="Screen Shot 2023-04-30 at 6 50 57 PM" src="https://user-images.githubusercontent.com/2219838/235389581-c8d54811-1a10-4761-84f3-6a8c7e0b92c8.png">


The reply bot should respond to you when you type in "!hello".

<img width="300" alt="Screen Shot 2023-04-28 at 10 46 19 PM" src="https://user-images.githubusercontent.com/2219838/235289717-383ccf45-ac8b-4179-a786-cd980e33076f.png">


Make sure you get that to work before continuing.

If successful, then kill the reply.py program. (control-c)

## Download the model and test that pygpt4all works as expected

Download the model:

```
wget http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin
```

Run "python example.py"

Make sure you get that to work before continuing.

You'll get a sense of how long responses may take.

## Test out the bot

- Run "python bot.py". Again, the output should show it logged in ok.
- From discord run "?ai Some question"

Note: If you run "python bot.py" and you get "Aborted (core dumped)", then you probably ran out of memory.

Here's one example in use:
<img width="874" alt="Screen Shot 2023-04-29 at 6 53 23 PM" src="https://user-images.githubusercontent.com/2219838/235331802-8115057c-a237-4b9d-a07d-c77637f2d209.png">


## Create a linux service (optional)
For Linux users: to set up the bot as a service to auto start upon a reboot, as root run:

```
cp aibot.service /etc/systemd/system/aibot.service
systemctl daemon-reload
systemctl start aibot
systemctl status aibot
tail -n 20 /var/log/syslog
systemctl enable aibot
```

## Limitations
- Since pygpt4all is CPU only, it may be slow. The python library to interact with discord is called discord.py. discord.py has a limitation where it will log every 10 seconds a bot is running.
- You may want to change the number of cores that it runs on to improve the speed. If so, add this parameter `n_threads=4` to the `generate` arguments, where 4 can be changed to what you want.
- If not running as a linux service, then if the bot program dies or needs to be re-started, change to the directory, run the activate script, then run "python bot.py" again.
- If you want to change the model, you'll have to change the code. (which should be fairly straighforward)
- If you don't like "?ai" you can change those in code.
- Only one ai request is handled at a time. On a small discord server with a couple of users, this would be totally fine. On a busier server, it would probably not be fine.
