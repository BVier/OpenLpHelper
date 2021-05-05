import os.path

primaryLines = []
secondaryLines = []


def open_file(filename, access):
    return open(os.path.join(os.path.dirname(__file__), os.pardir, filename), access)


def linesFromFile(filename):
    file = open_file(filename, "r")
    lines = []
    for line in file.readlines():
        lines.append(line.replace("\n", ""))
    file.close()
    return lines


def readFiles(original, translation):
    global primaryLines, secondaryLines
    primaryLines = linesFromFile(original)
    secondaryLines = linesFromFile(translation)
    assert(len(primaryLines) == len(secondaryLines))
    return primaryLines, secondaryLines


def write_to_file(lines, filename):
    output = open_file(filename, "w+")
    output.writelines("\n".join(lines))
    output.close()


def getSong(tag, closing, headers, twoSongs=True):
    counter = {"Vers": 1, "Chorus": 1, "Bridge": 1,
               "Pre-Chorus": 1, "Intro": 1, "Schluss": 1, "": 1}
    song = {}
    verse = ""
    expectHeader = True
    end_index = 0
    for row in range(1, len(primaryLines)):
        if "CCLI" in primaryLines[row]:
            end_index = row
            break
        elif primaryLines[row].replace(" ", "") == "":
            assert(primaryLines[row] == secondaryLines[row].replace(" ", ""))
            expectHeader = True
        elif expectHeader:
            verse = newVerse(row, headers, counter, song, verse)
            expectHeader = False
        else:
            song[verse].append(primaryLines[row])
            if twoSongs:
                song[verse].append(tag + secondaryLines[row] + closing)
    return song, end_index


def newVerse(row, headers, counter, song, verse):
    assert(len(primaryLines[row].split(" ")) < 3,
           "Expected new verse but line was: " + str(primaryLines[row]))
    for header in headers:
        if header in primaryLines[row]:
            try:
                assert(primaryLines[row] == secondaryLines[row])
                index = counter[header]
                counter[header] += 1
                verse = headers[header] + str(index)
                song[verse] = []
            finally:
                break
    return verse


def getAuthors(row):
    authors = primaryLines[row].split(" | ")
    authors = authors + secondaryLines[row].split(" | ")
    return list(dict.fromkeys(authors))
