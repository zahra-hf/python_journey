#Create a dictionary, write code that changes the price of banana to 1100 and removes apple altogether.

fruit_prices = {
    "apple": 1500,
    "banana": 1000,
    "orange": 1200
}
fruit_prices["banana"] = 1100
fruit_prices.pop("apple")
print(fruit_prices)