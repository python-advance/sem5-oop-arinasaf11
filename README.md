# Инвариантная самостоятельная работа

2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

```python
class Post: #родительский класс 
    def __init__(self, author, content):
        import datetime
        self.author = author
        self._content = content
        self.date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        self.comments = list()

    @property
    def content(self):
        return self._content

    def add_comment(self, comment):
        self.comments.append(comment)

    @content.setter
    def content(self, content):
        self._content = content

    @content.getter
    def content(self):
        return self._content

    def show(self):
        print("Date: " + str(self.date))
        print("Author: " + str(self.author))
        print("Content: " + str(self._content))

    def show_comments(self):
        for comment in self.comments:
            comment.show()
            print()


class Comment(Post):
    def __init__(self, author, content):
        super(Comment, self).__init__(author=author, content=content)


if __name__ == "__main__":
    post = Post("Деканат", "Всем должникам придти в 13:30 в кабинет 200")
    post.add_comment(Comment("Олег", "Хорошо"))
    post.add_comment(Comment("Кирилл", "А где находится 200 кабинет?"))

    print("POST")
    post.show()
    print()
    print("COMMENTS")
    post.show_comments()
```

![](https://github.com/python-advance/sem5-oop-arinasaf11/blob/master/ISR/post_comments.jpg?raw=true)

# Вариативная самостоятельная работа

3.1.

Разработка прототипа приложения “Регистрация на конференцию” на основе фрагмента технического задания с использованием ООП.

```python
import re 

"""
Создаем класс и пустой список для логгера
"""

class Conf():
  log = []
  
  """
  Описываем конструктор, где в качестве свойства выступает словарь с входящими полями формы 
  """
  def __init__(self, dict_conf):

    self.f_name = dict_conf["f_name"] 
    self.s_name = dict_conf["s_name"]
    self.email = dict_conf["email"]
    self.city = dict_conf["city"]

  
  """
  Создаем свойство класса @property для поля e-mail: getter, setter
  """
  @property
  def email(self):
      return self._email
    
  @email.setter
  def email(self, value):
    pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}" 
    number_re = re.compile(pattern) #компиляция выражения

    if (not (number_re.findall(str(value)))):
      raise ValueError('Неправильно введен адрес почты, проверьте правильность ввода!')
    else:
      self.log.append ("Успешно создан!")
      self._email = value

  
  """
  Создаем метод для получения данных из формы
  """
  def conf_client_info(self):
    self.participant_info = {
      "f_name": self.f_name,
      "s_name": self.s_name,
      "email": self.email,
      "city": self.city,
    }

    return self.participant_info

  """
  Метод возвращает строковое представление объекта.
  """
  def __str__(self):
    return (self.f_name + " " + self.s_name)


"""
Объявляем переменные для формы
"""
Fname = input("Введите имя:")
Sname = input("Введите фамилию:")
email = input("Введите почту:")
city = input("Введите город:")

info={"f_name":Fname,"s_name":Sname,"email":email, "city":city}

"""
Выводим значение полей
"""
g_info=Conf(info)
print(g_info.conf_client_info())

with open('Conf_log.txt', 'a') as f:
  f.write(str(g_info.log))
```

Результат:

![](https://github.com/python-advance/sem5-oop-arinasaf11/blob/master/VSR/conf.jpg?raw=true)
