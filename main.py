class SKU:
    def __init__(self, items, amounts):
        self.items = items
        self.amounts = amounts
        self.mp = {}
        self.create_mp()

    def add(self, item, value):
        self.items.append(item)
        self.amounts.append(value)
        self.create_mp[item] = value
        return self.mp

    def create_mp(self):
        self.mp = dict(zip(self.items, self.amounts))
        return self.mp

class Promos:
    def __init__(self, item_list, item_cnt, offer_cost):
        self.item_list = item_list
        self.item_cnt = item_cnt
        self.offer_cost = offer_cost
        self.consolidated = []
        self.consolidate()

    def add(self, item_list, item_cnt, offer_cost):
        self.item_list.append(item_list)
        self.item_cnt.append(item_cnt)
        self.offer_cost.append(offer_cost)
        self.consolidated.append([item_list, item_cnt, offer_cost])

    def consolidate(self):
        out = []
        for i in range(len(self.item_list)):
            temp = [self.item_list[i], self.item_cnt[i], self.offer_cost[i]]
            out.append(temp)
        self.consolidated = out
        return out

class Bought:
    def __init__(self, items, count):
        self.items = items
        self.count = count
        self.bought = {}
        self.create_mp()

    def add(self, item, count):
        self.items.append(item)
        self.count.append(count)
        self.create_mp[item] = count
        return self.mp

    def create_mp(self):
        self.bought = dict(zip(self.items, self.count))
        return self.bought

    def apply_promo(self, promos, sku):
        mp = {}
        tov = 0
        count_flg = 0
        for p in promos.consolidate():  # iterate the promos
            min_times = 99999  # minimum times an offer should be applied, if 2C+D is an offer, only once is applied to D
            for its in range(len(p[0])):  # iterate the count in promo items, 2C+D has 2 for C and 1 for D
                stu = p[0][its]  # name of the item
                if stu in self.bought:  # count the maximum times an offer can be applied to an item
                    promo_cnt = p[1][its]
                    bought_cnt = self.bought[stu]
                    times_to_app = bought_cnt // promo_cnt
                    if times_to_app < min_times:  min_times = times_to_app
                else:
                    min_times = 0
                    break
            tov += min_times * (p[2][0])  # apply the offer

            for its in range(len(p[0])):
                stu = p[0][its]
                if stu in self.bought:
                    self.bought[stu] -= min_times * p[1][its]
                    tov += self.bought[stu] * sku.mp[stu]  # add the amount not included in offer, for 2C+D this will add C
                    count_flg = 1
        if count_flg ==0:
           print("No items bought")

        return tov  # return the total amount

if __name__ == "__main__":
    print(final_amt)
