# from pprint import pprint
import math

import PythonSmolGraphSVG  # use current version that is included here


# import PythonSmolGraphFancyStuff
# import math


def drawGrid():
    global theDoc
    theDoc += "<g>\n"
    dgx = sg.minValueX
    # print("x minValueX", x, sg.minValueX)
    # print("sg.minValueY", sg.minValueY, sg.maxValueY)
    while dgx < sg.maxValueX:
        # print("dgx",dgx)
        theDoc += sg.graphLine(dgx, sg.minValueY, dgx, sg.maxValueY, 0.07, "#5f9b9c")
        dgx = dgx + 10.0

    dgy = sg.minValueY
    while dgy < sg.maxValueY:
        theDoc += sg.graphLine(sg.minValueX, dgy, sg.maxValueX, dgy, 0.07, "#5f9b9c")
        dgy = dgy + 10.0

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")
    theDoc += "</g>\n"


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("mm")

baseSize = 280

sg.setSize(baseSize * 2, baseSize * 2, -baseSize, baseSize, -baseSize, baseSize)
# sg.setCenter(-10,-10)
theDoc = sg.svgHeader()
# #########################
drawGrid()

theDoc += "<g>\n"

cylinderRadius = 25  # mm
stripWidth = 2 * math.pi * cylinderRadius
print('stripWidth / circumfrence', stripWidth)
stripHeight = 20  # mm
spokeCount = 12

theDoc += sg.graphRectangle(0, 0, stripWidth, stripHeight, color="#ff0000")

for i in range(0, 361, int(360/12)):
    theX = sg.map(i, 0, 360, 0, stripWidth)
    theY = stripHeight
    theDoc += sg.graphCircle(theX, theY , 3.0/2, color="#ff0000")
for i in range(0, 361):
    theY = 0
    theX = sg.map(i, 0, 360, 0, stripWidth, )
    tickHeight = 3.0  # mm
    if i % 5 == 0:
        tickHeight = 5
    if i % 10 == 0:
        tickHeight = 7
        theDoc += sg.graphText(str(i),theX,theY + 8, size="4pt", textAnchor="middle")
    theDoc += sg.graphLine(theX,theY, theX, theY + tickHeight)


# ######################
theDoc += "</g>\n"

theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# print(theDoc)

print(sg.getSizeHuman())
