from flask import Flask, render_template, request, send_from_directory
import main

app = Flask(__name__)

labels = ["Bed","Cabinet","Carpet","Ceramic floor","Chair","Closet","Cupboard","Curtains","Dining Table","Door","Frame","Futec frame","Futech tiles","Gypsum Board","Lamp","Nightstand","Shelf","Sideboard","Sofa","TV stand","Table","Transparent Closet","Wall Panel","Window","Wooden floor"]

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
    return render_template('item.html',image = image_path,items=items)


@app.route('/property/choose',methods=['GET'])
def suggestions_choose():
    image_path = "sample_images/1235120e979e9e18ab93ca40683fa499.jpg"
    objects, path = main.preprocess_image(image_path)
    lab = []
    for i in range(len(objects)):
        lab.append(labels[int(objects[i][-1])])
    return render_template('property.html',objects=objects,image="temp/"+path,len_objects = len(objects),labels=lab,choose=False)

@app.route('/property/<id>',methods=['GET'])
def property_id(id):
    image_path = request.args.get('image_path')
    files = main.find_on_amazon("./static/"+image_path,int(id))
    return render_template('property.html',image=image_path,choose=True,items=files)
    
    

@app.route('/datasets/<path:filename>')
def serve_datasets(filename):
    return send_from_directory('datasets', filename)
    


if __name__ == '__main__':
    app.run(debug=True)
