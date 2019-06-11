import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from item import Item

#years  = np.arange(1., 20., 0.5)
#cpw = lambda price, year, usage : price/(year * usage)
#vfunc = np.vectorize(cpw)
#cset = np.array([(1000, i, 20) for i in range(1,21)])
# print(cset)
# print(vfunc(cset))
sns.set_style('darkgrid')

# make this fn do both later


def scaled_cpw(price, years, usage, scale=None):
    price = price * (scale/years)
    years = scale
    return price


def scale_real_time(ogprice, years, scale):
    print(ogprice, years, scale, sep='===')

    if years == scale:
        return ogprice

    remaining_years = scale % years
    sections        = scale // years
    running_price   = ogprice
    price_array     = np.zeros(years) + running_price

    running_price += ogprice

    for i in range(sections - 1):
        price_array = np.concatenate(
            (price_array, np.zeros(years) + running_price))
        running_price += ogprice
    if remaining_years > 0:
        running_price += ogprice
        price_array = np.concatenate(
            (price_array, np.zeros(remaining_years) + running_price))
    return price_array


def plot_cpw(price, years, usage, scale=None, label=None):
    price       = scale_real_time(
                           price, years, scale) if scale is not None else price
    years       = scale if scale is not None else years
    years_array = np.arange(1, years + 1, 1)
    usage       = usage
    cpw         = price / (years_array * usage)
    plt.xlabel('years', fontsize=18)
    plt.ylabel('cost per use', fontsize=16)
    plt.plot(years_array, cpw, label=label)
    plt.legend()


def compare(item1, item2):
    ''' 
    plot two cost per use curve scaled over the life time of the product with the longer overall life time 
    each item is a tuple of the form (price, years it lasts, amount of expected uses per year, name )
    years must be an integer
    '''
    plt.figure()
    price1, years1, usage1, label1 = item1
    price2, years2, usage2, label2 = item2
    scale  = max(years1, years2)
    scale1 = scale if years1 < scale else None
    scale2 = scale if years2 < scale else None
    plot_cpw(price1, years1, usage1, scale=scale1, label=label1)
    plot_cpw(price2, years2, usage2, scale=scale2, label=label2)

#figure how to scale from within this function
def compare_all(items, scale=None):
    ''' 
    plot cost per use curve for a list of items scaled over the lifetime 
    of the longest lasting product
    '''
    for price, years, usage, label in items:
        plot_cpw(price, years, usage, label = label, scale = scale)


compare((5000, 15, 365, 'bifl backpack')   , (2000, 2, 365, 'normal backpack'))
compare((5499, 20, 365, 'mechanical board'), (300 , 2, 365, 'rubber dome'))

# unit tests
bifl_backpack = Item().called('bifl backpack item').whichcosts(5000).whichlasts(15).used(365)
print(bifl_backpack)
print(bifl_backpack.as_tuple())
normal_backpack = Item().called('normal backpack item').whichcosts(2000).whichlasts(2).used(365)
compare(bifl_backpack.as_tuple(), normal_backpack.as_tuple())

plt.show()
