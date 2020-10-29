from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return "<h1>Cardiovascular Disease</h1>"

if __name__ == "__main__":
    app.run()