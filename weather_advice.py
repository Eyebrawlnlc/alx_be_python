weather = input("What's the weather like today? (sunny/rainy/cold):")

while weather == "sunny":
    print("Wear a t-shirt and sunglasses")
    weather = input("What's the weather like today? (sunny/rainy/cold):")

while weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
    weather = input("What's the weather like today? (sunny/rainy/cold):")

while weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
    weather = input("What's the weather like today? (sunny/rainy/cold):")
else: 
    print("Sorry, I don't have recommendations for this weather.")

