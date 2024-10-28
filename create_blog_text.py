# create_blog_text.py

def create_blog_text(title, description):
    return f"Заголовок: {title}\n\n{description}\n\n- Раннее обучение детей\n- Важный шаг к успешному будущему\n- Пример успешного опыта"

# This module saves blog text in folder "__pycache__" with module "save_results.py".
# Here I tryed to create blog text. I made handle blog text to avoid issues. Also this method helps avoid issues
# Below you can see class method textGenr. I tryed make class to generate blogs from file "blog_text.txt", but it shows a lot of errors ->
# -> and I decided to avoid the given method.



#_________________________________________________________
# class_textGenr.py

# import markovify


# class textGenr:
#     def __init__(self, title, description):
#         combined_text = f"{title}\n\n{description}"
#         self.model = markovify.Text(combined_text)
#         self.model.compile = self.model.compile()
    
#     def generate_sentence(self):
#         sentence = self.model.make_short_sentence(140)
#         if sentence is None:
#             raise ValueError("Не удалось создать текст.")
#         return sentence

# if __name__ == "__main__":
#     with open(r'D:\PythonProjects\Mr_News_Helper\blog_text.txt', encoding='utf-8') as file:
#         text = file.read()

#     title, _, description = text.partition('\n\n')
#     generator = textGenr(title, description)

#     try:
#         print(generator.generate_sentence())
#     except ValueError as e:
#         print(e)

