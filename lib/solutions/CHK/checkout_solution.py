

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    product_dict = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    cost = 0
    product_amounts = {}
    for i in range(len(skus)):

        curr = skus[i]

        if curr not in product_dict:
            return -1

        if curr not in product_amounts:
            product_amounts[curr] = 1
        else:
            product_amounts[curr] += 1
    # raise NotImplementedError()

if __name__ == '__main__':
    in1 = 'ABCD'
    out1 = checkout(in1)



