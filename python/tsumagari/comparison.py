names = ['今西', '鈴木', '砂糖']
print(type(names))
print(names)
scores = [50, 80, 60]
print(scores)

scores.append(70)
print(scores)
scores.pop(0)
print(scores)

scores = {'国語': 50, '数学': 80, '英語': 60}
print(scores['国語'])
scores['理科'] = 70
print(scores)
scores['社会'] = 100
print(scores)
