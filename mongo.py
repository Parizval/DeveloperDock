from passlib.hash import pbkdf2_sha256
import pymongo
import uuid

# Establishing the connection
username = "DevDock"
password = "afKNiamzY7us3Il7"

srv = "mongodb+srv://{}:{}@supplychain-u6nhl.mongodb.net/test?retryWrites=true&w=majority".format(
    username, password)
client = pymongo.MongoClient(srv)

print("MongoDB Connected")

db = client['DeveloperDock']

LoginCollection = db['Auth']
ProjectCollection = db['Project']

def Register(email,name,password):
    q1 = {"email":email}

    result1 = LoginCollection.find(q1)
    check = False

    for  i in  result1:
        if  email == i['email']:
            check = True
            break
    
    if check:
        print("Email Address already exist in database.")
        return False
    else:
        password = pbkdf2_sha256.hash(password)
        q2 = {"name": name, "email": email,
              "password": password,"Id":str(uuid.uuid4())}
        
        LoginCollection.insert_one(q2)
        return True

def Login(email,password):
    l1 = {"email": email}
    res = LoginCollection.find(l1)

    data = {}
    data['check'] = False
    for i in res:
        if pbkdf2_sha256.verify(password, i['password']):
            data['name'] = i['name']
            data['check'] = True
    print(data)
    return data

def Project(ProjectName,LineCode,Language,Cloud,Check,Function,Config,email):
    l1 = { "Id": str(uuid.uuid4()),"Email":email,
        "ProjectName": ProjectName, "LineCode": LineCode, "Language": Language,
        "Cloud":Cloud,"Check":Check,"Function":Function, "Config": Config    }

    ProjectCollection.insert_one(l1)

def NormalProject(ProjectName,LineCode,Language,Function,result,email):

    l1 = { "Id": str(uuid.uuid4()),"Email":email,"Type":"Normal",
        "ProjectName": ProjectName, "LineCode": LineCode, "Language": Language,
        "Function":Function, "Result": result    }
    
    ProjectCollection.insert_one(l1)

def ProjectStats(email):
    l1 = {"Email": email}
  
    
    StatData = {}
    TableData = {}
    counter = 1
    Lang = []

    StatData['Project'] = 0 
    StatData['Public'] = 0 
    StatData['Private'] = 0 


    res = ProjectCollection.find(l1)
    for  i in  res:
        StatData['Project'] += 1 

        TableData[counter] = {"Project":i['ProjectName'],'Language':i['Language'],"Function":i['Function'],"Result":i['Result']}

        Lang.append(i['Language'])
        if i['Type'] == "Normal":
            StatData['Public'] += 1  
            TableData[counter]['Cloud'] = "Public"
        else: 
            pass
        counter += 1 
    StatData['Language'] = len(set(Lang))
    return StatData,TableData