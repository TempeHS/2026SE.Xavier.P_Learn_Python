def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return face

def main():
    text = convert(input("Input: "))
    print(text)

main()
