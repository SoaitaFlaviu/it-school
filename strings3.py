loren = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

words = loren.split(' ')

words2 = []

for word in words:
    words2.append(word.lower())

len(words)

print(len(words))

histogram = {}

for word in words2:
    histogram[word] = loren.count(word)

print(histogram)

for k, v in histogram.items():
    print(k, " - ", v)

