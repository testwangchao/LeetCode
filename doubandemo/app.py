from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

movie_data = [
    {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568902055.jpg",
        "movie_name": "爱尔兰人",
        "movie_score": "9.1"
    },
    {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2570137991.jpg",
        "movie_name": "82年生的金智英",
        "movie_score": "8.7"
    },
    {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2554514093.jpg",
        "movie_name": "新闻记者",
        "movie_score": "6.6"
    }, {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568902055.jpg",
        "movie_name": "爱尔兰人",
        "movie_score": "9.1"
    },
    {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2570137991.jpg",
        "movie_name": "82年生的金智英",
        "movie_score": "8.7"
    },
    {
        "img_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2554514093.jpg",
        "movie_name": "新闻记者",
        "movie_score": "6.6"
    }
]


@app.route('/')
def index():
    contexts = {"movies": movie_data, "tvs": movie_data}
    return render_template('index.html', **contexts)


@app.route('/list/')
def item_list():
    category = int(request.args.get("category"))
    if category == 1:
        items = movie_data
    else:
        items = movie_data
    return render_template('list.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=9999)
