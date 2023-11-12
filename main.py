# import requests
# import json 
# import flask
# def Response(name):
#     obj={"joewish":24,"Vikas":25}
#     if name=="joewish":
#         return json.dumps(obj[name])
#     else:
#         return "Key not present"

# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 

# creating a Flask app 
app = Flask(__name__) 

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 

		data = "hello world"
		return jsonify({'data': data}) 


# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 

	return jsonify({'data': num**2}) 

@app.route('/name/<string:name>', methods=["GET"])
def name(name):
	name=name.lower()
	obj={"joewish":"joewishvelagapalli@gmailcom","vikas":"vikaslikhy@gmail.com"}
	if name in obj:
		return jsonify({"name":name,"email":obj[name]})
	else:
		return jsonify({"message":"{0} are not a member, please request for new member sign up".format(name)})
	
	


# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
