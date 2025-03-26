from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/news")
def get_news():

    news = [ 

        {  
            "name": "Новость 1",

            "description": "Описание 1",

            "date": "26.03.25"
        },

        {
            "name": "Новость 2",

            "description": "Описание 2",

            "date": "26.03.25"
        },
        {

            "name": "Новость 3",

            "description": "Описание 3",

            "date": "26.03.25"

        },
        {

            "name": "Новость 4",

            "description": "Описание 4",

            "date": "26.03.25"
        },
    ]
    return jsonify(news)
def main():
    app.run("0.0.0.0", 8010, debug=True)

if __name__ == "__main__":
    main()