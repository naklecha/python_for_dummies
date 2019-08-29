from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('myhtml.html', mymsg="helloworld", flag=1, arr=[1,2,3,4,5])

@app.route("/<custom_msg>", methods=['GET'])
def custom(custom_msg):
    return render_template('myhtml.html', mymsg=custom_msg, flag=1, arr=[1,2,3,4,5])
    
if __name__ == '__main__':
	app.run(host="0.0.0.0" , port = 4000 , debug = True)