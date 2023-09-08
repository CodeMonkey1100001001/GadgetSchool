# ver 20230831.1000
import PythonSmolGraphSVG
import PythonSmolGraphFancyStuff

# import math

personHeight = 5


# for alpha in range(1,181):
#     halfAlpha = alpha / 2
#     b = personHeight / math.tan(halfAlpha * (3.14159265359 / 180))
#     print(halfAlpha, personHeight, b)

def drawGrid():
    global theDoc
    xStart = sg.minValueX
    yStart = sg.minValueY
    xEnd = sg.maxValueX
    yEnd = sg.maxValueY
    # xCenter = xEnd - xStart
    for gridX in range(xStart, int(xEnd) + 1, 1):
        theDoc += sg.graphLine(gridX, sg.minValueY, gridX, sg.maxValueY, 0.03, "#5f9b9c")

    for gridY in range(yStart, int(yEnd) + 1, 1):
        theDoc += sg.graphLine(sg.minValueX, gridY, sg.maxValueX, gridY, 0.03, "#5f9b9c")

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("inch")
sgf = PythonSmolGraphFancyStuff.SmolGraphFancy("inch")

sg.setSize(16, 16, -8, 8, -8, 8)
theDoc = sg.svgHeader()
# drawGrid()

# theDoc += sg.graphLine(0,0,1,1,0.1,"#ff0000")
# theDoc += sg.graphLine(0,0,1,-1,0.1,"#00ff00")
# theDoc += sg.graphLine(0,0,2,2,0.05,"#ff0000")
# theDoc += sg.graphLine(0,0,2,-2,0.05,"#00ff00")

smallLine = 0.003
mediumLine = 0.006
largeLine = 0.012

# How wide and tall to make the Grid
fancyVersion: bool = True
howWide = 7.0  # 7.0 in
for x in range(0, 151, 1):  # divide by 10 to get 1/10
    plotX = sg.map(x, 0, 150, 0.00, howWide)  # + 0.25
    lineWidth = smallLine
    xMod = (x % 10)
    # print("xMod", xMod)
    if x % 10 == 0:
        lineWidth = mediumLine
        theDoc += sg.graphText(str(int(x / 10)), plotX + 0.06, 0.35 - 0.50, "12pt", "#111111")
    # if x == 50 or x == 100:
    #     lineWidth = 0.018
    markingRadius = howWide
    v = howWide
    if fancyVersion:
        theReturn = sgf.circle_line_segment_intersection([0, 0], markingRadius, [plotX, 0], [plotX, markingRadius],
                                                         full_line=False)
        print(theReturn, theReturn)
        if len(theReturn) > 0:
            (h, v) = theReturn[0]

    # theDoc += sg.graphLine(plotX, 0.0, plotX, howWide, lineWidth, "#000000")  # normal version
    theDoc += sg.graphLine(plotX, 0.0, plotX, v, lineWidth, "#000000")  # fancy version

for y in range(0, 151, 1):  # divide by 10 to get 1/10
    plotY = sg.map(y, 0, 150, 0.00, howWide)  # + 0.25
    lineWidth = smallLine
    if y % 10 == 0:
        lineWidth = mediumLine
        theDoc += sg.graphText(str(int(y / 10)), -(1 / 16), plotY , "12pt", "#000000",textAnchor="end")
    markingRadius = howWide
    h = howWide
    if fancyVersion:
        theReturn = sgf.circle_line_segment_intersection([0, 0], markingRadius, [0, plotY], [markingRadius, plotY],
                                                         full_line=False)
        print(theReturn, theReturn)
        if len(theReturn) > 0:
            (h, v) = theReturn[0]
    # theDoc += sg.graphLine(0.0, plotY, howWide, plotY, lineWidth, "#000000") # normal version
    theDoc += sg.graphLine(0.0, plotY, h, plotY, lineWidth, "#000000")  # fancy version

# compass Circle start = 7.0
compassCircleStart = 7.0

# the Mask only use for non fancy version
if fancyVersion:
    theDoc += sg.graphArc(0, 0, compassCircleStart + (1 / 2), 0, 90, width=1.0, color="#ffffff")  # mask

# compass circle lines
# The innermost line
theDoc += sg.graphArc(0, 0, compassCircleStart, 0, 90, width=0.01, color="#000000")
# The alpha line
theDoc += sg.graphArc(0, 0, compassCircleStart + (2 / 8), 0, 90, 0.01, "#000000")
# The beta Line
theDoc += sg.graphArc(0, 0, compassCircleStart + (4 / 8), 0, 90, 0.01, "#000000")
# The final Tic Lines
theDoc += sg.graphArc(0, 0, compassCircleStart + (6 / 8), 0, 90, 0.01, "#000000")

# labels for text on compass circle
# we want to plot from outside to inside for the lines
compassCircleEnd = compassCircleStart + (6 / 8)
for theAngle in range(0, 90):  # 90 * 2 for extra tic lines 90 * 10 for a whole bunch
    # theAngle = theAngle / 2.0
    lineWidth = 0.0033
    lineLen = (1 / 8)

    if theAngle % 1 == 0:
        lineLen = (2 / 8)

    if theAngle % 5 == 0:
        lineLen = (4 / 8)
        lineWidth = 0.010
    if theAngle % 10 == 0:
        lineLen = (6 / 8)
        lineWidth = 0.015
        displayAngle = 90 - theAngle
        theDoc += sg.graphPolarText(textValue=str(int(displayAngle)),
                                    x=0, y=0, degrees=theAngle + 0.25,
                                    radius=compassCircleStart + (1 / 16),
                                    size="10pt", color="#000000")
        theDoc += sg.graphPolarText(textValue=str(int(theAngle)),
                                    x=0, y=0, degrees=theAngle + 0.25 - 2.0,
                                    radius=compassCircleStart + (5 / 16),
                                    size="10pt", color="#000000")
    theDoc += sg.graphDualPolarLine(0, 0,
                                    compassCircleEnd - lineLen, theAngle,
                                    compassCircleEnd, theAngle,
                                    lineWidth, "#000000")

# where is 10
if True:
    plotX = sg.map(100.0, 0, 150, 0.0, howWide)
    plotY = sg.map(100.0, 0, 150, 0.0, howWide)
    # theDoc += sg.graphCircle(plotX, plotY, 0.006, 0.116, "#00ff00")
    theDoc += sg.graphDisk(plotX, plotY, 0.05, "#000000")

# The shuttle
theDoc += "<g>\n"
# the tick marks
for i in range(0, 150):
    # polarScale = 3.0
    # theX = sg.map(theX, 0, 10, 0.0, polarScale)
    # theY = sg.map(theY, 0, 10, 0.0, polarScale)

    # theX2, theY2 = sg.polarToCartesianFlip(0,0,i,40)
    # theX2 = sg.map(theX2, 0, 10, 0.0, polarScale)
    # theY2 = sg.map(theY2, 0, 10, 0.0, polarScale)
    theX = sg.map(i, 0, 150, 0, howWide)
    lineHeight = 0.1
    if i % 5 == 0:
        lineHeight = 0.15
    if i % 10 == 0:
        lineHeight = 0.2
        theDoc += sg.graphText(str(int(i / 10)), theX , -1.20, "8pt", "#000000",textAnchor="start")
    theDoc += sg.graphLine(theX, -1, theX, -1 - lineHeight, 0.006, "#000000")

theDoc += "</g>\n"

# the center point
theDoc += sg.graphDisk(0, 0, 0.05, "#ff1111")

# alpha and beta
theDoc += sg.graphPolarText("α", 0, 0, -1.25, howWide + (1 / 16), "15pt", "#000000")
theDoc += sg.graphPolarText("α", 0, 0, 90.55, howWide + (1 / 16), "15pt", "#000000")
theDoc += sg.graphPolarText("β", 0, 0, -1.25, howWide + (5 / 16), "15pt", "#000000")
theDoc += sg.graphPolarText("β", 0, 0, 90.55, howWide + (5 / 16), "15pt", "#000000")

# the shuttle
theDoc += "<g>\n"
# body design
theWidth = sg.map(170, 0, 150, 0, howWide)
theDoc += sg.graphRectangle(0, -1, theWidth, -1.25, 0.01, "#ff0000")
# theDoc += sg.graphLine(0,-1,theWidth,-1,0.01,"#ff0000")
# theDoc += sg.graphLine(theWidth,-1,theWidth, -1.2, 0.01,"#ff0000")
theDoc += sg.graphDisk(0, -1, 0.125, "#ffaaaa")
theDoc += sg.graphDisk(0, -1, 0.05, "#ff1111")
theDoc += "</g>\n"

# final line
theDoc += sg.graphLine(0, -1, theWidth, -1, 0.012, "#000000")
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

subDivisions = 360 / 16
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

theDoc += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# print(theDoc)
print(sg.getSizeHuman())
