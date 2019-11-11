import datetime ,json

def handle_db(q):
    id=q.message.chat.id
    q.message.chat.username
    chat_type=q.message.chat.type
    if (chat_type=='private'):
        user=q.message.chat.username
    if (chat_type=='group' or chat_type=='super'):
        user=q.message.chat.title
    if not is_in_db(id):
        add_user(id,user)
        print(user, "User added")
        return None

def get_name(q):
    if (q.message.chat.type=='private'):
        return " " + q.message.chat.first_name
    else:
        return ""

def is_in_db(chat_id):
    data=loadData()
    return str(chat_id) in data

def add_user(chat_id,user):
    data=loadData()
    chat_id=str(chat_id)
    if chat_id not in data:
        data[chat_id] = {"morning":False,"name":user}
    saveData(data)

def get_daylies():
    data=loadData()
    ret=[]
    for id,k in data.items():
            if isinstance(k,dict) and k.get("morning",False):
                ret.append(id)
    return ret

def get_jees():
    data=loadData()
    ret=[]
    for id,k in data.items():
        if isinstance(k,dict) and k.get("jee",False):
            ret.append(id)
    return ret

def is_wl(chat_id):
    data=loadData()
    return data[str(chat_id)].get("wl",False)



def saveData(data):
        try:
            data['timestamp'] = str(datetime.datetime.now())
            with open('botdata.json', 'w') as outfile:
                outfile.write(json.dumps(
                                    data,
                                    indent=4,
                                    sort_keys=True))
        except (IOError, TypeError) as e:
            print(data)
            print('Saving the data failed!!')
            print(e)

def loadData():
        try:
            with open('botdata.json', 'r') as infile:
                data = json.load(infile)
            return data
        except IOError:
            print('No botdata.json file found!')
        except json.decoder.JSONDecodeError:
            print('Could not parse file!')
            data['timestamp'] = str(datetime.datetime.now())