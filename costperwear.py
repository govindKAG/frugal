import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    remaining_years = scale % years
    sections = scale // years
    running_price = ogprice
    price_array = np.zeros(years) + running_price
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
    price = scale_real_time(
        price, years, scale) if scale is not None else price
    years = scale if scale is not None else years
    # if scale is not None:
    #    price = price * (scale/years)
    #    years = scale
    years_array = np.arange(1, years + 1, 1)
    #print(years_array)
    usage = usage
    #print('dimension of price array ', price.shape)
    #print('\n dimension of years_array ', years_array.shape)
    cpw = price / (years_array * usage)
    #print(cpw.shape)
    #print(years_array.shape)
    plt.xlabel('years', fontsize=18)
    plt.ylabel('cost per use', fontsize=16)
    plt.plot(years_array, cpw, label=label)
    plt.legend()


def compare(item1, item2):
    plt.figure()
    price1, years1, usage1, label1 = item1
    price2, years2, usage2, label2 = item2
    scale = max(years1, years2)
    scale1 = scale if years1 < scale else None
    scale2 = scale if years2 < scale else None
    plot_cpw(price1, years1, usage1, scale=scale1, label=label1)
    plot_cpw(price2, years2, usage2, scale=scale2, label=label2)

#plot_cpw(5000, 30, 365, label = 'bifl')
#plot_cpw(300, 2, 365, scale=30, label = 'normal')


#plot_cpw(5000, 15, 365, label = 'bifl backpack')
#plot_cpw(2000, 2, 365, scale=15, label = 'normal backpack')
#
#plot_cpw(1600, 15, 365, label = 'nalgene')
#plot_cpw(300, 2, 365, scale=15, label = 'normal')
compare((5000, 15, 365, 'bifl backpack'), (2000, 2, 365, 'normal backpack'))
compare((5499, 20, 365, 'mechanical board'), (300, 2, 365, 'rubber dome'))

#scale_real_time(3000, 3, 15)
#scale_real_time(3000, 3, 17)
#scale_real_time(43000, 3, 17)
#print(scaled_cpw(200, 0.5, 20, scale = 15))

plt.show()
