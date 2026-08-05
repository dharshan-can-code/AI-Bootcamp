positive = {
    "love": 2,
    "great": 2,
    "good": 1,
    "amazing": 3
}

negative = {
    "hate": -2,
    "bad": -1,
    "bugs": -1,
    "boring": -2
}

word = input("Enter your statement") 
words = word.split( )

score = 0

for word in words:
    score += positive.get(word, 0)
    score += negative.get(word, 0)

if score > 0:
    label = "Positive"
elif score < 0:
    label = "Negative"
else:
    label = "Neutral"

print("Score:", score)
print("Label:", label)