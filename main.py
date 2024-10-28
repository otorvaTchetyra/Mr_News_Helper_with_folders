import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from get_news import get_news
# from class_textGenr import textGenr (will apear issues in markoify library)
from create_blog_text import create_blog_text #(It helps avoid issues in 30 line)
from create_image_text import create_image_text
from create_image import create_image
from save_results import save_blog_text, save_image_text

def main(topic, from_date, to_date, language='ru', api_key='9e3c2104624d4b8982ba5bb8908aded3'):
    # news_data = get_news(topic, from_date, to_date, language, api_key)
    description = get_news(topic, from_date, to_date, language, api_key)
    title = get_news(topic, from_date, to_date, language, api_key) #I copyed 'get_news' to 'title' to avoid issue in 17 line
    # blog_text = textGenr(title, description)
    blog_text = create_blog_text(title, description)
    image_text = create_image_text(blog_text)
    
    save_blog_text(blog_text)
    create_image(image_text)
    save_image_text(image_text)

    print("Все результаты были сохранены.")

if __name__ == "__main__":
    topic = 'space'
    from_date = '2024-10-22'
    to_date = '2024-10-23'
    main(topic, from_date, to_date)

