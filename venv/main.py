from magicList import MagicList, Person

a = MagicList()
a[0]=5
print (a)


b = MagicList(cls_type=Person)
#b[0].age=1
print (b[0].age)