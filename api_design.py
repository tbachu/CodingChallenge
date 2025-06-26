from flask import Flask, request, jsonify
import random
import data_science

app = Flask(__name__)


def get_user_dishes(user_id, dishes):
    random.seed(user_id)
    return random.sample(dishes, len(dishes))

@app.route('/')
def home():
    return (
        "<h1>Flask API is Running!</h1>"
        "<p>Test the API with these links:</p>"
        "<ul>"
        '<li><a href="/dishes?userId=1&page=0">Page 0</a></li>'
        '<li><a href="/dishes?userId=1&page=1">Page 1</a></li>'
        '<li><a href="/dishes?userId=2&page=0">User 2, Page 0</a></li>'
        "</ul>"
    )

@app.route('/dishes')
def get_dishes():
    user_id = int(request.args.get('userId', 1))
    page = int(request.args.get('page', 0))
    all_dishes = data_science.selected
    user_dishes = get_user_dishes(user_id, all_dishes)
    page_dishes = user_dishes[page*5:(page+1)*5]
    return jsonify([dish['dish_name'] for dish in page_dishes])


if __name__ == '__main__':
    app.run(debug=True)