

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    product_dict = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    special_offers1 = {
        'A': ((3,130),(5,200)),
        'B': ((2,45),),
        'H': ((5,45),(10,80)),
        'K': ((2,150),),
        'P': ((5,200),),
        'Q': ((5,80),),
        'V': ((2,90),(3,130)),
    }

    special_offers2 = {
        'F': (2,1),
        'U': (3,1)
    }

    special_offers3 = {
        'E': (2,'B'),
        'N': (3,'M'),
        'R': (3,'Q')
    }

    cost = 0
    product_amounts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'J': 0,
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Y': 0,
        'Z': 0,

    }
    prod_list = ['A','C','D','E','B','F']

    for i in range(len(skus)):

        curr = skus[i]

        if curr not in product_dict:
            return -1

        if curr not in product_amounts:
            product_amounts[curr] = 1
        else:
            product_amounts[curr] += 1

    for key in 'ZYXWVUTSRQPONMLKJHGFEDCBA':

        if key in special_offers1:
            val = product_amounts[key]
            offers = special_offers1[key]
            print(offers)
            for i in range(len(offers)-1,-1,-1):
                cost += (val // offers[i][0])*offers[i][1]
                val = val % offers[i][0]
            if val>=0:
                cost += val*product_dict[key]
        elif key in special_offers2:
            val = product_amounts[key]
            offers = special_offers2[key]
            cost += (val//(offers[0]+1)) * offers[0]*product_dict[key]
            val = val%(offers[0]+1)
            if val>=0:
                cost += val*product_dict[key]
        elif key in special_offers3:
            key_to_reduce = special_offers3[key][1]
            multiple = special_offers3[key][0]
            product_amounts[key_to_reduce] -= product_amounts[key]//multiple
            cost += product_amounts[key] * product_dict[key]
        else:
            val = product_amounts[key]
            if val>=0:
                cost += val*product_dict[key]


        ######
        # if key == 'A':
        #     p1 = (product_amounts['A'] // 5)*200
        #     p2 = ((product_amounts['A'] % 5)//3)*130
        #     p3 = ((product_amounts['A']%5)%3)*50
        #     cost += (p1+p2+p3)
        # elif key == 'B':
        #     # cost += (product_amounts['B'] // 2)*45 + (product_amounts['B'] % 2)*30
        #     if product_amounts['B'] >= 0:
        #         cost += (product_amounts['B'] // 2)*45 + (product_amounts['B'] % 2)*30
        # elif key == 'E':
        #     product_amounts['B'] -= product_amounts['E']//2
        #     cost += product_amounts[key] * product_dict[key]
        # elif key == 'F':
        #     cost += (product_amounts[key]//3)*20 + (product_amounts[key]%3) * 10
        # else:
        #     cost += product_amounts[key] * product_dict[key]

    return cost


#if __name__ == '__main__':
#    in1 = 'ABCDE'
#    out1 = checkout(in1)
#    print(out1)



