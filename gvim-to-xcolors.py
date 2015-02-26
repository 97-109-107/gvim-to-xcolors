#!/usr/bin/python
import re
import os
import json
import pprint
import colorsys
import sys
import kmeans

full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)
pp = pprint.PrettyPrinter(indent=4)
hexRegex = re.compile(r'gui(..)\=(#[a-fA-F\d]{6})')
highlightRegex = re.compile("^hi.(\w+)")

guifgRegex = re.compile(r'guifg\=(\S*)\s')
guibgRegex = re.compile(r'guibg\=(\S*)\s')
groupRegex = re.compile(r'hi\s(\w*)\s')

vimColorsFile = open(path+"/vimColors.json")
vimColors = json.load(vimColorsFile)

vimGroups = ['Normal', 'Visual', 'VertSplit', 'Identifier', 'Statement', 'PreProc', 'Type', 'Function', 'String', 'Conditional', 'Repeat', 'Label', 'Operator', 'Keyword', 'Exception', 'Character', 'Number', 'Boolean', 'Float', 'Comment', 'Special', 'Error', 'Todo']

outputXcolors = [] 
outputHtml = False;

def filterbyvalue(seq, value):
    value = value.lower()
    for el in seq:
        if el['group']==value: return el

def getHsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    # return only hsV to sort by Value
    return colorsys.rgb_to_hsv(r, g, b)[2]

def main():
    colorscheme = sys.argv[1]
    colorschemeHexes = list()
    colorschemeHighlights = list()
    colorschemeAside = list()
    normalFg = ''
    normalBg = ''
    humanProcessing = []
    colorschemeRgbs = []

    with open(colorscheme) as colorschemeFile:
        for line in colorschemeFile:
            if line.startswith('hi '):
                guifg = guifgRegex.findall(line)
                guibg = guibgRegex.findall(line)
                group = groupRegex.findall(line)

                if(guifg and guibg and group):
                    toInsert = {
                            "group": group[0].strip().lower(),
                            "fg":guifg[0].strip().lower(),
                            "bg":guibg[0].strip().lower()
                            }
                    if(toInsert["group"] == 'normal'):
                        normalFg = toInsert['fg'];
                        normalBg = toInsert['bg'];
                    humanProcessing.append(toInsert)



    # replace color names in our list with hex values, first fg then bgs
    for (i,token) in enumerate(['fg','bg']):
        for (j, entry) in enumerate(humanProcessing):
            vimColorName = entry[token]
            if(entry[token].find('bg') == 0):
                humanProcessing[j][token] = normalBg 
            if(entry[token].find('fg') == 0):
                humanProcessing[j][token] = normalFg 
            if(entry[token].find('none') == 0):
                if(token == 'fg'):
                    humanProcessing[j][token] = normalFg
                else:
                    humanProcessing[j][token] = normalBg
            if(entry[token].find('#') == -1):
                for o in vimColors:
                    if o['name'] == entry[token]:
                        humanProcessing[j][token] = o['hex']

    # look for the group we're after and compile a list
    for group in vimGroups:
        match = filterbyvalue(humanProcessing, group)
        if(match):
            outputXcolors.append(match)

    produceXColors(outputXcolors)


def produceXColors(c):
    out = []
    prefix = "*."
    count = 0

    for o in c:
        if o['group'] == 'normal':
            out.append("".join([prefix,"foreground: "+o["fg"]]))
            out.append("".join([prefix,"background: "+o["bg"]]))
            out.append("".join([prefix,"cursorColor: "+o["fg"]]))
        else:
            out.append("".join([prefix,"color"+str(count)+": "+o["fg"]]))
            count+=1
            if count == 15:
                break

    out = "\n".join(out)
    print(out)


def wrapJson(d):
    with open('output.json', 'w') as outfile:
        json.dump(d, outfile, indent=4, sort_keys=True)

def printout(colorscheme,colorschemeHexes):
    html = "<html><title>{0} colorscheme</title><body>".format(colorscheme)
    html += "<table><tr>"
    text = ""

    for (j, color) in enumerate(colorschemeHexes):
        if (j % 5 == 0):
            html += '</tr><tr>'
        textColor = getTextColor(color)
        html += ('<td style="width:100px;height:100px;background-color:{0};'
                 'color:{1};text-align:center;">'.format(color, textColor))
        html += color
        html += "</td>"
        text += color+"\n"

    html += "</tr></table>"
    html += "</body></html>"

    with open('./output.html', 'w') as outFile:
        outFile.write(html)

    with open('./output.txt', 'w') as outFile:
        outFile.write(text)

def usage():
    print("A single argument is required: python2 gvim-to-xcolors.py file")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        usage()
