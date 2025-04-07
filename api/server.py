from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def index():
    return "Hello world"

@app.get("/api/news")
def get_news():
    news = [
        {
            "name": "Новость 1",
            "description": "Описание 1",
            "date": "2023-04-01"
        },
        {
             "name": "Новость 2",
            "description": "Описание 2",
            "date": "2023-04-01"
        },
        {
            "name": "Новость 3",
            "description": "Описание 3",
            "date": "2023-04-01"
        }
    ]
    return jsonify(news)

def main():
    app.run("0.0.0.0", 8010, True)

if __name__ == "__main__":
    main()