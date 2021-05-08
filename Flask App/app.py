from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


webapp = Flask(__name__)
####################################################################################################################
#set up our database
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'   #we using sqlite db cos its easy
db = SQLAlchemy(webapp)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) #this field cannot be fasle
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Author not available')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #the function below printouts after a new post is created
    def __repr__(self):
        return 'Blog Post' + str(self.id)




####################################################################################################################



#just some dummy data and send to the post
all_posts = [
    {'title':'Post 1',
     'content': 'This is just a post, lets give it an id 1',
     'author':'Jon Kwame'
     },
     {'title':'Post 2',
     'content': 'This is just a post, lets give it an id 2',
     'author':'Eyram'
     },
     {'title':'Post 3',
     'content': 'This is just a post, lets give it an id 3',
     'author':'Efo Kofi'
     }
]

@webapp.route('/')
@webapp.route('/home')
def home():
    return render_template('index.html')

@webapp.route('/posts')
def post():
    return render_template('posts.html', posts=all_posts)

@webapp.route('/about')
def about():
    return "Welcome to about page"


#somethingn good for dynamic urls
@webapp.route('/<string:value>')
def something(value):
    return "Hello, you typed " + value + " in your url"

#limiting web pages to only specific requests... just pass the specific requet names to the methods list
@webapp.route('/onlyget', methods=['GET'])
def get_only():
    return 'You can only use get requests'









if __name__ == '__main__':
    webapp.run(debug=True)