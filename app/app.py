from flask import Flask

APP = Flask(__name__)

@APP.route("/", methods=["GET])
def main() -> str: 
  return "hello world"
  
if __name__=="__main__": 
  APP.run("localhost", 5000)
