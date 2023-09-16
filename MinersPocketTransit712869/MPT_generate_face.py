# from pprint import pprint
import math
import PythonSmolGraphSVG  # use current version that is included here
import PythonSmolGraphFancyStuff  #

# import PythonSmolGraphFancyStuff
# import math

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
baseSizeX = 215.9
baseSizeY = 279.4

sg.setSize(baseSizeX , baseSizeY, baseSizeX / 2 * -1.0 , baseSizeX / 2, baseSizeY / 2 * -1.0 , baseSizeY/2)
# sg.setCenter(baseSizeX / 2, baseSizeY / 2)
theDoc = sg.svgHeader()
theDocCut = sg.svgHeader()

# #########################
# drawGrid()

innerDiameter = 56.6
innerRadius = innerDiameter / 2
outerDiameter = 80.0
outerRadius = outerDiameter / 2

# theDoc += sg.graphCircle(0,0,innerDiameter / 2, width=0.7, color="#000000")
# theDoc += sg.graphCircle(0,0,outerDiameter / 2, width=0.7, color="#000000")
# theDoc += sg.graphCircle(0,0,10, width=0.7, color="#ff0000")

# theDoc += sg.graphRectangle(84/2 * -1.0 , -10 , 84/2 ,10, width=0.7)

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


# bottom arm protractor
innerRadiusProtractor = 32
outerRadiusProtractor = 42
for deg in range(0,91):
    tickWidth = 4.5
    if (deg % 5) == 0:
        tickWidth = 5.5
    if (deg % 10) == 0:
        tickWidth = 6.5
        theDoc += sg.graphPolarText(str(int(deg)),30,30, deg, innerRadiusProtractor + 2.1 , size="4pt", textAnchor="middle")
    theDoc += sg.graphDualPolarLine(30,30, outerRadiusProtractor - tickWidth, deg, outerRadiusProtractor, deg)
    #theDoc += sg.graphDualPolarLine(30,30, innerRadiusProtractor, deg, innerRadiusProtractor + 2, deg)

# bottom arm protractor cut
theDocCut += sg.graphArc(30,30, innerRadiusProtractor,0,90, color="#ff0000")
theDocCut += sg.graphArc(30,30, outerRadiusProtractor,0,90, color="#ff0000")
theDocCut += sg.graphDualPolarLine(30,30,innerRadiusProtractor,0, outerRadiusProtractor, 0, color="#ff0000")
theDocCut += sg.graphDualPolarLine(30,30,innerRadiusProtractor, 90, outerRadiusProtractor, 90, color="#ff0000")

# cut file
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




# the page cutout
printPortion, cutPortion = drawCutAndPrint(-100, -100,100,100)

theDoc += printPortion
# theDoc += cutPortion
theDocCut += cutPortion
# theDoc += sg.graphLine(wingStartX, wingStartY, llp1[0], llp1[1], width=0.7, color="#00ff00")
# theDoc += sg.graphLine(lrp1[0], lrp1[1], wingEndX, wingStartY, width=0.7, color="#00ff00")
# ######################

theDoc += sg.svgFooter()
theDocCut += sg.svgFooter()

fp = open("/tmp/misc/test.svg", "w")
fp.writelines(theDoc)
fp.close()

fp = open("/tmp/misc/test-cut.svg", "w")
fp.writelines(theDocCut)
fp.close()
# print(theDoc)

# print(sg.getSizeHuman())
