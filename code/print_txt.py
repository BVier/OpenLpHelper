from merge_utils import *

sep = "\n"
tag = "{tr}"
closing = "{/tr}"

txt_headers = {"Vers": "Vers ", "Pre-Chorus": "Pre-Chorus ", "Chorus": "Chorus ",
              "Bridge": "Bridge ", "Intro": "Intro ", "Schluss": "Schluss ", "": "Anderes "}

def merge_txt(original, translation):
    """
    MERGE
    """
    primaryLines, secondaryLines = readFiles(original, translation)

    lied, meta = getSong(tag, closing, txt_headers, original != translation)

    authors = getAuthors(meta+1)

    """
    CREATE FILE
    """
    lines = []
    lines.append(primaryLines[0])
    lines.append("")
    for verse in lied:
        lines.append(verse)
        lines.append(sep.join(lied[verse]))
        lines.append("")

    lines.append(primaryLines[meta])
    lines.append(" | ".join(authors))
    for row in primaryLines[meta+2:]:
        lines.append(row)

    output = open_file("txt/" + primaryLines[0] + ".txt", "w+")
    output.writelines("\n".join(lines))
    output.close()
