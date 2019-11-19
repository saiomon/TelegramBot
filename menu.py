from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import cloud

def menu_keyboard_def(erno=False):
    keyboard=[]
    keyboard=[[InlineKeyboardButton('🚌', callback_data='hsl'),
             InlineKeyboardButton('🚴‍♂', callback_data='bike'),
             InlineKeyboardButton('🌦', callback_data='wether')],
             [InlineKeyboardButton('💡', callback_data='lights'),
             InlineKeyboardButton('🍔', callback_data='por'),
             InlineKeyboardButton('🍣', callback_data='vpor')]]
    if erno:
        keyboard.append([InlineKeyboardButton('cloud', callback_data='cloud/')])
        keyboard.append([InlineKeyboardButton('🔁', callback_data='rfrsh')])
    return InlineKeyboardMarkup(keyboard)

def menu_keyboard():
    keyboard=[[InlineKeyboardButton('🚌', callback_data='hsl'),
             InlineKeyboardButton('🚴‍♂', callback_data='bike'),
             InlineKeyboardButton('🌦', callback_data='wether')],
             [InlineKeyboardButton('💡', callback_data='lights'),
             InlineKeyboardButton('🍔', callback_data='por'),
             InlineKeyboardButton('🍣', callback_data='vpor')],
             [InlineKeyboardButton('🧨', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)

def food_menu(dates):
    keyboard=[]
    for d in dates:
        keyboard.append(InlineKeyboardButton(d+'.', callback_data='por'+':'+d))
    keyboard=[keyboard,[InlineKeyboardButton('🚌', callback_data='hsl'),
             InlineKeyboardButton('🚴‍♂', callback_data='bike'),
             InlineKeyboardButton('🌦', callback_data='wether')],
             [InlineKeyboardButton('💡', callback_data='lights'),
             InlineKeyboardButton('🍔', callback_data='por'),
             InlineKeyboardButton('🍣', callback_data='vpor')],
             [InlineKeyboardButton('🧨', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)

def food_menu_v(dates):
    keyboard=[]
    for d in dates:
        keyboard.append(InlineKeyboardButton(d+'.', callback_data='vpor'+':'+d))
    keyboard=[keyboard,[InlineKeyboardButton('🚌', callback_data='hsl'),
             InlineKeyboardButton('🚴‍♂', callback_data='bike'),
             InlineKeyboardButton('🌦', callback_data='wether')],
             [InlineKeyboardButton('💡', callback_data='lights'),
             InlineKeyboardButton('🍔', callback_data='por'),
             InlineKeyboardButton('🍣', callback_data='vpor')],
             [InlineKeyboardButton('🧨', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)



def menu_keyboard_light():
    keyboard=[[InlineKeyboardButton('🔦', callback_data='on'),
             InlineKeyboardButton('🔌', callback_data='off'),
             InlineKeyboardButton('🧞‍♂', callback_data='status')],
             [InlineKeyboardButton('⏪', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)

def menu_keyboard_files(node):
    keyboard=[]
    lastline=[]
    d,f=cloud.get_dir(node)
    print(d,f)
    for ds in d:
        keyboard.append([InlineKeyboardButton("📁 "+ds,callback_data=node+ds+"/"),InlineKeyboardButton("❌",callback_data="removedir:"+node+ds+'/')])
    for fs in f:
        keyboard.append([InlineKeyboardButton("📄 "+fs,callback_data=node+fs),InlineKeyboardButton("❌",callback_data="removefile:"+node+fs)])
    lastline.append(InlineKeyboardButton('➕📁', callback_data="adddir:"+node))
    lastline.append(InlineKeyboardButton('➕📄', callback_data="addfil:"+node))
    if not(node=="cloud/"):
        prev=cloud.strip_last(node)
        print("{},prev:{}".format(node,prev))
        lastline.append(InlineKeyboardButton('⏪', callback_data=prev))
    lastline.append(InlineKeyboardButton('🧨', callback_data='back'))
    keyboard.append(lastline)
    return InlineKeyboardMarkup(keyboard)
