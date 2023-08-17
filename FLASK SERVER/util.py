import json,pickle
import numpy as np
location=None
model=None
data_col=None

def load_artifacts():
    global location
    global data_col
    with open('FLASK SERVER/artifacts/columns.json','r') as f:
        data_col=json.load(f)['data_columns']
        location=data_col[3:]
    global model
    if model is None:
        with open('FLASK SERVER/artifacts/home_prices_blr_model.pickle','rb') as f:
            model=pickle.load(f)
    print('loading artifacts...done')

def get_location():
    return location

def get_price(location,sqft,bhk,bath):
    try:
        location_ind=data_col.index(location.lower())
    except:
        location_ind=-1
    x=np.zeros(len(data_col))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if(location_ind>=0):
        x[location_ind]=1
    return round(model.predict([x])[0],3)





if(__name__=="__main__"):
    load_artifacts()
    # print(get_location())
    print(get_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_price('Ejipura', 1000, 2, 2))  # other location


