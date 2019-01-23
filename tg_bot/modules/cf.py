import time
from typing import Optional
from datetime import datetime
from typing import Optional, List
from cffi.backend_ctypes import xrange

from telegram import Message, Update, Bot, User, replymarkup
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from tg_bot.modules.users import get_user_id
from tg_bot.modules.helper_funcs.chat_status import user_admin


def roadmap(bot, update):
    chat_id = update.effective_chat.id
    message = update.effective_message
    if chat_id == -1001396225602:
        #format
        date_format = "%m/%d/%Y"
        now = time.strftime("%m/%d/%Y")
        a = datetime.strptime(now, date_format)
        #dates
        iasupport_D = datetime.strptime('09/22/2018', date_format) - a  #date AI Support 1.0
        mobileapp1_D = datetime.strptime('09/25/2018', date_format) - a #date Beta testing Mobile app
        lkd_D = datetime.strptime('09/30/2018', date_format) - a        #date Start LKD coin
        kyc_user_D = datetime.strptime('10/01/2018', date_format) - a   #date Start KYC for all users
        autoW_D = datetime.strptime('10/10/2018', date_format) - a      #date Auto Widthdraw KYC only
        mobileapp2_D = datetime.strptime('10/25/2018', date_format) - a #date Public Mobile aoo for all users
        cleanS_D = datetime.strptime('10/30/2018', date_format) - a     #date Cleaning system
        limitU_D = datetime.strptime('11/01/2018', date_format) - a     #date Limit 1 Million User
        iasupport2_D = datetime.strptime('12/31/2018', date_format) - a #date AI Support 2.0
        moveds_D = datetime.strptime('11/01/2019', date_format) - a     #date Move to Decentralized System
        #list dates
        list_dates = [iasupport_D.days, mobileapp1_D.days, lkd_D.days,
                      kyc_user_D.days, autoW_D.days, mobileapp2_D.days,
                      cleanS_D.days, limitU_D.days, iasupport2_D.days, moveds_D.days]
        #validations
        for i in xrange(len(list_dates)):
            if list_dates[i] <= 0:
                list_dates[i] = "_Implementado._"
            else:
                list_dates[i] = "_Faltan "+str(list_dates[i])+" días._"
        #answers
        respuesta = """
        📋 *Hoja de ruta*\n➖➖➖➖➖➖➖➖➖➖➖➖
        1️⃣ *Soporte IA 1.0*
         |-- """+list_dates[0]+"""
        2️⃣ *Aplicación móvil(beta)*
         |-- """+str(list_dates[1])+"""
        3️⃣ *Lanzamiento LKD*
         |-- """+str(list_dates[2])+"""
        4️⃣ *Verificación (KYC)*
         |-- """+str(list_dates[3])+"""
        5️⃣ *Retiros automáticos(KYC)*
         |-- """+str(list_dates[4])+"""
        6️⃣ *Aplicación móvil*
         |-- """+str(list_dates[5])+"""
        7️⃣ *Limpieza del sistema*
         |-- """+str(list_dates[6])+"""
        8️⃣ *Lím. 1 millón de usuarios*
         |-- """+str(list_dates[7])+"""
        9️⃣ *Soporte IA 2.0*
         |-- """+str(list_dates[8])+"""
        🔟 *Descentralización*
         |-- """+str(list_dates[9])+"""
        """
        #answer...
        update.message.reply_text(respuesta, parse_mode='MARKDOWN',
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Hoja de ruta en línea", url="www.cryptominingfarm.io/roadmap/")]]))
    else:
        message.reply_text("Response not available for this group.")


def rvghs(bot, update, args):
    chat_id = update.effective_chat.id
    message = update.effective_message
    msg1 = "Por favor ingresar tus *vGHS* o un número entre `0` y `20000000`. ejemplo: `10000`"
    if chat_id == -1001396225602:
        if len(args) >= 1:
            try:
                val = int(args[0])
                if int(val) <= 20000000 and int(val) >= 0:
                    vghs_day = (val/1000)*0.184
                    vghs_month = ((val/1000)*0.184)*30
                    vghs_year = ((val/1000)*0.184)*365
                    answer = "_Cálculo realizado con el stacking rate full(15%)._ \n" \
                                "📌 *DIARIO*\n" \
                                "*   >>* `"+str(val)+"` / 1000 x 0.184 = `"+str(round(vghs_day, 2))+"` USD \n" \
                                "📌 *MENSUAL*\n" \
                                "*   >>* `"+str(val)+"` / 1000 x 0.184 x 30 = `"+str(round(vghs_month, 2))+"` USD \n" \
                                "📌 *ANUAL*\n" \
                                "*   >>* `"+str(val)+"` / 1000 x 0.184 x 365 = `"+str(round(vghs_year, 2))+"` USD \n"
                    message.reply_text(answer,  parse_mode='MARKDOWN')
                else:
                    message.reply_text(msg1, parse_mode='MARKDOWN')
            except:
                message.reply_text("ERROR", parse_mode='MARKDOWN')
        else:
            message.reply_text(msg1, parse_mode='MARKDOWN')
    else:
        message.reply_text("Response not available for this group.")


__help__ = """
 - /roadmap: Show roadmap of CFPAY.
 - /rvgghs: Calculate power performance vghs.
"""
__mod_name__ = "CF"

ROADMAP_HANDLER = DisableAbleCommandHandler("roadmap", roadmap)
RVGHS_HANDLER =  DisableAbleCommandHandler("rvghs", rvghs, pass_args=True)

dispatcher.add_handler(ROADMAP_HANDLER)
dispatcher.add_handler(RVGHS_HANDLER)
