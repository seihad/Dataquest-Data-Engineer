# 2.Authenticating with the API
# headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
# params = {"t": "day"}
# response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

# python_top = response.json()



# # 3.Getting the Most Upvoted Post
# python_top_articles = python_top["data"]["children"]
# most_upvoted = ""
# most_upvotes = 0
# for article in python_top_articles:
#     ar = article["data"]
#     if ar["ups"] >= most_upvotes:
#         most_upvoted = ar["id"]
#         most_upvotes = ar["ups"]


# # 4.Getting Post Comments
# headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
# response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)

# comments = response.json()


# # 5.Getting the Most Upvoted Comment
# comments_list = comments[1]["data"]["children"]
# most_upvoted_comment = ""
# most_upvotes = 0
# for article in comments_list:
#     ar = article["data"]
#     if ar["ups"] >= most_upvotes:
#         most_upvoted_comment = ar["id"]
#         most_upvotes = ar["ups"]


# 6.Upvoting a Comment
