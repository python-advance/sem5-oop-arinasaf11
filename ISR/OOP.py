class Post: #родительский класс 
    def __init__(self, author, content):
        import datetime
        self.author = author
        self._content = content #контент поста полускрытый
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
        Post.__init__(self, author = author, content = content)
        #super(Comment, self).__init__(author=author, content=content)
        


if __name__ == "__main__":
    post = Post("Деканат", "Всем должникам придти в 13:30 в кабинет 200")
    post.add_comment(Comment("Олег", "Хорошо"))
    post.add_comment(Comment("Кирилл", "А где находится 200 кабинет?"))

    print("POST")
    post.show()
    print("COMMENTS")
    post.show_comments()
