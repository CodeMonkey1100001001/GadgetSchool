# from pprint import pprint

import PythonSmolGraphSVG  # use current version that is included here
#import PythonSmolGraphFancyStuff
# import math

def drawGrid():
    global theDoc
    dgx = sg.minValueX
    # print("x minValueX", x, sg.minValueX)
    # print("sg.minValueY", sg.minValueY, sg.maxValueY)
    while dgx < sg.maxValueX:
        # print("dgx",dgx)
        theDoc += sg.graphLine(dgx, sg.minValueY, dgx, sg.maxValueY, 0.025, "#5f9b9c")
        dgx = dgx + 1.0

    dgy = sg.minValueY
    while dgy < sg.maxValueY:
        theDoc += sg.graphLine(sg.minValueX, dgy, sg.maxValueX, dgy, 0.025, "#5f9b9c")
        dgy = dgy + 1.0

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("cm")

sg.setSize(20, 20, -10, 10, -10, 10)
# sg.setCenter(-10,-10)

theDoc = sg.svgHeader()
drawGrid()
theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# print(theDoc)

print(sg.getSizeHuman())
