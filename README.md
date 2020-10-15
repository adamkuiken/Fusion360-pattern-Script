# Fusion360-pattern-Script
A script using the Fusion360 API and C# that allows users to create a patterned cut throughout an object.

The original file has not been debugged yet. The nature of the program is computationally expensive and I do not have the current resources to run it continuously and debug it. That being said it is almost entirely direct from the API documentation.

To Use:
- Select two objects in the fusion workspace.
  - The first should be the smaller object that you want to pattern and then cut out of the larger object.
  - The second should be the large object that you want to split apart.
- Run the code

This will take the first element of the selection array as the smaller object and the second element as the larger. Then it performs calculations based on a boundary box and creates a pattern around the object. Finally it selects all of the patterned objects and uses them as the tool on the cut of the larger object. This cuts the larger object by the 'grid' of the patterned smaller object. 
