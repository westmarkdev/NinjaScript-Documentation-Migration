










 


SharpDX.Direct2D1.StrokeStyle







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_strokestyle.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.StrokeStyle | [Previous page](sharpdx_direct2d1_solidcolorbrush_color.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Describes the caps, miter limit, line join, and dash information for a stroke.


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd372217.aspx))


 




|  |
| --- |
| Notes:  
1.A stroke style is a device-independent resource; you can create it once then retain it for the life of your application. Please see the [MSDN Direct2D Resources Overview](https://msdn.microsoft.com/en-us/library/dd756757(v=vs.85).aspx) for more information.2.For convenience, Direct2D provides the [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.htm) function for creating new a StrokeStyle. |



 


 


Syntax
------


class StrokeStyle


 
Constructors
--------------




|  |  |
| --- | --- |
| new StrokeStyle(Factory factory, [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.htm) properties) | Creates an StrokeStyle that describes start cap, dash pattern, and other features of a stroke.  |
| new StrokeStyle(Factory factory, [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.htm) properties, float[] dashes) | Creates an StrokeStyle that describes start cap, dash pattern, and other features of a stroke.  |







|  |
| --- |
| Tip: For NinjaScript development purposes, when creating a StrokeStyle object you should use the [NinjaTrader.Core.Globals.D2DFactory](d2dfactory.htm) property |





Method and Properties
---------------------




|  |  |
| --- | --- |
| [DashCap](sharpdx_direct2d1_strokestyle_dashcap.htm) | Gets a value that specifies how the ends of each dash are drawn.  |
| [DashesCount](sharpdx_direct2d1_strokestyle_dashescount.htm) | Retrieves the number of entries in the dashes array.  |
| [DashOffset](sharpdx_direct2d1_strokestyle_dashoffset.htm) | Retrieves a value that specifies how far in the dash sequence the stroke will start.  |
| [DashStyle](sharpdx_direct2d1_strokestyle_dashstyle.htm) | Gets a value that describes the stroke's dash pattern.  |
| [Dispose()](sharpdx_disposebase_dispose.htm) | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [EndCap](sharpdx_direct2d1_strokestyle_endcap.htm) | Retrieves the type of shape used at the end of a stroke.  |
| [GetDashes()](sharpdx_direct2d1_strokestyle_getdashes.htm) | Copies the dash pattern to the specified array.  |
| [IsDisposed](sharpdx_disposebase_isdisposed.htm) | Gets a value indicating whether this instance is disposed. (Inherited from DisposeBase.) |
| [LineJoin](sharpdx_direct2d1_strokestyle_linejoin.htm) | Retrieves the type of joint used at the vertices of a shape's outline.  |
| [MiterLimit](sharpdx_direct2d1_strokestyle_miterlimit.htm) | Retrieves the limit on the ratio of the miter length to half the stroke's thickness.  |
| [StartCap](sharpdx_direct2d1_strokestyle_startcap.htm) | Retrieves the type of shape used at the beginning of a stroke.  |






 
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
 
 
 



