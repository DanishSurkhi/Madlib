with open("story.txt", "r") as f:
    story=f.read()
words=set()
start_index=-1
start_word="<"
end_word=">"

for i,char in enumerate(story):
    if char==start_word:
        start_index=i
    if char==end_word and start_index!=-1:
        word=story[start_index:i+1]
        words.add(word)
        start_index=-1

answers={}

for word in words:
    answer=input("give word for "+word+" : ")
    answers[word]=answer
for word in words:
    story=story.replace(word,answers[word])
print(story)






