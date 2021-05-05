from merge_utils import *

tag = "{tr}"
closing = "{/tr}"

before = "---["
after = "]---"

copy_headers = {"Vers": "Strophe:", "Pre-Chorus": "Überleitung:", "Chorus": "Refrain:",
                "Bridge": "Bridge:", "Intro": "Intro:", "Schluss": "Ende:", "": "Anderes:"}


def merge_copyAndPaste(original, translation):
    primaryLines, secondaryLines = readFiles(original, translation)

    song, end_row = getSong(tag, closing, copy_headers,
                            original != translation)
    authors = getAuthors(end_row+1)

    lines = [primaryLines[0], secondaryLines[0], ""]
    for vers in song:
        lines.append(before + vers + after)
        lines.append("\n".join(song[vers]))
        lines.append("")

    lines.append(primaryLines[end_row])
    lines.append(" | ".join(authors))
    for row in primaryLines[end_row+2:]:
        lines.append(row)

    write_to_file(lines, "copyAndPaste/" + primaryLines[0] + ".txt")
