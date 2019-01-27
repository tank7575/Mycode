import bible

def most_common_words(freqs):
    values = freq.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs(k)  == best:
          words.append(k)
    return (words, best)

print(most_common_words(bible))
