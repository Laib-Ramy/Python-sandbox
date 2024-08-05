import os

with open(r"your path","r") as file:
    text = file.read()

# Traitement du texte
words = text.lower().split()
words = [word.strip(".,?!") for word in words]

# Comptage des mots
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Tri des mots par fréquence
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Affichage des résultats
i=0
for word, count in sorted_words:
    print(f"{word}: {count}")
    i+=1
    if i==15:
        break
  
