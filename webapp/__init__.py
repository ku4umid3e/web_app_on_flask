from flask import Flask, render_template
from dotenv import load_dotenv
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():
    load_dotenv()
    app = Flask(__name__)

    @app.route("/")
    def index():
        title = "Прогноз погоды"
        news = get_python_news()
        weather = weather_by_city("st petersburg, russia")
        return render_template(
                                "index.html",
                                page_title=title,
                                weather=weather,
                                news_list=news
                                )
    return app
