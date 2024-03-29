

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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21,
    }

    special_offers1 = {
        'A': ((3,130),(5,200)),
        'B': ((2,45),),
        'H': ((5,45),(10,80)),
        'K': ((2,120),),
        'P': ((5,200),),
        'Q': ((3,80),),
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

    for key in 'WVURQPONMLKJIHGFEDCBA':

        if key in special_offers1:
            val = product_amounts[key]
            if val>=0:
                offers = special_offers1[key]
                #print(offers)
                for i in range(len(offers)-1,-1,-1):
                    cost += (val // offers[i][0])*offers[i][1]
                    val = val % offers[i][0]

                cost += val*product_dict[key]
        elif key in special_offers2:
            if val>=0:
                val = product_amounts[key]
                offers = special_offers2[key]
                cost += (val//(offers[0]+1)) * offers[0]*product_dict[key]
                val = val%(offers[0]+1)

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

    special_offer4_num = 0
    for key in 'ZYTSX':
        special_offer4_num += product_amounts[key]
    cost += (special_offer4_num // 3) * 45
    rest = special_offer4_num % 3
    #while rest > 0:
    for key in 'XSTYZ':
        curr = product_amounts[key]
        if rest<=curr:
            cost += product_dict[key] * rest
            break
        else:
            cost += product_dict[key] * curr
            rest -= curr

    return cost

