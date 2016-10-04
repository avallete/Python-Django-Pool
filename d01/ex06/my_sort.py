# -*- coding: utf-8 -*-

def tupple_list_to_dict(src):
    dest = {}
    for tupple in src:
        if tupple[1] in dest.keys():
            dest[tupple[1]].append(tupple[0])
        else:
            dest[tupple[1]] = [tupple[0]]
    return dest

def run(debug=False):
    d = {'Hendrix':'1942','Allman':'1946','King':'1925','Clapton':'1945','Johnson':'1911',
        'Berry':'1926','Vaughan':'1954','Cooder':'1947','Page':'1944','Richards':'1943',
        'Hammett':'1962','Cobain':'1967','Garcia':'1942','Beck':'1944','Santana':'1947',
        'Ramone':'1948','White':'1975','Frusciante':'1970','Thompson':'1949',
        'Burton':'1939', }
    dict = tupple_list_to_dict(d.items())
    for date, names in sorted(dict.items(), key=lambda x: x[0]):
        if debug:
            print("%s :: %s" % (date, sorted(names)))
        else:
            for name in sorted(names):
                print(name)

if __name__ == '__main__':
    run()
