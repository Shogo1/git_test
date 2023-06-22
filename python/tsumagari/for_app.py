last_names = ['今西', '砂糖', '鈴木', '田中']
first_names = ['航平', '仗助', '康二', '浩介']

# for i in range(len(last_names)):
#     print(last_names[i]+first_names[i]+'さん')

for last_name, first_name in zip(last_names, first_names):
    print(last_name+first_name+'さん')

# for i in range(len(last_names)):
#     print('出席番号', i, '番目の'+last_names[i]+'さん')

for num, last_name in enumerate(last_names):
    print('出席番号', num, '番目の'+last_name+'さん')
