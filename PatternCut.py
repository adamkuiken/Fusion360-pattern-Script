import adsk.core, adsk.fusion,traceback

#get root
app = adsk.core.Application.get()
design = app.activeProduct
rootComp = design.rootComponent
ui = app.userInterface

ui.messageBox('Script activated')
selections - ui.activeSelections
#get cut object (small) and object to cut (large)
small = selections[0]
large = selections[1]

#get Large Object Measurements
vL1 = adsk.core.Vector3D.create(0.0, 0.0, 1.0)
vL2 = adsk.core.Vector3D.create(0.0, 1.0, 0.0)
boxL = app.measureManager.getOrientedBoundingBox(lare,vL1,vL2)
largeLen = boxL.length
largeWid = boxL.width
largeHeight = boxL.height

#get Small Object Measurements
vS1 = adsk.core.Vector3D.create(0.0, 0.0, 1.0)
vS2 = adsk.core.Vector3D.create(0.0, 1.0, 0.0)
boxS = app.measureManager.getOrientedBoundingBox(small,vS1,vS2)
smallLen = boxS.length
smallWid = boxS.width
smallHeight = boxS.height
spacing = 0.001
lenSplit = int(round(largeLen/(smallLen + spacing)))
widSplit = int(round(LargeWid/(smallWid + spacing)))

#create input entities
inputEntites = adsk.core.ObjectCollection.create()
inputEntites.add(small)



#set Quantities for grid
quantityOne = adsk.core.ValueInput.createByString(lenSplit)
distanceOne = adsk.core.ValueInput.createByString(spacing)
quantityTwo = adsk.core.ValueInput.createByString(widSplit)
distanceTwo = adsk.core.ValueInput.createByString(spacing)

#set inputs for pattern
rectangularPatterns = rootComp.features.rectangularPatternFeatures
rectangularPatternInput = rectangularPatterns.createInput(inputEntites, xAxis, quantityOne, distanceOne, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)

# Set the data for second direction
rectangularPatternInput.setDirectionTwo(yAxis, quantityTwo, distanceTwo)

# Create the rectangular pattern
rectangularFeature = rectangularPatterns.add(rectangularPatternInput)

#define objects for cut
targetBody = large
toolBodies = rectangularFeature
CombineCutInput = rootComp.features.combineFeatures.createInput(targetBody, toolBodies )

#create cut     
CombineCutFeats = features.combineFeatures
CombineCutInput = CombineCutFeats.createInput(targetBody, toolBodies)
CombineCutInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
CombineCutFeats.add(CombineCutInput)

row = 0 # index of row
numRow = 10 #number of blocks in a row 
count = 0
for i in CombineCutFeats:
    i.transform = (spacing + smallLen*i,spacing + row*smallWid,0)
    count = count+1
    if count == numRow:
        count = 0
        row = row+1

ui.messageBox('Script Completed')