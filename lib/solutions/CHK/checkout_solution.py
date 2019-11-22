

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    product_dict = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }

    cost = 0
    product_amounts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0
    }
    prod_list = ['A','C','D','E','B','F']

    for i in range(len(skus)):

        curr = skus[i]

        if curr not in product_dict:
            return -1

        product_amounts[curr] += 1
    for key in prod_list:
        if key == 'A':
            p1 = (product_amounts['A'] // 5)*200
            p2 = ((product_amounts['A'] % 5)//3)*130
            p3 = ((product_amounts['A']%5)%3)*50
            cost += (p1+p2+p3)
        elif key == 'B':
            # cost += (product_amounts['B'] // 2)*45 + (product_amounts['B'] % 2)*30
            if product_amounts['B'] >= 0:
                cost += (product_amounts['B'] // 2)*45 + (product_amounts['B'] % 2)*30
        elif key == 'E':
            product_amounts['B'] -= product_amounts['E']//2
            cost += product_amounts[key] * product_dict[key]
        elif key == 'F':
            cost += (product_amounts[key]//3)*20 + (product_amounts[key]%3) * 10
        else:
            cost += product_amounts[key] * product_dict[key]

    return cost


#if __name__ == '__main__':
#    in1 = 'ABCDE'
#    out1 = checkout(in1)
#    print(out1)
