from flask import Flask, render_template
from dotenv import load_dotenv
from weather import weather_by_city
from python_org_news import get_python_news


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


if __name__ == "__main__":
    app.run(debug=True)
