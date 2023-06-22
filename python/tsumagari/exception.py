def calc_try(base, height):
    return base*height*0.5


base = 10
height = '5'

try:
    rsult = calc_try(base, height)
    print('計算結果{}'.format(result))
except Exception as e:
    print('計算できません')
    print(e)
