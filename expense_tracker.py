import pandas as pd

data = {
    "expense": ["Amazon", "Swiggy", "Uber", "Flipkart"],
    "amount": [500, 300, 200, 1000]
}

df = pd.DataFrame(data)

def category(x):
    if "Amazon" in x or "Flipkart" in x:
        return "Shopping"
    elif "Swiggy" in x:
        return "Food"
    else:
        return "Transport"

df["category"] = df["expense"].apply(category)

print(df)
