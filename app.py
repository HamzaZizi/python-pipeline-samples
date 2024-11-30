# from flask import Flask , render_template
# app =   Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True , host='0.0.0.0', port=80)


from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/generate_random', methods=['GET'])
def generate_random():
    random_number = random.randint(1, 100)
    return jsonify(random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
