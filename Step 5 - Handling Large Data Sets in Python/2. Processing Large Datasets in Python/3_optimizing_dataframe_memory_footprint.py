'''1.Introduction'''

'''2.Estimating Memory Consumption'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# print(moma.info())

'''3.How Pandas Represents Values in a Dataframe'''

# import pandas as pd
# moma = pd.read_csv("moma.csv")
# print(moma._data)

'''4.Different Types Have Different Memory Footprints'''

'''5.Estimating The Memory Manually'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# num_entries = moma.size
# total_bytes = num_entries * 8
# total_megabytes = total_bytes / (2 ** 20)
# print(total_megabytes)

'''6.Calculating the True Memory Footprint'''

'''7.Memory Footprint of Non-numerical Data'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# obj_cols = moma.select_dtypes(include=['object'])
# print(obj_cols)
# obj_cols_mem = obj_cols.memory_usage(deep=True)
# print(obj_cols_mem)
# obj_cols_sum = obj_cols_mem.sum() / (2 ** 20)
# print(obj_cols_sum)

'''8.Optimizing Integer Columns With Subtypes'''
# import numpy as np
# print(np.iinfo('int16').min)
# print(np.iinfo('float16').min)


'''9.Optimizing Integer Columns With Subtypes'''
# import numpy as np
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# def change_to_int(df, col_name):
#     # Get the minimum and maximum values
#     col_max = df[col_name].max()
#     col_min = df[col_name].min()
#     # Find the datatype
#     for dtype_name in ['int8', 'int16', 'int32', 'int64']:
#         # Check if this datatype can hold all values
#         if col_max <  np.iinfo(dtype_name).max and col_min > np.iinfo(dtype_name).min:
#             df[col_name] = df[col_name].astype(dtype_name)
#             break

# # Add you code below
# float_moma = moma.select_dtypes(include=['float64'])
# print(float_moma.isnull().sum())
# change_to_int(moma, 'ExhibitionSortOrder')
# print(moma['ExhibitionSortOrder'].dtype)


'''10.Optimizing Float Columns With Subtypes'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# float_cols = moma.select_dtypes(include=['float']).columns

# # Write you code below
# for col in float_cols:
#     moma[col] = pd.to_numeric(moma[col], downcast='float')
#     print(moma[col].dtype)



'''11.Converting To DateTime'''

'''12.Converting To DateTime'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])
# moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])

# print(moma[["ExhibitionBeginDate", "ExhibitionEndDate"]].memory_usage(deep=True))

'''13.Converting to Categorical to Save Memory'''

'''14.Converting to Categorical to Save Memory'''
# import pandas as pd
# moma = pd.read_csv("moma.csv")
# for col in moma.select_dtypes(include=['object']):
#     num_unique_values = len(moma[col].unique())
#     num_total_values = len(moma[col])
#     if num_unique_values / num_total_values < 0.5:
#         moma[col] = moma[col].astype('category')

# print(moma.info(memory_usage='deep'))


'''15.Selecting Types While Reading the Data In'''
import pandas as pd

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']
moma = pd.read_csv("moma.csv", parse_dates=['ExhibitionBeginDate', 'ExhibitionEndDate'], usecols=keep_cols)
print(moma.memory_usage(deep=True).sum()/(1024*1024))