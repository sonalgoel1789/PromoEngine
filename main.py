def apply(promos):
    mp = {}
    tov = 0
    for p in promos:  # iterate the promos
        min_times = 99999  # minimum times an offer should be applied, if 2C+D is an offer, only once is applied to D
        for its in range(len(p[0])):  # iterate the count in promo items, 2C+D has 2 for C and 1 for D
            stu = p[0][its]  # name of the item
            if stu in bought:  # count the maximum times an offer can be applied to an item
                promo_cnt = p[1][its]
                bought_cnt = bought[stu]
                times_to_app = bought_cnt // promo_cnt
                if times_to_app < min_times:  min_times = times_to_app
            else:
                min_times = 0
                break
        tov += min_times * (p[2][0])  # apply the offer
        for its in range(len(p[0])):
            stu = p[0][its]
            if stu in bought:
                bought[stu] -= min_times * p[1][its]
                tov += bought[stu] * sku[stu]  # add the amount not included in offer, for 2C+D this will add C
    return tov  # return the total amount



if __name__ == "__main__":
    sku = {'A': 50, 'B': 30, 'C': 20, 'D': 15}  # {item:cost}
    promos = [[['A'], [3], [130]], [['B'], [2], [45]],
              [['C', 'D'], [1, 1], [30]]]  # [items] [no. of items] [promo_cost]
    bought = {'A': 5, 'B': 5, 'C': 1, 'D': 2}  # {item:no. of items}
    total_offer_value = apply(promos)
