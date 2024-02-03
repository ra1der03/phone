import re
from collections import defaultdict
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
names=[]
# TODO 1: выполните пункты 1-3 ДЗ
for i,item in enumerate(contacts_list):
  name=(((",".join(item[:3])).replace(',',' ').strip()).split(' '))
  [name.remove(x) for x in name if len(x)<4]
  contacts_list[i][:3]=name
  names.append(name)

for i, name in enumerate(names):
  for t,item in enumerate(contacts_list[1:]):
    if name[:3]!=item[:3] and name[:2]==item[:2]:
      if len(item[3])<1:
        contacts_list.remove(item)
      else:
        pass
count=[]
for i, item in enumerate(contacts_list):
  for m,meti in enumerate(contacts_list[::-1]):
    for y in range(1,len(item)):
      if item[:y]==meti[:y] and item[y]=='' and meti[y]!='' and item[y+1:]!=meti[y+1]:
        contacts_list[i][:y+1]=meti[:y+1]
      elif item[:y]==meti[:y] and item[y]=='' and meti[y]!='':
        contacts_list[i][:y+1]=meti[:y+1]
        count.append(i)
      elif item[:y]==meti[:y] and meti[y]=='' and item[y]!='':
        contacts_list[i][:y+1] = item[:y+1]
        count.append(i)
      else:
        continue
co=0
for i in count:
  contacts_list.remove(contacts_list[i-co])
  co += 1

result=''
pattern = r"(\+7|8)?\s?\(?(\d\d\d)\)?(\s?|\-?)(\d\d\d)\-?(\d+)\-?(\d\d)+(\s+\(?\w+\.?\s+\d+\)?)?"
for elem in contacts_list:
  result += ', '.join(elem)+', '

res = re.findall(pattern, result)
sub_pat = r"+7(\2)-\4-\5-\6 \7"
res = re.sub(pattern, sub_pat, result)
result, count = [], 0
for i in range(7, len(res.split(', '))+1, 7):
    result.append(res.split(', ')[i-7:i])
contacts_list=result
# pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)

