import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)


#get_data()       

#this method is created to create data in DB.
def post_data():
    data={
        'name':'neeraj',
        'roll':222,
        'city':'lay'
        }


    json_data = json.dumps(data)
    r = requests.post(url= URL, data = json_data)
    data = r.json()
    print(data)

post_data()     

#this method use to update data 
def update_data():
    data={
        'id':8,
        'name':'suraj',
        'city':'kullu'
    }

    json_data = json.dumps(data)
    r = requests.put(url= URL, data = json_data)
    data = r.json()
    print(data)


#update_data()    


#This method is use to delete data from DB
def delete_data():
    data={
        'id':3
    }

    json_data = json.dumps(data)
    r = requests.delete(url= URL, data = json_data)
    data = r.json()
    print(data)

#delete_data()    