# Sample FreeCAD Automation Script
import FreeCAD, Part

# Create a simple box
doc = FreeCAD.newDocument("SampleBox")
box = doc.addObject("Part::Box", "Box")
box.Length = 10
box.Width = 20
box.Height = 5

# Export as STEP file
Part.export([box], "SampleBox.step")
print("STEP file exported successfully!")
