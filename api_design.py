from flask import Flask, request, jsonify
import random
import data_science

app = Flask(__name__)


def get_user_dishes(user_id, dishes):
    random.seed(user_id)
    return random.sample(dishes, len(dishes))


@app.route('/get_dishes')
def get_dishes():
    user_id = int(request.args.get('user_id'))
    page = int(request.args.get('page', 0))
    all_dishes = data_science.selected
    user_dishes = get_user_dishes(user_id, all_dishes)
    page_dishes = user_dishes[page*5:(page+1)*5]
    return jsonify([dish['dish_name'] for dish in page_dishes])


if __name__ == '__main__':
    app.run(debug=True)