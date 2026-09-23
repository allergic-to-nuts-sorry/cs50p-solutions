def convert(text):
    if(":(" in text):
        text = text.replace(":(","🙁")
    if(":)" in text):
        text = text.replace(":)","🙂")
    return text

def main():
    text = input()
    print(convert(text))

main()

