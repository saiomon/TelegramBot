import menu,db,food,forecast,jee,hsl,db
import cloud as cdb
import lights as hue
import datetime, subprocess
from logprint import printer

import os
from telegram.ext import ConversationHandler
from telegram.ext.dispatcher import run_async

CREATE_DIR=0
CREATE_FILE=1

@run_async
def out(update, context):
    print(update.message.text)

def rfrsh(update,context):
    q = update.callback_query
    context.bot.answerCallbackQuery(callback_query_id=q.id,text="Restarting")
    subprocess.call(['./refresh.sh'])

def start(update, context):
    db.handle_db(update)
    admin=os.environ.get("ERNO","")
    b=update.message.chat.id==int(admin)#101714155
    update.message.reply_text(text='MOICCULI{}! Mie oon Erppa.'.format(db.get_name(update)), reply_markup=menu.menu_keyboard_def(erno=b))

@run_async
def main_menu(update,context):
    q = update.callback_query
    db.handle_db(q)
    admin=os.environ.get("ERNO","")
    b=q.message.chat.id==int(admin)#101714155
    q.edit_message_text(text='MOICCU{}! Mie oon Erppa.'.format(db.get_name(q)), reply_markup=menu.menu_keyboard_def(erno=b))

@run_async
def send_daily(context):
    ids=db.get_daylies()
    for id in ids:
        context.bot.send_message(chat_id=id,text="PIRTEAÄÄ HUOMENTA!")

@run_async
def jees(context):
    if 9<= datetime.datetime.now().hour <=23:
        ids=db.get_jees()
        for id in ids:
            context.bot.send_message(chat_id=id,text=jee.get_jee())
    t=jee.new_time()
    print(context.job.interval)
    print(t+datetime.datetime.now(),type(t),t)
    context.job.interval=t
    print(context.job.interval)

def cloud(update,context):
    q = update.callback_query
    path=q.data
    print("path: ",path)
    #print(context.user_data.get('dir_path',"None"),"----------")
    if cdb.is_file(path):
        print("file: ",cdb.get_fn(path))
        #print("Prev: ",cdb.strip_file(path))
        #print("pretty: ",cdb.pretty_dir(path))
        q.edit_message_text(text="Downloading:\n{} from {}".format(cdb.get_fn(path),cdb.strip_file(cdb.pretty_dir(path)[1:])),reply_markup=menu.menu_keyboard_files(cdb.strip_file(path)))
        context.bot.send_document(chat_id=q.message.chat.id,document=open(path,'rb'))
    else:
        if cdb.is_dir(path):
            dire="Erppa cloud:\n{}".format(cdb.pretty_dir(path))
        q.edit_message_text(text=dire,reply_markup=menu.menu_keyboard_files(path))

def cloud_del_file(update,context):
    q = update.callback_query
    path=q.data.split(":")[1]
    print("Removed file path: ",path)
    new_path=cdb.strip_file(path)
    txt=cdb.del_file(path)
    #print("new path: ",new_path)
    #print("res: ",txt)
    context.bot.answerCallbackQuery(callback_query_id=q.id,text=txt)
    q.edit_message_text(text=new_path,reply_markup=menu.menu_keyboard_files(new_path))

def cloud_del_dir(update,context):
    q = update.callback_query
    path=q.data.split(":")[1]
    print("Removed dir path: ",path)
    new_path=cdb.strip_last(path)
    #print("New path: ",new_path)
    txt=cdb.del_dir(path)
    #print("res: ",txt)
    context.bot.answerCallbackQuery(callback_query_id=q.id,text=txt)
    q.edit_message_text(text=new_path,reply_markup=menu.menu_keyboard_files(new_path))

def add_dir(update,context):
    print(context.user_data)
    q = update.callback_query
    path=q.data.split(":")[1]
    context.bot.answerCallbackQuery(callback_query_id=q.id,text="Type & send new folder name")
    print("Dir path to be added: ",path)
    context.user_data['dir_path']=path
    return CREATE_DIR

def new_dir(update,context):
    path=context.user_data.get('dir_path',None)
    if path:
        new_path=path+update.message.text[:127]
        txt=cdb.add_dir(new_path) #char limit from stetson
    context.bot.send_message(chat_id=update.message.chat.id,text=txt,reply_markup=menu.menu_keyboard_files(path))
    return ConversationHandler.END

def add_file(update, context):
    q = update.callback_query
    path=q.data.split(":")[1]
    context.bot.answerCallbackQuery(callback_query_id=q.id,text="Send the file")
    print("Dir path for file to be added: ",path)
    context.user_data['file_path']=path
    return CREATE_FILE

def doc(update,context):
    print("FIlu: ",update.message.document)
    doc=update.message.document
    file_id=doc.file_id
    file=context.bot.get_file(file_id)
    path=context.user_data.get('file_path',None)
    if path:
        file.download(custom_path='{}{}'.format(path,doc.file_name))
    context.bot.send_message(chat_id=update.message.chat.id,text="Added {}".format(doc.file_name),reply_markup=menu.menu_keyboard_files(path))
    return ConversationHandler.END

@run_async
def bus(update,context):
    q = update.callback_query
    printer(q)
    q.edit_message_text(text=hsl.get_dös(), reply_markup=menu.menu_keyboard())

@run_async
def bike(update,context):
    q = update.callback_query
    printer(q)
    q.edit_message_text(text=hsl.get_zyk(), reply_markup=menu.menu_keyboard())

@run_async
def weather(update,context):
    q = update.callback_query
    printer(q)
    q.edit_message_text(text=forecast.forecast(), reply_markup=menu.menu_keyboard())

@run_async
def por(update,context):
    q = update.callback_query
    printer(q)
    try:
        d=q.data.split(':')[1].split('.')
    except:
        resp=food.por()
    else:
        resp=food.por(datetime.date.today().replace(month=int(d[1]),day=int(d[0])))
    dates=food.get_dates()
    q.edit_message_text(text=resp, reply_markup=menu.food_menu(dates))

@run_async
def vpor(update,context):
    q = update.callback_query
    printer(q)
    try:
        d=q.data.split(':')[1].split('.')
    except:
        resp=food.por_v()
    else:
        resp=food.por_v(datetime.date.today().replace(month=int(d[1]),day=int(d[0])))
    dates=food.get_dates()
    q.edit_message_text(text=resp, reply_markup=menu.food_menu_v(dates))

@run_async
def light(update,context):
    q = update.callback_query
    printer(q)
    q.edit_message_text(text="Light setup", reply_markup=menu.menu_keyboard_light())

@run_async
def on(update,context):
    q = update.callback_query
    printer(q)
    if db.is_wl(q.message.chat.id):
        txt=hue.lightsON()
    else:
        txt="Not allowed."
    q.edit_message_text(text=txt, reply_markup=menu.menu_keyboard_light())

@run_async
def off(update,context):
    q = update.callback_query
    printer(q)
    if db.is_wl(q.message.chat.id):
        txt=hue.lightsOFF()
    else:
        txt="Not allowed."
    q.edit_message_text(text=txt, reply_markup=menu.menu_keyboard_light())

@run_async
def status(update,context):
    q = update.callback_query
    printer(q)
    if db.is_wl(q.message.chat.id):
        txt=hue.lightStatus()
    else:
        txt="Not allowed."
    q.edit_message_text(text=txt, reply_markup=menu.menu_keyboard_light())