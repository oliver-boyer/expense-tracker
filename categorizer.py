def categorize(name):
 categories = {
    "food":["mcdonald's", "wendy's" , "burger king", "restaurant", "food"],
    "transport":["uber","bus","taxi","metro","gas" ],
    "entertainment":["netflix","cinema","apple music","game", "arcade" ],
    "shopping":["amazon", "zara", "mall", "store"]

  }
 for category, keywords in categories.items():
   for keyword in keywords:
    if keyword in name.lower():
     return category

 return "other"


