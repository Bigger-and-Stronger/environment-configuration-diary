from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Display.SimpleGui import init_display
import os

def create_cube(length=1.0):
    cube_shape = BRepPrimAPI_MakeBox(length, length, length).Shape()
    return cube_shape

def export_step(shape, filename="cube.step"):
    step_writer = STEPControl_Writer()
    status = step_writer.Transfer(shape, STEPControl_AsIs)
    if status != IFSelect_RetDone:
        print("STEP export failed.")
        return False

    output_path = os.path.abspath(filename)
    if step_writer.Write(output_path) == IFSelect_RetDone:
        print(f"STEP file exported to: {output_path}")
        return True
    else:
        print("Failed to write STEP file.")
        return False

def display_shape(shape):
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(shape, update=True)
    start_display()

if __name__ == "__main__":
    cube = create_cube(1.0)
    export_step(cube, "cube.step")
    # display_shape(cube)