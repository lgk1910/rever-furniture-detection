from flask import Flask, render_template, request, jsonify
from google.protobuf.message import Error
import model
import time
import glob
import re

app = Flask(__name__)

@app.route('/')
def home():
    return "Real estate image Tagging using Transfer Learning model"

@app.route("/predict/", methods=['GET', 'POST'])

    
def post():
    def check_url(url):
        # Compile the ReGex
        p = re.compile(r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
        # If the string is empty 
        # return false
        if (url == None):
            return False
    
        # Return if the string 
        # matched the ReGex
        if(re.search(p, url)):
            return True
        else:
            return False
    
    # execution_time = time.time()
    try:
        content = request.json
        url_list = content["urls"]
        url_list_filtered = []
        for url in url_list:
            if check_url(str(url))==True:
                url_list_filtered.append(url)
        
        print(url_list_filtered)
        obj_list = []
        
        # Cleaning cache
        trained_model.delete_images(model.image_path)
        trained_model.delete_images('runs/detect/exp/')
        
        # Predict
        execution_time = time.time()
        trained_model.predict(url_list_filtered)
        # trained_model.transform_vec()
        obj_list = trained_model.transform_vec()
        Time = time.time() - execution_time
        
        # for file in glob.glob(model.save_dir+'*.txt'):
        #     with open(file, 'r') as f:
        #         obj_list.append(f.read())
        
        trained_model.delete_images(model.image_path)
        trained_model.delete_images('runs/detect/exp/')
  
        url_detect = list(zip(url_list_filtered,obj_list))
        return jsonify(num_urls = len(obj_list), value=url_detect, time=Time, avg_time=Time/len(obj_list)), 200
    except Error as e:
        print(e)
        return jsonify(label="Error"), 400

if __name__ == '__main__':
    trained_model = model.Model()
    app.run(debug=True)