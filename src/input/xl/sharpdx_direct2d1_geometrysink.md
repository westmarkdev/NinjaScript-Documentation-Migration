










 


SharpDX.Direct2D1.GeometrySink







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_geometrysink.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.GeometrySink | [Previous page](sharpdx_direct2d1_fillmode.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Describes a geometric path that can contain lines, arcs, cubic Bezier curves, and quadratic Bezier curves. 


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd316592.aspx))


 




|  |
| --- |
| Notes:   
1.To create a GeometrySink, describe a [PathGeometry](sharpdx_direct2d1_pathgeometry.htm) and retrive the object using the [PathGeometry.Open()](sharpdx_direct2d1_pathgeometry_open.htm) method2.A geometry sink consists of one or more figures. Each figure is made up of one or more line, curve, or arc segments. To create a figure, call the [BeginFigure](sharpdx_direct2d1_geometrysink_beginfigure.htm) method, specify the figure's start point, and then use its Add methods (such as [AddLine](sharpdx_direct2d1_geometrysink_addline.htm)) to add segments. When you are finished adding segments, call the [EndFigure](sharpdx_direct2d1_geometrysink_endfigure.htm) method. You can repeat this sequence to create additional figures. When you are finished creating figures, call the [Close](sharpdx_direct2d1_geometrysink_close.htm) method. |



 


Syntax
------


interface GeometrySink


 
Methods
---------




|  |  |
| --- | --- |
| [AddArc()](sharpdx_direct2d1_geometrysink_addarc.htm) | Adds a single arc to the path geometry.  |
| [AddLine()](sharpdx_direct2d1_geometrysink_addline.htm) | Creates a line segment between the current point and the specified end point and adds it to the geometry sink.  |
| [AddLines()](sharpdx_direct2d1_geometrysink_addlines.htm) | Creates a sequence of lines using the specified points and adds them to the geometry sink.  |
| [BeginFigure()](sharpdx_direct2d1_geometrysink_beginfigure.htm) | Starts a new figure at the specified point.  |
| [Close()](sharpdx_direct2d1_geometrysink_close.htm) | Closes the geometry sink, indicates whether it is in an error state, and resets the sink's error state.  |
| [Dispose()](sharpdx_disposebase_dispose.htm) | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.  (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [EndFigure()](sharpdx_direct2d1_geometrysink_endfigure.htm) | Ends the current figure; optionally, closes it.  |
| [SetFillMode()](sharpdx_direct2d1_geometrysink_setfillmode.htm) | Specifies the method used to determine which points are inside the geometry described by this geometry sink and which points are outside.  |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



