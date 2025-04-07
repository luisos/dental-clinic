# -*- coding: utf-8 -*-

#--------------------------------------------
import cProfile
name = u"П’є-Блює Іван Петрович"
names = [name] * 100000
def test():
    #cProfile.run("map(titlecase, names)")
    cProfile.run("map(namelize, names)")
    cProfile.run("map(namelize2, names)")
    cProfile.run("map(namelize3, names)")
    cProfile.run("map(namelize4, names)")
#--------------------------------------------


import string
import re

ABC = u"абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def strcmp(s1, s2):
    #for c1, c2 in map(lambda c1,c2: (c1 or '', c2 or ''), s1.lower(), s2.lower()):
    for c1, c2 in map(None, s1.lower(), s2.lower()):
        try:
            result = cmp(ABC.index(c1), ABC.index(c2))
        except ValueError:
            result = cmp(c1, c2)
        if result:
            break
    return result

def titlecase(s):
    #return re.sub(r"[ -].", lambda mo: mo.group(0)[0] + mo.group(0)[1].upper(), s.capitalize())
    #return re.sub(r"-.", lambda mo: '-' + mo.group(0)[1].upper(), string.capwords(s))
    return '-'.join(map(lambda s: s[0].upper() + s[1:],string.capwords(s).split("-")))


def namelize(name):
    name = name.lower().split("-")
    return '-'.join([s[:1].upper() + s[1:] for s in name])


def namelize2(name):
    parts = string.capwords(name).split("-")
    name = parts[0]
    for p in parts[1:]:
        name += "-" + p[0].upper() + p[1:]
    return name


def namelize3(name):
    return '-'.join(map(string.capwords, name.split("-")))
    #return string.capwords(name)


def namelize4(name):
    return ''.join(map(string.capitalize, re.split(r"([ -]+)", name)))


if __name__ == '__main__':
    print(namelize(u"бонч-бруєвич"))
    test()
