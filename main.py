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
	if authChecker():
		name=name.lower()
		obj={"joewish":"joewishvelagapalli@gmailcom","vikas":"vikaslikhy@gmail.com"}
		if name in obj:
			return jsonify({"name":name,"email":obj[name]})
	else:
		return jsonify({"message":"{0} are not a member, please request for new member sign up".format(name)})

# @app.route('/test/', methods=["GET"])
def authChecker():
	auth = str(request.headers.get("Authorization")).split(" ")
	if auth[0]=="Basic" and checkAuthList(auth[1]):
		return True
	else:
		return False
	

def checkAuthList(authID):
	
	if authID in listOfUsers:
		return True 
	else:
		return False 


# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
