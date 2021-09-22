phrases_pentakill = [
    "So go and set your spirit free",
    "Let the lifeless clear the way",
    "For we have come to save you from your pain",
    "So let your voices scream",
    "Powerless lifelines freed from time",
    "Because we exist to survive the changing tide"
]

for phrase in phrases_pentakill:
    message = ""
    maior_len = ""
    i = 0
    a = phrase.split(" ")

    while i < len(a):
        message += str(len(a[i])) + "-"
        if len(a[i]) > len(maior_len):
            maior_len = a[i]

        i += 1

    message = message[-len(message):-1]
    print("{:25s} {}".format(message, maior_len))