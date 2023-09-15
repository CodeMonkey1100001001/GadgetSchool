# from pprint import pprint
import math

import PythonSmolGraphSVG  # use current version that is included here


# import PythonSmolGraphFancyStuff
# import math


def drawGrid():
    global theDoc
    #theDoc += f'<g inkscape:groupmode="layer"\nid="layer1"\ninkscape:label="Grid">\n'
    theDoc += f'<g>\n'
    dgx =  int(sg.minValueX / 10 ) * 10
    # print("x minValueX", x, sg.minValueX)
    # print("sg.minValueY", sg.minValueY, sg.maxValueY)
    while dgx < sg.maxValueX:
        # print("dgx",dgx)
        theDoc += sg.graphLine(dgx, sg.minValueY, dgx, sg.maxValueY, 0.07, "#5f9b9c")
        theDoc += sg.graphText(str(int(dgx)), dgx, sg.minValueY + 10, size="4pt", color="#444444")
        dgx = dgx + 10.0

    dgy = int( sg.minValueY / 10 ) * 10
    while dgy < sg.maxValueY:
        theDoc += sg.graphLine(sg.minValueX, dgy, sg.maxValueX, dgy, 0.07, "#5f9b9c")
        theDoc += sg.graphText(str(int(dgy)), sg.minValueX + 10 , dgy, size="4pt", color="#444444")
        dgy = dgy + 10.0

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")
    theDoc += "</g>\n"


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("mm")

# 8.5" x 11" sheet of paper
baseSizeX = 215.9
baseSizeY = 279.4

sg.setSize(baseSizeX , baseSizeY, baseSizeX / 2 * -1.0 , baseSizeX / 2, baseSizeY / 2 * -1.0 , baseSizeY/2)
# sg.setCenter(baseSizeX / 2, baseSizeY / 2)
theDoc = sg.svgHeader()
# #########################
drawGrid()

innerDiameter = 56.6
outerDiameter = 84.0

theDoc += sg.graphCircle(0,0,innerDiameter / 2, width=0.7, color="#000000")
theDoc += sg.graphCircle(0,0,outerDiameter / 2, width=0.7, color="#000000")
theDoc += sg.graphCircle(0,0,10, width=0.7, color="#ff0000")


# ######################

theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# print(theDoc)

print(sg.getSizeHuman())
