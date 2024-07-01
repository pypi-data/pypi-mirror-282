Introduction
============

We’ve built the bot framework you’ve been waiting for!
======================================================

Unlock seamless Telegram bot development with our intuitive, powerful framework. Tap into our thriving community for support and inspiration

Installing
==========

You can install or upgrade ``ptb-easy-bot`` via

.. code:: shell

    $ pip install ptb-easy-bot --upgrade

To install a pre-release, use the ``--pre`` `flag <https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-pre>`_ in addition.


Quick Start
===========

::

    from Easy_Bot import _powerup_bot_ , commnders 
    from telegram import Bot
    import asyncio

    TOKEN = ""
    WEBHOOK_URL = ""
    PORT = int(os.environ.get('PORT', '8443'))

    async def main(WEBHOOK_URL,TOKEN):
        if WEBHOOK_URL:
            bot = Bot(TOKEN)
            await bot.set_webhook(WEBHOOK_URL + "/" + TOKEN)
        start_check_updates()
        
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello..")

    Handlers = {
        commnders :  {
            'start' : start_command,
        },
        
    }
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(WEBHOOK_URL,TOKEN))
        _powerup_bot_(
            TOKEN=TOKEN, 
            Handlers=Handlers,
            Webhook_url=WEBHOOK_URL,
            PORT=PORT
        )
    
