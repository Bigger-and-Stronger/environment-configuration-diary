#include "Viewer.h"

#include <BRepTools.hxx>
#include <BRepPrimAPI_MakeBox.hxx>

int main(int argc, char** argv)
{
  Viewer vout(50, 50, 500, 500);

  vout << BRepPrimAPI_MakeBox(10, 10, 20)
       << BRepPrimAPI_MakeBox(20, 30, 10);

  if ( argc > 1 )
  {
    BRep_Builder bb;
    TopoDS_Shape fromFile;
    //
    if ( !BRepTools::Read(fromFile, argv[1], bb) )
    {
      std::cout << "Failed to read BREP shape from file " << argv[1] << std::endl;
      return 1;
    }

    vout << fromFile;
  }

  vout.StartMessageLoop();

  return 0;
}
