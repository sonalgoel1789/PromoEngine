import unittest
from main import SKU, Bought, Promos


class PromoTest(unittest.TestCase):
    def test_case1(self):
        sku_ob = SKU(['A', 'B', 'C', 'D'], [50, 30, 20, 15])
        sku = sku_ob.create_mp()

        promos_ob = Promos([['A'], ['B'], ['C', 'D']], [[3], [2], [1, 1]], [[130], [45], [30]])
        promos = promos_ob.consolidate  # [items] [no. of items] [promo_cost]

        bought_ob = Bought(['A', 'B', 'C', 'D'], [5, 5, 1, 2])  # {item:no. of items}
        final_amt = bought_ob.apply_promo(promos_ob, sku_ob)

        self.assertEqual(final_amt, 400)


if __name__ == '__main__':
    unittest.main()
