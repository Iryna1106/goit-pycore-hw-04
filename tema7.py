import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')
