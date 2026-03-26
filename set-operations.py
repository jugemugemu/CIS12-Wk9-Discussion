def value_counts(values:tuple) -> dict:
    '''Returns a dictionary of distinct elements in a tuple mapped to their frequency.

    :param values: a tuple containing distinct and/or duplicate elements
    :return: a dictionary mapping the tuple's distinct elements to their total number of occurrences in the tuple
    '''
    counter = {}
    for value in values:
        counter[value] = counter.get(value, 0)
        counter[value] += 1
    return counter

def invert_dict(d:dict) -> dict:
    '''Returns an inverted dictionary where the key-value pair is swapped.

    :param d: the dictionary to be inverted
    :return: the inverted dictionary
    '''
    new = {}
    for key, value in d.items():
        new[value] = new.get(value, [])
        new[value].append(key)
    return new

def inverted_counts(values:tuple) -> dict:
    '''Returns a dictionary that maps integers to a list of elements in the given tuple that occur that many times.

    :param values: tuple to be counted, then inverted
    :return: dictionary containing integer keys with to lists of elements appearing that many times
    '''
    return invert_dict(value_counts(values))

def is_valid_set(a:tuple) -> bool:
    '''Returns True or False whether the given tuple's elements are distinct or not.

    :param a: the tuple being tested
    :return: True or False
    '''
    return len(a) == len(value_counts(a))

def make_distinct(a:tuple) -> tuple:
    '''Return a tuple of distinct elements from a given tuple.

    :param a: tuple to be made distinct
    :return: a tuple with distinct elements
    '''
    return tuple(value_counts(a).keys())

def union(a:tuple, b:tuple) -> tuple:
    '''Returns a tuple of distinct elements consisting of the elements from tuples a and b.

    :param a: the first tuple
    :param b: the second tuple
    :return: the union of the two tuples
    '''
    return tuple(make_distinct(a + b))

def intersect(a:tuple, b:tuple) -> tuple:
    '''Returns a tuple of distinct elements consisting of the elements shared by both tuples a and b.

    :param a: the first tuple
    :param b: the second tuple
    :return: the intersection of the two tuples
    '''
    return tuple(inverted_counts(a + b).get(2, []))

def are_disjointed(a: tuple, b: tuple) -> bool:
    '''Returns True or False whether the two tuples don't have any elements in common or do.

    :param a: the first tuple
    :param b: the second tuple
    :return: True or False
    '''
    return intersect(a, b) == ()

def difference(a:tuple, b:tuple) -> tuple:
    '''Returns a tuple of distinct elements consisting of elements in tuple a not found in tuple b.

    :param a: the tuple to be 'subtracted' by b
    :param b: the tuple to 'subtract' into a
    :return: tuple but with distinct elements containing no elements from b
    '''
    c = a + intersect(a, b) # Double up on the shared elements to filter out later
    distinct_elements = inverted_counts(c).get(1, [])
    return tuple(distinct_elements)

def symmetric_difference(a:tuple, b:tuple) -> tuple:
    '''Returns the symmetric difference of tuples a and b.

    :param a: the first tuple
    :param b: the second tuple
    :return: tuple of distinct elements consisting of elements exclusively in tuples a or b
    '''
    distinct_elements = inverted_counts(a + b).get(1, [])
    return tuple(distinct_elements)

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
    print(f'D = {D} -- {set_responses[is_valid_set(D)]}, but {make_distinct(D)} does')

    print('\nCounting Values and Inverting Dictionaries')
    counts = value_counts(A + B)
    print(f'The function value_counts(A + B) produces the dictionary {counts}')
    invert_counts = invert_dict(counts)
    print(f'Inverting this with the function invert_dict(value_counts(A + B)) gives {invert_counts}')
    print(f'The keys {invert_counts.keys()} are the occurrences of the elements.')
    print(f'{invert_counts.get(1, [])} is the list of the elements that occur once, and')
    print(f'{invert_counts.get(2, [])} is the list of the elements that occur twice.')
    print(f'{invert_counts.get(3, [])} is the list of the elements that occur three times.')
    print(f'As there are none (nor a key entry of 3), the default value is given, which is an empty list')

    print('\nUnion Operations')
    print(f'A ∪ B = {union(A, B)}')
    print(f'A ∪ C = {union(A, C)}')

    print('\nIntersect Operations')
    print(f'A ∩ B = {intersect(A, B)}')
    print(f'A ∩ C = {intersect(A, C)}')

    print('\nCheck if Tuples are Disjointed')
    disjoint_responses = {True: 'disjointed',
                          False: 'not disjointed'}
    print(f'A and B are {disjoint_responses[are_disjointed(A, B)]}')
    print(f'A and C are {disjoint_responses[are_disjointed(A, C)]}')
    print(f'C and B are {disjoint_responses[are_disjointed(C, B)]}')

    print('\nDifference Operations')
    print(f'A - B = {difference(A, B)}')
    print(f'B - A = {difference(B, A)}')
    print(f'A - C = {difference(A, C)}')

    print('\nSymmetric Difference Operations')
    print(f'A △ B = {symmetric_difference(A, B)}')
