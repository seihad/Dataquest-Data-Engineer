'''1.Introduction'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# index = pd.Index([num for num in range(1, cars.shape[0] + 1)])
# cars.set_index(index,inplace=True)

'''2.Pandas Series'''


'''3.Arithmetic and Summary Statistics'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# max_weight = cars['Weight'].max()
# print(max_weight)
# min_weight = cars['Weight'].min()
# print(min_weight)

# weight_ratio = max_weight / min_weight
# print(weight_ratio)

'''4.Value Counts'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")

# origin_counts = cars['Origin'].value_counts()
# print(origin_counts)
# origin_counts_dict = origin_counts.to_dict()
# print(origin_counts_dict)


'''5. Filtering Rows'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")

# european_cars = cars[cars['Origin'] == 'Europe']
# print(european_cars.shape)

'''6.Logical Operators'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")

# non_us_cars = cars[~(cars['Origin'] == 'US')]
# low_mpg_horsepower = cars[(cars['MPG'] > 0) & (cars['MPG'] < 10) & (cars['Horsepower'] >= 150)]

# light_or_fast = cars[(cars['Weight'] <=2000 )| (cars['Acceleration'] >= 30)]

'''7.Masks with Column Selection'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# name_and_origin = cars.loc[(cars['MPG']>0) & (cars['MPG']<12) & (cars['Horsepower'] >= 200), ['Name', 'Origin']]
# print(name_and_origin)

'''8.Adding Columns'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")

# cars['PW_ratio'] = cars['Horsepower'] / cars['Weight']
# max_pw_ratio = cars['PW_ratio'].max()
# print(max_pw_ratio)


'''9.Column with Partial Data'''
import pandas as pd
cars = pd.read_csv("cars.csv")

mpg_l100_constant = 235.214583

mpg_non_zero = cars.loc[~(cars['MPG'] == 0),'MPG']
L100 = pd.Series()
L100 =  mpg_l100_constant / mpg_non_zero
cars['L/100'] = L100