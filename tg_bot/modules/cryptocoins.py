import requests, json
from telegram import Message, Chat, Update, Bot, ParseMode
from telegram.ext import CommandHandler, run_async
from tg_bot import dispatcher
#from tg_bot.__main__ import DATA_IMPORT
#from telegram.error import BadRequest
#from io import BytesIO
#from typing import Optional
#from tg_bot.modules.helper_funcs.chat_status import user_admin


@run_async
#@user_admin
def price(bot: Bot, update: Update):
    msg = update.effective_message
    chat = update.effective_chat 
    #if __name__ == "__crypto__":
    if chat.type != chat.PRIVATE:
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            bpi = data['bpi']
            #for key, value in bpi.items():
            coin = round(bpi['USD']['rate_float'], 2)#, bpi[key]['rate']
            msg.reply_text("📉 *BTC price:*\n💲`"+str(coin)+" USD`\n _By coindesk._", parse_mode='MARKDOWN')
        else:
            msg.reply_text("*El API no esta operativa*", parse_mode='MARKDOWN')

__mod_name__ = "Cryptocoins"

__help__ = """
*Admin only:*
 - /p: Price Bitcoin.
"""
PRICE_HANDLER = CommandHandler("p", price)

dispatcher.add_handler(PRICE_HANDLER)
