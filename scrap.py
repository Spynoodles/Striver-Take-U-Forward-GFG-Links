
import re

with open('WAYBACK_STRIVER.html','r') as file:
    text = file.read()

    result = []
    start = 0
    while start <(len(text)):
        if text[start] == "<" and text[start+1]!= "a":
            while(text[start] != ">"):
                start +=1

        else:
            result.append(text[start])
        start+=1

    formatted_text =''.join(result)
    # print(formatted_text)

    #Processing for <a target="_blank" rel="noreferrer">

# <a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/" target="_blank" rel="noreferrer">3-Sum Problem<a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/" target="_blank" rel="noreferrer" class="flex justify-center items-center text-zinc-700 dark:text-zinc-300"><a href="https://web.archive.org/web/20240510213845mp_/https://leetcode.com/problems/3sum/" target="_blank" rel="noreferrer">Save NotesCloseSaveMedium
    formatted_text = re.split(r"[target=\"_blank\" rel=\"noreferrer\">]",formatted_text)
    print(len(formatted_text))

    for i in formatted_text:
        print(i)
