#A dictionary stores data in key:value pairs.

#"happy" is the key.
#"😊" is the value.
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "fire": "🔥",
    "cool": "😎"
}

#lower() converts everything to lowercase:
sentence = input("Enter a sentence: ").lower()

#Loop Through Dictionary
#this loop goes through every key-value pair:
#word = "happy", emoji = "😊" etc etc
#.items() allows us to access both the key and value of a dictionary at the same time.

for word, emoji in emoji_dict.items():
    sentence = sentence.replace(word, emoji)

print("Converted:")
print(sentence)
