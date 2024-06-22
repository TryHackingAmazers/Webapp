from flask import Flask, render_template, request
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
    items = main.get_recommendation_objects(form_data)
    return render_template('home.html',image=form_data,items=items)


if __name__ == '__main__':
    app.run(debug=True)
