# # 1.Introduction to the Data
# raw_hamlet = sc.textFile("hamlet.txt")
# raw_hamlet.take(5)

# 2.The Map Method
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)




# 3.Beyond Lambda Functions
# 4.The FlatMap Method
hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))


# 5.Filter Using a Named Function
# 6.Actions