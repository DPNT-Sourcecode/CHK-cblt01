

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    product_dict = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    cost = 0
    product_amounts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    for i in range(len(skus)):

        curr = skus[i]

        if curr not in product_dict:
            return -1

        if curr == 'A':
            if (product_amounts[curr]+1)%3 == 0:
                cost += 30
            elif (product_amounts[curr]+1)%5 == 0:
                cost +=20
            product_amounts[curr] += 1
        elif curr == 'B' and (product_amounts[curr]+1)%2 == 0 and (product_amounts[curr]>0):
            product_amounts[curr] += 1
            cost += 15
        elif curr == 'E' and (product_amounts[curr]+1)%2 == 0:
            product_amounts[curr] += 1
            # Add 40 for E, subtract 30 for B, therefore +10:
            cost += 10
            product_amounts['B'] -= 1
        else:
            product_amounts[curr] += 1
            cost += product_dict[curr]

    return cost


if __name__ == '__main__':
    in1 = 'EEB'
    out1 = checkout(in1)
    print(out1)

