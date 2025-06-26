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
        '<li><a href="/get_dishes?user_id=1&page=0">Page 0</a></li>'
        '<li><a href="/get_dishes?user_id=1&page=1">Page 1</a></li>'
        '<li><a href="/get_dishes?user_id=2&page=0">User 2, Page 0</a></li>'
        "</ul>"
    )

@app.route('/dishes')
def get_dishes():
    try:
        user_id = request.args.get('userId')
        if user_id is None:
            return jsonify({'error': 'Missing user_id parameter'}), 400
        user_id = int(user_id)
        page = int(request.args.get('page', 0))
        all_dishes = data_science.selected
        user_dishes = get_user_dishes(user_id, all_dishes)
        page_dishes = user_dishes[page*5:(page+1)*5]
        return jsonify([dish.get('dish_name', 'Unknown') for dish in page_dishes])
    except ValueError:
        return jsonify({'error': 'Invalid user_id or page parameter'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)