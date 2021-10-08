d = {'person': 2, 'cat': 4, 'spider': 8}
for balls in d.items():
    print('A {} has legs'.format(balls))

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))

y = 2.5
print(type(y))
print(y, y + 1, y * 2, y ** 2)

t, f = True, False
print(type(t))

what = 'what'
tf = 'tf'
print (what, tf, len(what))

print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;

shut = 'shut'
up = 'up'
su12 = '{} {} {}'.format(shut, up, 12)
print(su12)

xs = [3, 1, 2]   # Create a list
print(xs, xs[2])
print(xs[-1], xs[-2], xs[-3])

xs[-2] = 'good',
print(xs)