def sum_num_len(*args):
    summa = 0
    def process_(*elem):
        nonlocal summa
        for i in elem:
            if isinstance(i,(int, float)):
                summa += i
            elif isinstance(i,(str)):
                summa += len(i)
            elif isinstance(i,(tuple, set, list)):
                process_(*i)
            elif isinstance(i,dict):
                process_(*i.keys())
                process_(*i.values())
    process_(*args)
    return summa
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = sum_num_len(data_structure)
print(result)

