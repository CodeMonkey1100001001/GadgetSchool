# from pprint import pprint
import math

import PythonSmolGraphSVG  # use current version that is included here
import PythonSmolGraphFancyStuff
import math

print("Tangent Table")
print("α - angle in degrees, tan(α), tan(α) * 100, sin(α), sin(α) * 100")
precisionMult = 1
for i in range(0,90 * precisionMult):
    theAngleDegrees = i / precisionMult
    theTrigTan = math.tan(math.radians(theAngleDegrees))
    theTrigSin = math.sin(math.radians(theAngleDegrees))
    whatIf100Tan= 100 * theTrigTan
    whatIf100Sin = 100 * theTrigSin
    theAngleDegrees = int(theAngleDegrees)
    print(f'{theAngleDegrees:02d}\t{theTrigTan:0.06f}\t{whatIf100Tan:0.02f}\t{theTrigSin:0.06f}\t{whatIf100Sin:0.02f}')

def drawGrid():
    global theDoc
    # theDoc += f'<g inkscape:groupmode="layer"\nid="layer1"\ninkscape:label="Grid">\n'
    theDoc += f'<g>\n'
    dgx = sg.minValueX
    print("sg.minValueX", sg.minValueX)
    print("sg.minValueY", sg.minValueY, sg.maxValueY)
    if (sg.units == "inch"):
        gridStep = 1.0
    if (sg.units == "mm"):
        gridStep = 10

    while dgx < sg.maxValueX:
        # print("dgx",dgx)
        theDoc += sg.graphLine(dgx, sg.minValueY, dgx, sg.maxValueY, "#5f9b9c")
        #theDoc += sg.graphText(str(int(dgx)), dgx, sg.minValueY + 10, size="4pt", color="#444444")
        dgx = dgx + gridStep

    dgy = sg.minValueY
    while dgy < sg.maxValueY:
        theDoc += sg.graphLine(sg.minValueX, dgy, sg.maxValueX, dgy, "#5f9b9c")
        #theDoc += sg.graphText(str(int(dgy)), sg.minValueX + 10, dgy, size="4pt", color="#444444")
        dgy = dgy + gridStep

    theDoc += sg.graphLine(sg.minValueX, 0, sg.maxValueX, 0, 0.1, "red")
    theDoc += sg.graphLine(0, sg.minValueY, 0, sg.maxValueY, 0.1, "green")
    theDoc += "</g>\n"


print("hello")

sg = PythonSmolGraphSVG.SmolGraph2SVG("inch")
pysgfs = PythonSmolGraphFancyStuff.SmolGraphFancy("inch")

# 8.5" x 11" sheet of paper
baseSizeX = 8.5
baseSizeY = 11

sg.setSize(baseSizeX, baseSizeY, baseSizeX / 2 * -1.0, baseSizeX / 2, baseSizeY / 2 * -1.0, baseSizeY / 2)
# sg.setCenter(baseSizeX / 2, baseSizeY / 2)
theDoc = sg.svgHeader()
theDocCut = ""  # HERE Here sg.svgHeader()

# #########################
sg.setCenter(0,0)
drawGrid()
cols = [-3.7, -1.80]
sg.fontFamily = "OldTimesAmericanTitlingW"
sg.fontSize = "12pt"
theDoc += sg.graphText("α - ANGLE IN DEGREES tan(α), sin(α) TABLE", 0,5.0, textAnchor="middle")
theDoc += sg.graphText("PLUS CALCUATIONS FOR 100", 0,4.8, textAnchor="middle")
theDoc += sg.graphText("300", -3.75,5.0, textAnchor="middle", size="14pt")  # fake page number

theDoc += sg.graphText("α°", cols[0],4.125, textAnchor="start", size="14pt")  # fake page number
theDoc += sg.graphText("tan(α)", cols[0] + 0.40,4.125, textAnchor="start", size="14pt")  # fake page number
theDoc += sg.graphText("x100", cols[0] + 0.40 + 0.7,4.125, textAnchor="start", size="14pt")  # fake page number

theDoc += sg.graphText("α°", cols[1], 4.125, textAnchor="start", size="14pt")  # fake page number
theDoc += sg.graphText("tan(α)", cols[1] + 0.40,4.125, textAnchor="start", size="14pt")  # fake page number
theDoc += sg.graphText("x100", cols[1] + 0.40 + 0.7,4.125, textAnchor="start", size="14pt")  # fake page number


#theDoc += sg.graphDisk(0,0,1,color="#00ff00")
print("Tangent Table")
print("α - angle in degrees, tan(α), tan(α) * 100, sin(α), sin(α) * 100")
precisionMult = 1
theFivesAdd = 0
for i in range(0,90 * precisionMult):
    theAngleDegrees = i / precisionMult
    theTrigTan = math.tan(math.radians(theAngleDegrees))
    theTrigSin = math.sin(math.radians(theAngleDegrees))
    whatIf100Tan= 100 * theTrigTan
    whatIf100Sin = 100 * theTrigSin
    theAngleDegrees = int(theAngleDegrees)
    theDegree = f'{theAngleDegrees:02}'
    if (theAngleDegrees % 5) == 0:
        theFivesAdd += 0.1
    print(f'{theDegree}\t{theTrigTan:0.06f}\t{whatIf100Tan:0.02f}\t{theTrigSin:0.06f}\t{whatIf100Sin:0.02f}')
    colY = 4 - (i * 0.18) - theFivesAdd
    colX = cols[0] #-3.5
    if theAngleDegrees == 44:
        theFivesAdd = 0
    if theAngleDegrees > 44:
        colX = cols[1] #-2.2
        colY = 4 - ((i - 45)  * 0.18) - theFivesAdd

    theDoc += sg.graphText(theDegree, colX, colY, textAnchor="start" )
    theDoc += sg.graphText(f'{theTrigTan:0.05f}', colX + 0.40, colY, textAnchor="start" )
    theDoc += sg.graphText(f'{whatIf100Tan:0.02f}', colX + 1.15, colY, textAnchor="start" )




# ############################
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
