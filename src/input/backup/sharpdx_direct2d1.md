










 


SharpDX.Direct2D1







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt;
SharpDX.Direct2D1 | [Previous page](sharpdx_vector2.htm)
[Return to chapter overview](sharpdx_sdk_reference.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |





The SharpDX.Direct2D1 namespace provides a managed Direct2D API.   Direct2D is a hardware-accelerated, immediate-mode, 2-D graphics API that provides high performance and high-quality rendering for 2-D geometry, bitmaps, and text.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd370990.aspx))




In this section
---------------




|  |  |
| --- | --- |
| [AntialiasMode](sharpdx_direct2d1_antialiasmode.htm) | Specifies how the edges of nontext primitives are rendered. |
| [ArcSegment](sharpdx_direct2d1_arcsegment.htm) | Describes an elliptical arc between two points. |
| [ArcSize](sharpdx_direct2d1_arcsize.htm) | Specifies whether an arc should be greater than 180 degrees. |
| [Brush](sharpdx_direct2d1_brush.htm) | Defines an object that paints an area. Interfaces that derive from Brush describe how the area is painted.  |
| [BrushProperties](sharpdx_direct2d1_brushproperties.htm) | Describes the opacity and transformation of a brush. |
| [DrawTextOptions](sharpdx_direct2d1_drawtextoptions.htm) | Specifies whether text snapping is suppressed or clipping to the layout rectangle is enabled. This enumeration allows a bitwise combination of its member values. |
| [Ellipse](sharpdx_direct2d1_ellipse.htm) | Contains the center point, x-radius, and y-radius of an ellipse. |
| [FigureBegin](sharpdx_direct2d1_figurebegin.htm) | Indicates whether a specific GeometrySink figure is filled or hollow.  |
| [FigureEnd](sharpdx_direct2d1_figureend.htm) | Indicates whether a specific GeometrySink figure is open or closed.  |
| [FillMode](sharpdx_direct2d1_fillmode.htm) | Specifies how the intersecting areas of geometries or figures are combined to form the area of the composite geometry.  |
| [GeometrySink](sharpdx_direct2d1_geometrysink.htm) | Describes a geometric path that can contain lines, arcs, cubic Bezier curves, and quadratic Bezier curves.  |
| [MeasuringMode](sharpdx_direct2d1_measuringmode.htm) | Indicates the measuring method used for [text layout](sharpdx_directwrite_textlayout.htm). |
| [PathGeometry](sharpdx_direct2d1_pathgeometry.htm) | Represents a complex shape that may be composed of arcs, curves, and lines.  |
| [RenderTarget](sharpdx_direct2d1_rendertarget.htm) | Represents an object that can receive drawing commands.  |
| [SolidColorBrush](sharpdx_direct2d1_solidcolorbrush.htm) | Paints an area with a solid color. |
| [StrokeStyle](sharpdx_direct2d1_strokestyle.htm) | Describes the caps, miter limit, line join, and dash information for a stroke. |
| [SweepDirection](sharpdx_direct2d1_sweepdirection.htm) | Defines the direction that an elliptical arc is drawn. |






 
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
 
 
 



