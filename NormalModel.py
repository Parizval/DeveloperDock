import pickle 

language = {"Python":4,"NodeJs":2,"Java":1,"Go":0,"Other":3}
function = {"Simple":2,"Payment":1,"High":0}
CodeSize = {"Small":2,"Medium":1,"High":0}


with open('Normal_Pickle','rb') as f:
    normal_model =  pickle.load(f)


def NormalPrediction(lang,fun,code):
    lang_map = language[lang]
    fun_map = function[fun]
    code_map = CodeSize[code]
    output = normal_model.predict([[0,0,code_map,fun_map,lang_map]])

    return output[0]
