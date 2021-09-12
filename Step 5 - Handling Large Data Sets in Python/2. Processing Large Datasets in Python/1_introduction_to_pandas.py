
'''1.Introduction'''
# import pandas as pd



'''2.Read a CSV with Pandas'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")

'''3.Dataframes'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# cars_shape = cars.shape
# print(cars_shape)
# first_six_rows = cars.head(6)
# print(first_six_rows)
# last_four_rows = cars.tail(4)
# print(last_four_rows)

'''4.Accessing Data with Indexes'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# cars_odd = cars.iloc[1::2, :3]
# fifth_odd_car_name = cars_odd.iat[4,0]
# last_four = cars_odd.tail(4)
# print(last_four)

'''5.Accessing Data with Names'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# cars.set_index('Name', inplace=True)
# weight_torino = cars.loc['Ford Torino', 'Weight']
# print(weight_torino)

'''6.Dataframe Indexes'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# cars.set_index('Name', inplace=True)
# honda_civic_hp = cars.loc['Honda Civic', 'Horsepower']
# print(honda_civic_hp)
# cars.reset_index(inplace=True)

'''7.Delving Deeper into Loc'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# numeric_data = cars.loc[:,'MPG':'Acceleration']
# numeric_data.head(5)
# print(numeric_data.head(5))

'''8.Selecting Columns'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# weights = cars['Weight']
# name_origin_0_and_3 = cars.loc[[0,3], ['Name', 'Origin']]
# print(name_origin_0_and_3)


'''9.Selecting Rows'''
# import pandas as pd
# cars = pd.read_csv("cars.csv")
# car_100 = cars.loc[99]
# cars_2_to_10 = cars.loc[1:9]
# print(cars_2_to_10)


'''10.Index Locations and Label Locations'''
import pandas as pd
cars = pd.read_csv("cars.csv")
num_rows = cars.shape[0]
one_index = pd.Index([num for num in range(1, num_rows+1)])
print(one_index)
cars.set_index(one_index, inplace=True)

car_100 = cars.loc[100]
cars_2_to_10 = cars.loc[2:10]
print(cars_2_to_10)
