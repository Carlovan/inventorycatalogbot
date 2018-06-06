Second version of the [@InventoryCatalogBot](t.me/inventorycatalogbot) Telegram bot, completely rewritten from scratch.

# Installation

## Dependencies
To install you need
* Python >= 3.5
* PostgreSQL >= 9.4

Then run
```$ pip install -r requirements.txt```
to install all the python dependencies.

## Database
Create a new database inside you PostgreSQL server and leave it empty.  
Then edit `settings.json` to set the data to access your own database.

## Settings
You can edit the settings inside the `settings.json` file.
* `token`: _Required._ This is your bot token, you can get one from [@BotFather](t.me/botfather)
* `database_url`: _Required._ This is the [connection URI](https://www.postgresql.org/docs/9.4/static/libpq-connect.html#AEN41613) to your database
* `webhook`: _Optional._ This is the URL to set the webhook to; if not set it will use the polling method
* `admin`: _Required._ This is the chat_id of the first admin; this user wil be automatically added as admin by the `/adinit/` command.

You can also set a changelog editing the `changelog.txt` file.

## Running
Make sure your settings are right and the database is running, then just run
```$ python main.py```

Send the command `/adinit` with the admin user set in `settings.json` to initialize the database.

To stop the bot send a SIGINT pressing `Crtl-C`
