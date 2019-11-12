import logging,os,datetime,random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler,Filters, ConversationHandler

import actions


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN=os.environ.get("ERPPABOTACCESS", None)
    updater = Updater(TOKEN, use_context=True)
    disp=updater.dispatcher
    jobs=updater.job_queue

    disp.add_handler(CommandHandler('start', actions.start)) #for start command
    disp.add_handler(MessageHandler(Filters.command,actions.start)) #any command
    disp.add_handler(CallbackQueryHandler(actions.main_menu,pattern="back")) #main

    #general fkts:
    disp.add_handler(CallbackQueryHandler(actions.weather,pattern="wether"))
    disp.add_handler(CallbackQueryHandler(actions.por,pattern="por"))
    disp.add_handler(CallbackQueryHandler(actions.vpor,pattern="vpor"))
    disp.add_handler(CallbackQueryHandler(actions.bus,pattern="hsl"))
    disp.add_handler(CallbackQueryHandler(actions.bike,pattern="bike"))
    disp.add_handler(CallbackQueryHandler(actions.light,pattern="lights"))
    disp.add_handler(CallbackQueryHandler(actions.on,pattern="on"))
    disp.add_handler(CallbackQueryHandler(actions.off,pattern="off"))
    disp.add_handler(CallbackQueryHandler(actions.status,pattern="status"))

    #cloud:
    disp.add_handler(CallbackQueryHandler(actions.cloud,pattern="^cloud"))
    disp.add_handler(CallbackQueryHandler(actions.cloud_del_file,pattern="^removefile"))
    disp.add_handler(CallbackQueryHandler(actions.cloud_del_dir,pattern="^removedir"))

    #conversations:
    conv_dir=ConversationHandler(conversation_timeout=60,
        entry_points=[CallbackQueryHandler(actions.add_dir,pattern="^adddir")],

        states={
            actions.CREATE_DIR: [MessageHandler(Filters.text,actions.new_dir)],
        },
        fallbacks=[CommandHandler('cancel',actions.out)]
    )

    conv_file=ConversationHandler(conversation_timeout=60,
        entry_points=[CallbackQueryHandler(actions.add_file,pattern="^addfil")],

        states={
            actions.CREATE_FILE: [MessageHandler(Filters.document,actions.doc)],
        },
        fallbacks=[MessageHandler(Filters.text,actions.out)]
    )
    
    disp.add_handler(conv_dir)
    disp.add_handler(conv_file)

    t7=datetime.time(hour=7)
    jobs.run_daily(actions.send_daily,time=t7)#daily

    d=actions.jee.new_time()
    print(d+datetime.datetime.now(),type(d),d)
    jobs.run_repeating(actions.jees,d)#random

    disp.add_handler(MessageHandler(Filters.text,actions.out)) #print txt
    
    disp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
