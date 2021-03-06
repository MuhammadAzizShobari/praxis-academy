print('Simple Assignment')
shoplist = ['apple','mango','carrot','banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
#notice that both shoplist and mylist both print
#the same list without the 'apple' confirming that
#they point to the same object

print('Copy by making a full slice')
# make a Copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different