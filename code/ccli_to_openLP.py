from print_xml import merge_xml
from print_txt import merge_txt
from print_copyAndPaste import merge_copyAndPaste
from time import sleep
from traceback import print_exc

original = "en_original.txt"
translation = "en_translation.txt"
single = "de_lied.txt"

try:
    merge_xml(single, single)
    # merge_txt(single, single)
    # merge_copyAndPaste(single, single)

    merge_xml(original, translation)
    # merge_txt(original, translation)
    # merge_copyAndPaste(original, translation)
except:
    print_exc() 
    sleep(120)
    