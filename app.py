from flask import Flask,render_template, request, jsonify
import numpy as np
from fastai.vision.all import *
import pickle
import io
import os
from PIL import Image

# Initialiazing flask app
app = Flask(__name__)

def parent_label_multi(o):
    return [Path(o).parent.name]

# Loading  saved model
model = load_learner('model/exportMulticat.pkl', cpu=True)

# Rendering index.html at /
@app.route('/')
def index():
    return render_template('index.html')

# Getting data with POST Method
@app.route('/upload', methods=["POST"])
def upload():
    # try:
        # Getting img from POST
        file = request.files['user-img'].read()
        img = PILImage.create(file)
        prediction,pred_idx,probs = model.predict(img)

        # Getting Prediction ready to sent it to frontend
        print('prediction:', prediction)
        response = {"result": str(prediction)}
        return jsonify(response)

if __name__ == '__main__':
    port = os.getenv('PORT',5000)
    app.run(host='0.0.0.0', port=port)
