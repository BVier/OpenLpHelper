from merge_utils import *

sep = "<br/>"
tag = '<tag name="tr">'
closing = "</tag>"

xml_headers = {"Vers": "v", "Pre-Chorus": "p", "Chorus": "c",
              "Bridge": "b", "Intro": "i", "Schluss": "e", "": "o"}

def merge_xml(original, translation):
  """
  MERGE
  """
  primaryLines, secondaryLines = readFiles(original, translation)
  is_translation = original!=translation
  for line in primaryLines:
    line = line.replace("&", "&amp;")
    line = line.replace("'", "&apos;")
    line = line.replace("<", "&lt;")
    line = line.replace(">", "&gt;")
    line = line.replace('"', "&quot;")

  # Assert title is only in first row
  title = []
  title.append(primaryLines[0])
  title.append(secondaryLines[0])

  lied, info = getSong(tag, closing, xml_headers, is_translation)

  authors = getAuthors(info+1)

  # Ignore if secondary is different
  copyright = primaryLines[info+2]
  ccli = primaryLines[info+4].replace("CCLI-Lizenznummer ", "")
  if "CCLI-Lizenznummer " not in primaryLines[info+4]:
    ccli = primaryLines[info+5].replace("CCLI-Lizenznummer ", "")

  """
  CREATE FILE
  """
  lines = []
  lines.append("<?xml version='1.0' encoding='UTF-8'?>")
  lines.append(
      '<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.8">')

  lines.append("  <properties>")
  lines.append("    <titles>")
  lines.append("      <title>" + title[0] + "</title>")
  if is_translation:
    lines.append("      <title>" + title[1] + "</title>")
  lines.append("    </titles>")
  lines.append("    <copyright>" + copyright + "</copyright>")
  lines.append("    <ccliNo>" + ccli + "</ccliNo>")
  lines.append("    <authors>")
  for author in authors:
      lines.append("      <author>" + author + "</author>")
  lines.append("    </authors>")
  lines.append("  </properties>")

  # Ensure the tag gets formatted
  if is_translation:
    lines.append("""  <format>
    <tags application="OpenLP">
      <tag name="tr">
        <open>&lt;em style="font-size:70px; -webkit-text-fill-color:#ffff99 "&gt;</open>
        <close>&lt;/em&gt;</close>
      </tag>
    </tags>
  </format>""")

  lines.append("  <lyrics>")
  for verse in lied:
      lines.append('    <verse name="' + verse + '">')
      lines.append('      <lines>' + sep.join(lied[verse]) + '</lines>')
      lines.append('    </verse>')
  lines.append("  </lyrics>")

  lines.append("</song>")

  output = open_file("liedtexte/" + title[0] + ".xml", "w+")
  output.writelines("\n".join(lines))
  output.close()
