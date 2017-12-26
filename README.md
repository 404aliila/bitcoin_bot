# Bitcoin bot
Bitcoin bot is a telegram bot that sends you bitcoin price every 15 minutes.

### How to use :
First thing first, you need to install some python modules in order to have the bot working.
required modules :
	+ telepot
	+ sqlite3
you can use 'pip' to install the mentioned modules.

next you need to create a file called 'bot_token.py' and this is where youre bot's token is.
the content of file sould look like this:

token = '123456789:ABCDEFGH1234567890ABCDEFGH123456789'

so now you need to setup the bot's database, where the bot user's chat ids are stored.
simply run :

$ python create_database.py

and thats it! you're good to go now, just run

$ nohup python bit.py &

and youre bot is online.
