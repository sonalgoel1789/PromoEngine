def prom_mp(promos):
    mp = {}
    tov = 0
    for p in promos:
        k = ''
        min_times = 99999
        for its in range(len(p[0])):
            stu = p[0][its]
            k += stu + "+"
            if stu in bought:
                promo_cnt = p[1][its]
                bought_cnt = bought[stu]
                times_to_app = bought_cnt // promo_cnt
                if times_to_app < min_times:  min_times = times_to_app
                # mod_left = bought_cnt%promo_cnt
                # prom_amt_curr = times_to_app*p[2][0]
                # left_amt_curr = mod_left*sku[stu]
                # amt = prom_amt_curr + left_amt_curr
            else:
                min_times = 0
                break
        tov += min_times * (p[2][0])
        for its in range(len(p[0])):
            stu = p[0][its]
            if stu in bought:
                bought[stu] -= min_times * p[1][its]
                tov += bought[stu] * sku[stu]
    return tov


if __name__ == "__main__":
    sku = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    promos = [[['A'], [3], [130]], [['B'], [2], [45]], [['C', 'D'], [1, 1], [30]]]  # [items] [no. of items] [cost]
    bought = {'A': 5, 'B': 5, 'C': 1, 'D': 2}  # {item:no. of items}
    prom_mp(promos)
