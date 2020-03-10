names = ['Kazuma', 'Aqua', 'drakness', 'Megumin']
greeted_names = map(lambda x: 'Hi ' + x, names)

# This prints something similar to: <map object at Isekai>
print(greeted_names)
# Recall, that map returns an iterator 

# We can print all names in a for loop
for name in greeted_names:
    print(name)