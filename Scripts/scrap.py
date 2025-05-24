import re
import pandas as pd


# html = '''Easy<a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/if-else/if-else-statements/" target="_blank" rel="noreferrer">If Else statements<a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/if-else/if-else-statements/" target="_blank" rel="noreferrer" class="flex justify-center items-center text-zinc-700 dark:text-zinc-300"><a href="https://web.archive.org/web/20240510213845mp_/https://practice.geeksforgeeks.org/problems/java-if-else-decision-making0924/0?category%5B%5D=Java&amp;category%5B%5D=Java&amp;difficulty%5B%5D=-2&amp;page=1&amp;query=category%5B%5DJavadifficulty%5B%5D-2page1category%5B%5DJava" target="_blank" rel="noreferrer">'''


def extract_link_and_text(html):

    # Extract all href links
    links = []
    start = 0
    while True:
        href_index = html.find('href="', start)
        if href_index == -1:
            break
        start_quote = href_index + len('href="')
        end_quote = html.find('"', start_quote)
        link = html[start_quote:end_quote]
        links.append(link)
        start = end_quote + 1

    text_content = []
    start = 0
    while True:
        gt_index = html.find(">", start)
        lt_index = html.find("<", gt_index)
        if gt_index == -1 or lt_index == -1:
            break
        content = html[gt_index + 1 : lt_index].strip()
        if content:
            text_content.append(content)
        start = lt_index + 1

    if links:
        archive_prefix = "https://web.archive.org/web/20240510213845mp_/"
        last_link = links[-1]
        if last_link.startswith(archive_prefix):
            # Strip everything after prefix up to the first underscore or slash
            clean_start = last_link.find("_/") + 2
            links[-1] = last_link[clean_start:] if clean_start > 1 else last_link

    if text_content and links and not re.match(r'^[^a-zA-Z0-9]', text_content[0]):
        return text_content[0], links[-1]
    else:
        return None


with open("WAYBACK_STRIVER.html", "r") as file:
    text = file.read()

    result = []
    start = 0
    while start < (len(text)):
        if text[start] == "<" and text[start + 1] != "a":
            while text[start] != ">":
                start += 1

        else:
            result.append(text[start])
        start += 1

    formatted_text = "".join(result)
    # print(formatted_text)

    # Processing for <a target="_blank" rel="noreferrer">

    # <a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/" target="_blank" rel="noreferrer">3-Sum Problem<a href="https://web.archive.org/web/20240510213845mp_/https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/" target="_blank" rel="noreferrer" class="flex justify-center items-center text-zinc-700 dark:text-zinc-300"><a href="https://web.archive.org/web/20240510213845mp_/https://leetcode.com/problems/3sum/" target="_blank" rel="noreferrer">Save NotesCloseSaveMedium
    # formatted_text = re.split(r"[Save]",formatted_text)
    formatted_text = formatted_text.split("Save NotesCloseSave")
    # print("Length of the text is :",len(formatted_text))

    df = pd.DataFrame(columns=["Problem", "Link"])

    for i in formatted_text:
        result = extract_link_and_text(i)
        if result:
            df.loc[len(df)] = result

    df.to_csv("Scrapped_Links.csv")
