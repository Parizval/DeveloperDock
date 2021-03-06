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

def Project(ProjectName,LineCode,Language,Cloud,Function,result,email):
    l1 = { "Id": str(uuid.uuid4()),"Email":email,"Type":"Kube",
        "ProjectName": ProjectName, "LineCode": LineCode, "Language": Language,
        "Cloud":Cloud,"Function":Function, "Result": result    }

    ProjectCollection.insert_one(l1)

def NormalProject(ProjectName,LineCode,Language,Function,result,email):

    l1 = { "Id": str(uuid.uuid4()),"Email":email,"Type":"Normal",
        "ProjectName": ProjectName, "LineCode": LineCode, "Language": Language,
        "Function":Function, "Result": result    }
    
    ProjectCollection.insert_one(l1)

def ProjectStats(email):
    l1 = {"Email": email}
  
    NormalResult = {"Network":"Network Load Balancer (v2)" , "Serverless":"AWS Lambda",
    "Application":"Application Load Balancer (v2)","Sticky":"Session Based Load Balancer"}

    NormalFunction = {"Simple":"Simple Web Application/LMS/","Payment":"Payment GateWay or Session",
    "High":"High Performance/High Usage Application"
    }

    KubeHeading = {"Kubeless":" Kubeless Functions" , 
    "Round Robin":"Round Robin Load Balancer (v2)","Ring Hash":"Ring Hash Load Balancing Algorithm"}

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

        TableData[counter] = {"Project":i['ProjectName'],'Language':i['Language']}

        Lang.append(i['Language'])
        if i['Type'] == "Normal":
            StatData['Public'] += 1  
            TableData[counter]['Cloud'] = "Public"
            TableData[counter]["Result"] = NormalResult[i['Result']]
            TableData[counter]['Function'] = NormalFunction[i['Function']]
        else:
            if  i['Cloud'] == 'Public': 
                StatData['Public'] += 1  
            else: 
                StatData['Private'] += 1  
            TableData[counter]['Cloud'] = i['Cloud']
            TableData[counter]["Result"] = KubeHeading[i['Result']]
            TableData[counter]['Function'] = NormalFunction[i['Function']]
        counter += 1 
    StatData['Language'] = len(set(Lang))
    return StatData,TableData