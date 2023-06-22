def say_hello():
    print('みなさん、こんにちは')


say_hello()


def say_hello2(name):
    print('{}さん、こんにちは'.format((name)))


say_hello2('今西')
say_hello2('佐藤')


def calc_square(side):
    return side*side


result = calc_square(10)
print(result)

base = 10
height = 20
area = base*height*0.5


def calc_tri(base=10, height=10):
    return base*height*0.5


print(calc_tri(10, 20))
print(calc_tri())

# ここにコメントを追加しました。
