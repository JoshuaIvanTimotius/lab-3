import price_info


def test_total_cost_shopping():

    result = price_info.total_cost_shopping()

    assert (result == 46.75)

def test_cost_of_fruit():
    result = []
    price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95,
                  'pomegranate': 4.95}
    quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1,
                     'pomegranate': 2}
    fruit='orange'
    quantity=10

    result = price_info.cost_of_fruits(fruit, quantity)

    assert (result == 14)

