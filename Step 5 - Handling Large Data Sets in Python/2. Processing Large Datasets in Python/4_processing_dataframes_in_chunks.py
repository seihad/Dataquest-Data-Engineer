'''2.Processing Chunks'''
# import pandas as pd
# import matplotlib.pyplot as plt
# memory_footprints = []
# moma = pd.read_csv("moma.csv", chunksize=250)

# for chunk in moma:
#     memory_footprints.append(chunk.memory_usage(deep=True).sum()/(1024*1024))
# plt.hist(memory_footprints)
# plt.show()

'''3.Counting Across Chunks'''
# import pandas as pd
# iter_chunks = pd.read_csv("moma.csv", chunksize=250)
# num_rows = 0
# for chunk in iter_chunks:
#     num_rows += len(chunk)
# print(num_rows)


'''4.Batch Processing'''
# import pandas as pd
# lifespans = []
# dtypes = {"ConstituentBeginDate": "float", "ConstituentEndDate": "float"}
# chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype=dtypes)
# for chunk in chunk_iter:
#     diff = chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate']
#     lifespans.append(diff)
# lifespans_dist = pd.concat(lifespans)
# print(lifespans_dist)

'''5.Optimizing Performance'''

'''6.Counting Unique Values'''
# import pandas as pd
# iter_chunks = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
# overall_vc = []
# for chunk in iter_chunks:
#     count = chunk['Gender'].value_counts()
#     overall_vc.append(count)
# combined_vc = pd.concat(overall_vc)
# print(combined_vc)


'''7.Combining Chunks Using GroupBy'''
# import pandas as pd
# iter_chunks = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
# overall_vc = []
# for chunk in iter_chunks:
#     count = chunk['Gender'].value_counts()
#     overall_vc.append(count)
# combined_vc = pd.concat(overall_vc)
# final_vc = combined_vc.groupby(combined_vc.index).sum()
# print(final_vc)


'''8.Working With Intermediate Dataframes'''
import pandas as pd
chunk_iter = pd.read_csv("moma.csv", chunksize=1000, usecols=['Gender', 'ExhibitionID'])
df_list = []
for chunk in chunk_iter:
    temp = chunk['Gender'].groupby(chunk['ExhibitionID']).value_counts()
    df_list.append(temp)
final_df = pd.concat(df_list)
id_gender_counts = final_df.groupby(final_df.index).sum()
print(id_gender_counts)
