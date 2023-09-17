# from pprint import pprint
import math

import PythonSmolGraphSVG  # use current version that is included here
import PythonSmolGraphFancyStuff

# give lower left as x,y and upper right as h,v
def drawCutAndPrint(x,y,h,v):
    retVPrint = ""
    retVCut =""
    retVCut += sg.graphRectangle(x,y,h,v, color="#ff0000", width=0.1)

    # LL
    retVPrint += sg.graphRectangle(x - 10, y - 10, x, y, color="#000000", width=.25)
    # LR
    retVPrint += sg.graphRectangle(h + 10, y - 10, h, y, color="#000000", width=.25)
    # UL
    retVPrint += sg.graphRectangle(x - 10, v + 10, x, v, color="#000000", width=.25)
    # UR
    retVPrint += sg.graphRectangle(h + 10, v + 10, h, v, color="#000000", width=.25)

    return retVPrint, retVCut


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
pysgfs = PythonSmolGraphFancyStuff.SmolGraphFancy("mm")

# 8.5" x 11" sheet of paper
baseSizeX = 279.4
baseSizeY = 215.9

sg.setSize(baseSizeX , baseSizeY, baseSizeX / 2 * -1.0 , baseSizeX / 2, baseSizeY / 2 * -1.0 , baseSizeY/2)
# sg.setCenter(baseSizeX / 2, baseSizeY / 2)
theDoc = sg.svgHeader()
theDocCut = "" # HERE Here sg.svgHeader()

# #########################
# drawGrid()

# -------------------------
# Bottom Cylinder Drawing
sg.setCenter(-130,-90)
cylinderRadius = 40  # mm
stripWidth = 2 * math.pi * cylinderRadius
stripWidth = stripWidth + 0.2  # compensate for the paper thickness
print('stripWidth / circumfrence', stripWidth)
stripHeight = 10  # mm
spokeCount = 12

# printCutXmin = -3
# printCutYmin = -3
# printCutXmax = stripWidth + 10
# printCutYmax = stripHeight + 50
#
theDocCut += "<g id='cut'>\n"
# the alignment cut
# theDoc += sg.graphRectangle(printCutXmin,printCutYmin,printCutXmax,printCutYmax, color="#ff0000",width=0.1)
theDocCut += sg.graphRectangle(0, 0, stripWidth +8, stripHeight - 0.9, color="#ff0000")  # strip cut
for i in range(0, 371, int(360/12)):
    theX = sg.map(i, 0, 360, 0, stripWidth)
    theY = 0  # stripHeight
    theDocCut += sg.graphCircle(theX, theY , 3.0/2, color="#ff0000")
theDocCut += "</g>\n"

theDoc += "<g id='print_bottom_cylinder'>\n"
# #LL
# theDoc += sg.graphRectangle(printCutXmin - 10, printCutYmin - 10, printCutXmin, printCutYmin, color="#000000", width=.25)
# #LR
# theDoc += sg.graphRectangle(printCutXmax + 10, printCutYmin - 10, printCutXmax, printCutYmin, color="#000000", width=.25)
# #UL
# theDoc += sg.graphRectangle(printCutXmin - 10, printCutYmax + 10, printCutXmin, printCutYmax, color="#000000", width=.25)
# #UR
# theDoc += sg.graphRectangle(printCutXmax + 10, printCutYmax +10, printCutXmax, printCutYmax, color="#000000", width=.25)


for i in range(0, 371):
    theY = stripHeight
    theX = sg.map(i, 0, 360, 0, stripWidth, )
    tickHeight = 3.0  # mm
    if i % 5 == 0:
        tickHeight = 5.0
    if i % 10 == 0:
        tickHeight = 6.0
        theDoc += sg.graphText(str(i),theX,theY - 7.5, size="4pt", textAnchor="middle")
    theDoc += sg.graphLine(theX,theY + 1, theX, theY - tickHeight )  # print past the cut line
theDoc += "</g>\n"

# The vernier scale
# vernier for top disk
theDoc += "<g id='printvernier'>\n"
for i in range(-10, 11):
    theY = 40
    iValue = i - (0.1 * i)
    theX = sg.map(iValue, 0, 360, 0, stripWidth) + 10
    tickHeight = 2.5 # mm
    if i % 5 == 0:
        tickHeight = 3.25
    if i % 10 == 0:
        tickHeight = 3.50
    if i < 10 and i > -10:
        theDoc += sg.graphText(str(abs(i)), theX, theY + 3.75, size="1.5pt", textAnchor="middle")
    theDoc += sg.graphLine(theX,theY, theX, theY + tickHeight)
theDoc += sg.graphText("Vernier Scale",10,theY + 5.5,size="4pt", textAnchor="middle")
theDoc += "</g>\n"
theDocCut += sg.graphRectangle(3.30,theY,3.30 + 13.98 - 0.6 ,theY+7.55, color="#ff0000", width=0.1)

# ---------------------------------
# vernier for swing arm
swingArmRadius = 42.5
sg.setCenter(-80,60)
for i in range(0,11):
    whereToPrint = i
    tickHeight = 2.5 # mm
    if i % 5 == 0:
        tickHeight = 3.25
    if i % 10 == 0:
        tickHeight = 3.50
    if i == 0:
        whereToPrint = i + 0.25
    if i < 10 and i > -10:
        theDoc += sg.graphPolarText(str(abs(i)),0,0, whereToPrint + 90, swingArmRadius + 3.5, size="1.5pt", textAnchor="middle" )
    theDoc += sg.graphDualPolarLine(0,0,swingArmRadius,i + 90 , swingArmRadius+ tickHeight, i + 90, width=0.1)
# swing arm cutout
theDocCut += sg.graphArc(0,0,swingArmRadius,85,90 + 30 ,color="#ff0000")

topWidth = 9.19
inp1 = pysgfs.circle_line_segment_intersection([0, 0], swingArmRadius, [0,0], [10,0])
print("inp1",inp1)
theDocCut += sg.graphLine(inp1[1][0],inp1[1][1],inp1[1][0] + topWidth,inp1[1][1], color="#ff0000",width=0.1)

inp2 = pysgfs.circle_line_segment_intersection([0, 0], swingArmRadius, [0,-15], [10,-15])
print("inp2",inp2)
theDocCut += sg.graphLine(inp2[1][0],inp2[1][1],inp2[1][0]+12.19,inp2[1][1], color="#ff0000", width=0.1)

theDocCut += sg.graphLine(inp1[1][0]+9.46,inp1[1][1],inp1[1][0]+9.46,inp2[1][1], color="#ff0000", width=0.1)

# ---------------------------------
# put the center back to normal
sg.setCenter(0,0)


# Artwork for the Top Disk Dial
innerDiameter = 56.6
innerRadius = innerDiameter / 2
outerDiameter = 80.0
outerRadius = outerDiameter / 2
# actual protractor
for deg in range(0,360):
    tickWidth = 6.5
    if (deg % 5) == 0:
        tickWidth = 7.5
    if (deg % 10) == 0:
        tickWidth = 8.5
        theDoc += sg.graphPolarText(str(int(deg)),0,0, deg, innerRadius + 2.1 , size="4pt", textAnchor="middle")
    theDoc += sg.graphDualPolarLine(0,0, outerRadius - tickWidth, deg, outerRadius, deg)
    theDoc += sg.graphDualPolarLine(0,0, innerRadius, deg, innerRadius + 2, deg)
# CUT for the Top Disk Dial
cutColor = "#ff0000"
cutWidth = 0.1
#the wings
theDocWings = ""
wingStartX = 84/2 * -1
wingStartY = -10
wingEndX = 84/2
wingEndY = 10
wingCircleRadius = 80 / 2
wingLL = [wingStartX, wingStartY]
wingLR = [wingEndX, wingStartY]
wingUL = [wingStartX, wingEndY]
wingUR = [wingEndX, wingEndY]

ulp1, urp1 = pysgfs.circle_line_segment_intersection([0, 0], wingCircleRadius, wingUL, wingUR)
llp1, lrp1 = pysgfs.circle_line_segment_intersection([0, 0], wingCircleRadius, wingLL, wingLR)
print(ulp1, urp1)
print(llp1, lrp1)

theDocWings += sg.graphLine(wingStartX, wingEndY, ulp1[0], ulp1[1], width=cutWidth, color=cutColor) # UL
theDocWings += sg.graphLine(wingLL[0], wingLL[1], llp1[0], llp1[1], width=cutWidth, color=cutColor) # LL
theDocWings += sg.graphLine(wingLL[0], wingLL[1], wingUL[0], wingUL[1], width=cutWidth, color=cutColor) # UL to LL
ulPolarDegrees, ulPolarRadius = sg.cartesianToPolar(ulp1[0],ulp1[1])
urPolarDegrees, urPolarRadius = sg.cartesianToPolar(urp1[0], urp1[1])
theDocWings += sg.graphArc(0,0, ulPolarRadius, ulPolarDegrees, urPolarDegrees, width=cutWidth, color=cutColor)

llPolarDegrees, llPolarRadius = sg.cartesianToPolar(llp1[0], llp1[1])
lrPolarDegrees, lrPolarRadius = sg.cartesianToPolar(lrp1[0], lrp1[1])
theDocWings += sg.graphLine(urp1[0], urp1[1], wingUR[0], wingUR[1], width=cutWidth, color=cutColor)
theDocWings += sg.graphLine(wingUR[0], wingUR[1], wingLR[0], wingLR[1], width=cutWidth, color=cutColor)
theDocWings += sg.graphLine(lrp1[0], lrp1[1], wingLR[0], wingLR[1], width=cutWidth, color=cutColor)
theDocWings += sg.graphArc(0,0, llPolarRadius, lrPolarDegrees, llPolarDegrees, width=cutWidth, color=cutColor)

theDocWings += sg.graphCircle(0,0,innerDiameter / 2, width=cutWidth, color=cutColor)

# theDoc += theDocWings
theDocCut += theDocWings

# bottom arm protractor
innerRadiusProtractor = 32
outerRadiusProtractor = 42
for deg in range(0,91):
    tickWidth = 4.5
    if (deg % 5) == 0:
        tickWidth = 5.5
    if (deg % 10) == 0:
        tickWidth = 6.5
        degPrint = deg
        if int(deg) == 0:
            degPrint = deg + 1
        if int(deg) == 90:
            degPrint = deg - 1.5
        print(deg,degPrint)
        theDoc += sg.graphPolarText(str(int(deg)),30,30, degPrint, innerRadiusProtractor + 2.1 , size="4pt", textAnchor="middle")
    theDoc += sg.graphDualPolarLine(30,30, outerRadiusProtractor - tickWidth, deg, outerRadiusProtractor, deg)
    #theDoc += sg.graphDualPolarLine(30,30, innerRadiusProtractor, deg, innerRadiusProtractor + 2, deg)

# bottom arm protractor cut
theDocCut += sg.graphArc(30,30, innerRadiusProtractor,0,90, color="#ff0000")
theDocCut += sg.graphArc(30,30, outerRadiusProtractor,0,90, color="#ff0000")
theDocCut += sg.graphDualPolarLine(30,30,innerRadiusProtractor,0, outerRadiusProtractor, 0, color="#ff0000")
theDocCut += sg.graphDualPolarLine(30,30,innerRadiusProtractor, 90, outerRadiusProtractor, 90, color="#ff0000")



# the page cutout
printPortion, cutPortion = drawCutAndPrint(-132, -100,132,100)
theDoc += printPortion
theDoc += cutPortion
theDocCut += cutPortion


# ######################

theDoc += theDocCut # HERE Here temporary while debug to keep them both in one file

theDoc += sg.svgFooter()
theDocCut += sg.svgFooter()

# create the PRINT file
fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

# create the CUT file
fp = open("/tmp/misc/test-cut.svg", "w")
fp.writelines(theDocCut)
fp.close()

# print(theDoc)

print(sg.getSizeHuman())
