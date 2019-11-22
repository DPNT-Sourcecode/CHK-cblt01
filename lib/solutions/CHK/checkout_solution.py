

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
    prod_list = ['A','C','D','E','B']

    for i in range(len(skus)):

        curr = skus[i]

        if curr not in product_dict:
            return -1

        product_amounts[curr] += 1
    print(product_amounts)
    print(cost)
    for key in prod_list:
        print(key)
        if key == 'A':
            p1 = (product_amounts['A'] // 5)*200
            p2 = ((product_amounts['A'] % 5)//3)*130
            p3 = ((product_amounts['A']%5)%3)*50
            cost += (p1+p2+p3)
            print(cost)
        elif key == 'B':
            cost += (product_amounts['B'] // 2)*45 + (product_amounts['B'] % 2)*30
        elif key == 'E':
            product_amounts['B'] -= product_amounts['E']//2
            cost += product_amounts[key] * product_dict[key]
        else:
            cost += product_amounts[key] * product_dict[key]
        print(product_amounts[key])
        print(cost)



    return cost


if __name__ == '__main__':
    in1 = 'AAAAAA'
    out1 = checkout(in1)
    print(out1)
