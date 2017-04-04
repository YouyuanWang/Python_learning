# coding:utf-8

from os import walk

def find_keywords(key,catalog):
    found_list = []
    for dirpath, dirnames, filenames in walk(catalog):
        for name in filenames:
            full_name = dirpath + '\\' + name
            if key in name:
                found_list.append(full_name)
            with open(full_name) as f:
                for l in f.readlines():
                    if key in l:
                        found_list.append(full_name + ':' + l)
    return found_list

keywords = raw_input('please input the search word:')
catalog = 'C:\Python27'

result = find_keywords(keywords,catalog)

print 'The result is : '
for r in result:
    print r


