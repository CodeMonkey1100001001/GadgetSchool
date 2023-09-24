# from pprint import pprint
import PythonSmolGraphSVG
#import PythonSmolGraphFancyStuff

# vernier scale 1/10 inches

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

sg = PythonSmolGraphSVG.SmolGraph2SVG("mm")
#sgf = PythonSmolGraphFancyStuff.SmolGraphFancy("inch")

sg.setSize(300, 300, -150, 150, -150, 150)
# sg.setCenter(-10,-10)

theDoc = sg.svgHeader()
# drawGrid()


theDoc += "<g>\n"
insideRadius = 101.5 / 2
outsideRadius = 120.5 / 2
for i in range(0,360):

    markWidth = i / 10
    theHeight = 3
    # print("inchMark", inchMark, inchMark % 1)
    if markWidth % 0.5 == 0:
        theHeight = 4
    if markWidth % 1 == 0:
        theHeight = 5
        theDoc += sg.graphPolarText(str(int(i)),0,0, i, insideRadius + 5.5 ,  textAnchor="middle", size="6pt")
    theDoc += sg.graphDualPolarLine(0,0,insideRadius,i,insideRadius + theHeight,i,width=0.2)
# theDoc += sg.graphText("Decimal Inches",0,0.55,"6pt")
theDoc += "</g>\n"

theDoc += "<g>\n"
theDoc += sg.graphCircle(0,0,insideRadius, color="#ff0000")
theDoc += sg.graphCircle(0,0,outsideRadius, color="#ff0000")
theDoc += sg.graphDisk(0,0,2, color="#ff0000")
theDoc += "</g>\n"

theDoc += "<g>\n"
insideRadius = 47
outsideRadius = 45
for i in range(10,171):
    theAngle = i - 90
    markWidth = i / 10
    theHeight = 3
    # print("inchMark", inchMark, inchMark % 1)
    # if markWidth % 0.5 == 0:
    #     theHeight = 4
    # if markWidth % 1 == 0:
    #     theHeight = 5
    #     # theDoc += sg.graphPolarText(str(int(i)),0,0, i, insideRadius + 7 ,  textAnchor="middle", size="6pt")
    # theHeight = theAngle / 3
    theDoc += sg.graphDualPolarLine(0,0,insideRadius,theAngle,insideRadius + 1.25 ,theAngle,width=0.2)

    if i % 5 == 0:
        theDoc += sg.graphDualPolarLine(0,0,insideRadius-7.33,theAngle,insideRadius ,theAngle,width=0.2)

    if i % 10 == 0:
        theDoc += sg.graphDualPolarLine(0,0,20,theAngle,insideRadius ,theAngle,width=0.2)

# theDoc += sg.graphText("Decimal Inches",0,0.55,"6pt")
theDoc += sg.graphArc(0,0,insideRadius,10-90, 170-90, width=0.2)
theDoc += sg.graphArc(0,0,insideRadius + 1.25,10-90, 170-90, width=0.2)
theDoc += sg.graphArc(0,0,insideRadius -7.33 ,10-90, 170-90, width=0.2)

theDoc += "</g>\n"

theYPos = 31
theDoc += sg.graphDisk(0,theYPos,35/2, color="#ffffff")
for i in range(0,360,12):
    theDoc += sg.graphDualPolarLine(0,theYPos,10,i,35/2 ,i,width=0.1)
theDoc += sg.graphCircle(0,theYPos,35/2, color="#000000" , width=0.1)








# theDoc += sg.graphArc(0, 0, 7, 45, 45 + 90, 0.2, "#FF00FF")
# theDoc += sg.graphRectangle(-4, -4, -3, -3, 0.1, "#770737")
# theDoc += sg.graphRectangleFilled(-4, -5, -3, -4, "#F33A6A", 0.1, "#0000cc")
# theDoc += sg.graphCircle(-5, 5, 1.0, 0.2, "#0000ff")
# theDoc += sg.graphDisk(-5, 3, 1.0, "#00ccff")
# theDoc += sg.graphDiskText(-5, 1, 1.0, "disk text", "#0000cc")  # graph a disc but with hover help
# theDoc += sg.graphText("PlainText", 4, -5, "24pt", "#cc0000")
# theDoc += sg.graphTextRotate("Rotated66", 4, -5, "12pt", 66, "#cc00cc")
# theDoc += sg.graphDualPolarLine(0, 0, 2.5, 66, 3.0, 67, 0.1, "#ff4444")
# theDoc += sg.graphPolarLine(0, 0, 9.5, 12, 0.1, "#cc4433")
# # theDoc += sg.drawArc(4,-4,2,45,45+90,0.1,"#fafa00")
# theDoc += sg.graphArc(4.5, -4.5, 2, 45, 45 + 90, 0.1, "#fafa00")
# theDoc += sg.graphLine(-5, -9, 5, -9)  # test using defaults for width and color

# test font-family change
# sg.fontFamily = "sans"
# theDoc += sg.graphText("PlainSansText", 4.5, -6, "24pt", "#cc0000")

theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# print(theDoc)

print(sg.getSizeHuman())
