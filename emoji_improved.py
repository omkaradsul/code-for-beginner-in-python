def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word)
    return output


message = input(">")
print(emoji_converter(message))
