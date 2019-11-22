

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
            cost += product_dict[curr]
        elif curr == 'A' and (product_amounts[curr]+1)%3 == 0:
            product_amounts[curr] += 1
            cost += 30
        elif curr == 'B' and (product_amounts[curr]+1)%2 == 0:
            product_amounts[curr] += 1
            cost += 15

        else:
            product_amounts[curr] += 1
            cost += product_dict[curr]

    return cost


#if __name__ == '__main__':
#    in1 = 'AAA'
#    out1 = checkout(in1)
#    print(out1)


