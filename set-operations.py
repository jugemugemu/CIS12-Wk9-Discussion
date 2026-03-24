def value_counts(values:tuple) -> dict:
    counter = {}
    for value in values:
        counter[value] = counter.get(value, 0)
        counter[value] += 1
    return counter

def invert_dict(d:dict) -> dict:
    new = {}
    for key, value in d.items():
        new[value] = new.get(value, [])
        new[value].append(key)
    return new

def is_valid_set(a: tuple) -> bool:
    return len(a) == len(value_counts(a))

def union(a:tuple, b:tuple) -> tuple:
    return tuple(value_counts(a + b).keys())

def intersect(a:tuple, b:tuple) -> tuple:
    return tuple(invert_dict(value_counts(a + b)).get(2, ()))

def are_disjointed(a: tuple, b: tuple) -> bool:
    return intersect(a, b) == ()

def difference(a:tuple, b:tuple) -> tuple:
    return tuple(invert_dict(value_counts(a + intersect(a, b))).get(1, ()))

def symmetric_difference(a:tuple, b:tuple) -> tuple:
    return tuple(invert_dict(value_counts(a + b)).get(1, ()))

if __name__ == '__main__':
    A = (3, 6, 9, 12)
    B = (2, 4, 6, 8)
    C = (1, 5, 7, 11)
    D = (1, 1, 2, 3, 4)

    print('Sample Tuples')
    set_responses = {True: 'qualifies as a set',
                 False: 'does not qualify as a set'}
    print(f'A = {A} -- {set_responses[is_valid_set(A)]}')
    print(f'B = {B} -- {set_responses[is_valid_set(B)]}')
    print(f'C = {C} -- {set_responses[is_valid_set(C)]}')
    print(f'D = {D} -- {set_responses[is_valid_set(D)]}')

    print('\nUnion Operations')
    print(f'A ∪ B = {union(A, B)}')
    print(f'A ∪ C = {union(A, C)}')

    print('\nIntersect Operations')
    print(f'A ∩ B = {intersect(A, B)}')
    print(f'A ∩ C = {intersect(A, C)}')

    print('\nCheck if Tuples are Disjointed')
    disjoint_responses = {True: 'disjointed', False: 'not disjointed'}
    print(f'A and B are {disjoint_responses[are_disjointed(A, B)]}')
    print(f'A and C are {disjoint_responses[are_disjointed(A, C)]}')
    print(f'C and B are {disjoint_responses[are_disjointed(C, B)]}')

    print('\nDifference Operations')
    print(f'A - B = {difference(A, B)}')
    print(f'B - A = {difference(B, A)}')
    print(f'A - C = {difference(A, C)}')

    print('\nSymmetric Difference Operations')
    print(f'A △ B = {symmetric_difference(A, B)}')
