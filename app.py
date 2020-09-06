from flask import Flask,request,url_for,redirect,render_template
import pickle
import random
import sys
import numpy as np 

app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
#create global dictionary
previousCrops={}
@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():  
  # store all input values temperature,humidity,rainfall,ph
  temp=request.args.get('temperature')
  hum=request.args.get('humidity')
  rainfall=request.args.get('rainfall')
  ph=request.args.get('ph')
  #store crops in an list
  crops=['rice','wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
  #check if the entered values are already available in the dictionary if yes then return stored crop
  result='rice'
  givenData=str(temp)+" "+str(hum)+" "+str(ph)+" "+str(rainfall)
  print('This is standard output', file=sys.stdout)
  print(givenData, file=sys.stdout)
  #print(previousCrops, file=sys.stdout)
  if givenData in previousCrops:
      result=previousCrops[givenData]
  else:
      result=random.choice(crops) #get a random crop as result
      previousCrops[givenData]=result #store it in dictionary
  return render_template('index.html',pred='Predicted Crop is {}'.format(result))
  
if __name__ == '__main__':
  app.run(debug=True)

