from flask import Flask, render_template, request, send_from_directory
import main

app = Flask(__name__)


# Routes
@app.route('/')
@app.route('/home',methods=['GET'])
def home(image=None,items=None):
    return render_template('home.html',image=image,items=items)

@app.route('/home',methods=['POST'])
def home_post():
    form_data = request.files['image']
    path = "temp/"+main.generate_random_filename('jpg')
    items = main.get_recommendation_objects(form_data,'./static/'+path)
    return render_template('home.html',image=path,items=items)

@app.route('/home/<item>',methods=['GET'])
def item(item):
    image_path = request.args.get('image_path')
    items = main.get_similar_objects(item,'./static/'+image_path)[:10]
    print(items)
    return render_template('item.html',image = image_path,items=items)

@app.route('/datasets/<path:filename>')
def serve_datasets(filename):
    return send_from_directory('datasets', filename)
    


if __name__ == '__main__':
    app.run(debug=True)
