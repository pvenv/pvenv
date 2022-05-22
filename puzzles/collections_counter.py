'''
Найти кол-во букв "И" в тексте
'''

from collections import Counter

#пример 1

# text = 'Привет мир!'

# text_cnt = Counter(text)
# print(f'{text_cnt=}')

# i_cnt = text_cnt['и']
# print(f'{i_cnt=}')

############################

#пример 2, когда мы не обращаем внимание на регистр

# text = 'ПрИвет мир!'

# text_cnt = Counter(text.lower())
# print(f'{text_cnt=}')

# i_cnt = text_cnt['и']
# print(f'{i_cnt=}')