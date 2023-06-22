class Person:
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationnlity = nationality
        self.age = age

    def __call__(self):
        print('ここはcall関数です')

    def say_hello(self, name):
        print('こんにちは、{}さん。私は{}です。'.format(name, self.name))


# インスタント化（実体化）
imanihi = Person('今西', '日本', 25)
mike = Person('マイク', 'アメリカ', 13)

imanihi.say_hello('佐藤')
mike.say_hello('佐藤')

imanihi()
# imanihi()
