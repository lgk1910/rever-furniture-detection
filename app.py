from flask import Flask, render_template, request, jsonify
from google.protobuf.message import Error
import model
import time
import glob

app = Flask(__name__)

@app.route('/')
def home():
    return "Real estate image Tagging using Transfer Learning model"

@app.route("/predict/", methods=['GET', 'POST'])
def post():
    # execution_time = time.time()
    try:
        content = request.json
        url_list = content["urls"]
        obj_list = []
        
        # Cleaning cache
        trained_model.delete_images(model.image_path)
        trained_model.delete_images('runs/detect/exp/')
        
        # Predict
        execution_time = time.time()
        trained_model.predict(url_list)
        trained_model.transform_vec()
        Time = time.time() - execution_time
        
        for file in glob.glob(model.save_dir+'*.txt'):
            with open(file, 'r') as f:
                obj_list.append(f.read())
        
        trained_model.delete_images(model.image_path)
        trained_model.delete_images('runs/detect/exp/')
  
        url_detect = list(zip(url_list,obj_list))
        return jsonify(value=url_detect, time=Time), 200
    except Error as e:
        print(e)
        return jsonify(label="Error"), 400

if __name__ == '__main__':
    trained_model = model.Model()
    app.run(debug=True)