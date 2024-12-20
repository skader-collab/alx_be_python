# Get user input for weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Use if-elif-else for decision making based on weather
if weather.lower() == "sunny":
  recommendation = "Wear a t-shirt and sunglasses."
elif weather.lower() == "rainy":
  recommendation = "Don't forget your umbrella and a raincoat."
elif weather.lower() == "cold":
  recommendation = "Make sure to wear a warm coat and a scarf."
else:
  recommendation = "Sorry, I don't have recommendations for this weather."
