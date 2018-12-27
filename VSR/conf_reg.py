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
