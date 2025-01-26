import itertools


def apply_func(func, iterator):
    for it in iterator:
        yield func(it)


def generate_squared_numbers(start=0):
    for number in itertools.count(start):
        yield number**2


def combine_iterators(*iterators):
    return itertools.chain.from_iterable(iterators)


infinite_gen = generate_squared_numbers(-3)
print("Generation until 0 element (from -3**2):")
print(' | '.join([str(next(infinite_gen)) for i in range(0)]))

print("Generation 1 element from same infinite generator:")
print(' | '.join([str(next(infinite_gen)) for i in range(1)]))

print("Generation until 11 element:")
print(' | '.join([str(next(infinite_gen)) for i in range(11)]))
print()


word_math = "MATH"
chars = iter(word_math)
tripled_chars = apply_func(lambda x: x * 3, chars)

print("Applying tripling symbols:")
# [print(next(tripled_chars, ''), end=' | ') for i in range(len(word_math))]

# Iterator walking with no StopIteration Exception
print(' | '.join(tripled_chars.__iter__()))
print()


iterator1 = apply_func(lambda x: x * 0.5, iter([0, 20, 40]))
iterator2 = itertools.combinations(word_math, 3)
iterator3 = iter(range(4, -6, -2))
combined_iterator = combine_iterators(iterator1, iterator2, iterator3)
print("Combining iterators into one:")
print(' | '.join([str(v) for v in combined_iterator.__iter__()]))