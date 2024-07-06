from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from ecommbot.retrieval_generation import generate
from ecommbot.ingest import ingestdata

app = Flask(__name__)

load_dotenv()

vstore=ingestdata("done")
chain=generate(vstore)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    data = request.json
    msg = data.get('msg')
    print(msg)
    result=chain.invoke(msg)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)