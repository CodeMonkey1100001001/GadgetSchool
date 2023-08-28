# ver 20230824.1619
import PythonSmolGraphSVG
import math

personHeight = 5
# for alpha in range(1,181):
#     halfAlpha = alpha / 2
#     b = personHeight / math.tan(halfAlpha * (3.14159265359 / 180))
#     print(halfAlpha, personHeight, b)



def drawGrid():
    global theDoc
    xStart = sg.minValueX
    xEnd = sg.maxValueX
    yEnd = sg.maxValueY
    #xCenter = xEnd - xStart
    for x in range(0, int(xEnd)+1, 1):
        theDoc += sg.graphLine(x, sg.minValueY, x, sg.maxValueY, 0.003, "#5f9b9c")

    for y in range(0, int(yEnd)+1, 1):
        theDoc += sg.graphLine(sg.minValueX, y, sg.maxValueX, y, 0.003, "#5f9b9c")

    # while x < sg.maxValueX:
    #     # print("x",x)
    #     theDoc += sg.graphLine(x, sg.minValueY, x, sg.maxValueY, 0.05, "#5f9b9c")
    #     x = x + 1.0
    #
    # y = sg.minValueY
    # while y < sg.maxValueY:
    #     theDoc += sg.graphLine(sg.minValueX, y, sg.maxValueX, y, 0.05, "#5f9b9c")
    #     y = y + 1.0

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("inch")

sg.setSize(physicalWidth=4.25*96*2, physicalHeight=6.0*96*2, minX=-4.25, maxX=4.25, minY=-6, maxY=6)
theDoc = sg.svgHeader()
# drawGrid()

# theDoc += sg.graphLine(0,0,1,1,0.1,"#ff0000")
# theDoc += sg.graphLine(0,0,1,-1,0.1,"#00ff00")
# theDoc += sg.graphLine(0,0,2,2,0.05,"#ff0000")
# theDoc += sg.graphLine(0,0,2,-2,0.05,"#00ff00")

# x = 0
# while x < 10.1: #
# the X grid
for x in range(0,151,2): # divide by 10 to get 1/10
    plotX = sg.map(x,0,100,0.00,2.25) # + 0.25
    lineWidth = 0.006
    xMod = (x % 10)
    # print("xMod", xMod)
    if xMod == 0:
        lineWidth = 0.012
        theDoc += sg.graphText(str(int(x/10)), plotX +0.06,  0.35 - 0.50 , "12pt", "#111111")
    if x == 50 or x == 100:
        lineWidth = 0.018
    theDoc += sg.graphLine(plotX, 0.0, plotX, 3.50, lineWidth, "#000000")

# the Y Grid
for y in range(0,151,2): # divide by 10 to get 1/10
    plotY = sg.map(y,0,100,0.00,2.25) # + 0.25
    lineWidth = 0.006
    yMod = (y % 10)
    # print("yMod", yMod)
    if yMod == 0:
        lineWidth = 0.012
        theDoc += sg.graphText(str(int(y/10)), 0.45 - 0.50 , plotY - 0.05, "12pt", "#111111")
    if y == 50 or y == 100:
        lineWidth = 0.018
    theDoc += sg.graphLine(0.0, plotY, 3.5, plotY, lineWidth, "#000000")

# the Mask
theDoc += sg.drawArc(0, 0, 3.86, 0, 90, "1.0", "#ffffff") #mask

# compass circle lines
theDoc += sg.drawArc(0, 0, 3.36, 0, 90, "0.01", "#000000")
theDoc += sg.drawArc(0, 0, 3.46, 0, 90, "0.01", "#000000")
theDoc += sg.drawArc(0, 0, 3.56, 0, 90, "0.01", "#000000")
theDoc += sg.drawArc(0, 0, 3.66, 0, 90, "0.01", "#000000")

# labels for text on compass circle
for theAngle in range(0,90):
    lineLen = 0.09
    if theAngle % 5 == 0:
        lineLen = 0.2
    if theAngle % 10 == 0:
        lineLen = 0.3
        displayAngle = 90 - theAngle
        theDoc += sg.graphPolarText(textValue=str(displayAngle), x=0, y=0, degrees= theAngle + 0.25, distance = 3.385, size="5pt", color="#000000")
        theDoc += sg.graphPolarText(textValue=str(theAngle), x=0, y=0, degrees= theAngle + 0.25 - 2.0, distance = 3.485, size="5pt", color="#000000")

    theDoc += sg.graphDualPolarLine(0, 0, 3.66 - lineLen, theAngle, 3.66 , theAngle, "0.1", "#000000" )

# where is 10
if True:
    plotX = sg.map(100.0, 0, 100, 0.0, 2.25)
    plotY = sg.map(100.0, 0, 100, 0.0, 2.25)
    # theDoc += sg.graphCircle(plotX, plotY, 0.006, 0.116, "#00ff00")
    theDoc += sg.graphDisk(plotX, plotY, 0.02, "#000000")

#the center point
theDoc += sg.graphDisk(0,0,0.05,"#ff1111")

# alpha and beta
theDoc += sg.graphPolarText("α",0,0,-1.25, 3.36, "8pt", "#000000")
theDoc += sg.graphPolarText("α",0,0,90.55, 3.36, "8pt", "#000000")
theDoc += sg.graphPolarText("β",0,0,-1.25, 3.46, "8pt", "#000000")
theDoc += sg.graphPolarText("β",0,0,90.55, 3.46, "8pt", "#000000")


# the shuttle
theDoc += "<g>\n"
#body design
theWidth = sg.map(170,0,100,0,2.25)
theDoc += sg.graphRectangle(0,-1,theWidth,-1.25, 0.01, "#ff0000")
#theDoc += sg.graphLine(0,-1,theWidth,-1,0.01,"#ff0000")
#theDoc += sg.graphLine(theWidth,-1,theWidth, -1.2, 0.01,"#ff0000")
theDoc += sg.graphDisk(0, -1, 0.125, "#ffaaaa")
theDoc += sg.graphDisk(0, -1, 0.05,"#ff1111")
theDoc += "</g>\n"

#final line
theDoc += sg.graphLine(0,-1,theWidth, -1, 0.012, "#000000")
# the tick marks
theDoc += "<g>\n"
for i in range(0,150):
    polarScale = 3.0
    #theX = sg.map(theX, 0, 10, 0.0, polarScale)
    #theY = sg.map(theY, 0, 10, 0.0, polarScale)

    #theX2, theY2 = sg.polarToCartesianFlip(0,0,i,40)
    #theX2 = sg.map(theX2, 0, 10, 0.0, polarScale)
    #theY2 = sg.map(theY2, 0, 10, 0.0, polarScale)
    theX = sg.map(i,0,100,0,2.25)
    lineHeight = 0.1
    if i % 5 == 0:
        lineHeight = 0.15
    if i % 10 == 0:
        lineHeight = 0.2
        theDoc += sg.graphText(str(int(i/10)),theX + 0.05, -1.20, "6pt", "#000000")
    theDoc += sg.graphLine(theX, -1, theX, -1 - lineHeight, 0.006, "#000000")

theDoc += "</g>\n"

# theDoc += sg.graphText("TEST", 1.0, 1.0, "12pt", "#ff2222")
# theDoc += sg.graphLine(0, 0, 2, 3.00, 0.003, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 3.25, 0.004, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 3.50, 0.005, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 3.75, 0.006, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 4.00, 0.007, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 4.25, 0.008, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 4.50, 0.009, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 4.75, 0.010, "#000000")
# theDoc += sg.graphLine(0, 0, 2, 5.00, 0.011, "#000000")

# cartX, cartY = sg.polarToCartesian(0,0,100,90)
# theDoc += sg.graphLine(0,0,1.0,1.0,0.1,"green")
# theDoc += sg.graphLine(0,0,1.0,0.0,0.1,"blue")
#
# cartX, cartY = sg.polarToCartesian(0,0,100,180)
# theDoc += sg.graphLine(0,0,cartX,cartY,2.0,"blue")

subDivisions = 360/16
minorRadius = 1
majorRadius = 2

subSteps = 7

degreesBetween = (360 / subDivisions) - 7

lineWidth = 0.5
lineColor = "black"

tickLarge = 4
tickMedium = 3
tickSmall = 2

markLineWidth = 0.15



if False:
    theX, theY = sg.polarToCartesianFlip(0,0,3,45)
    theDoc += sg.graphText("45deg",theX,theY,"#000000","24pt")

theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg","w")
fp.writelines(theDoc)
fp.close()

#print(theDoc)
print(sg.getSizeHuman())