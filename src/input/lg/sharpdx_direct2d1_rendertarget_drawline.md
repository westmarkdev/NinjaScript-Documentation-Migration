










 


SharpDX.Direct2D1.RenderTarget.DrawLine()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_rendertarget_drawline.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt; [RenderTarget](sharpdx_direct2d1_rendertarget.htm) &gt;
SharpDX.Direct2D1.RenderTarget.DrawLine() | [Previous page](sharpdx_direct2d1_rendertarget_drawgeometry.htm)
[Return to chapter overview](sharpdx_direct2d1_rendertarget.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Draws a line between the specified points.


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd371895.aspx))


 




|  |
| --- |
| Note:  This method doesn't return an error code if it fails. |



 


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush)  

RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth)  

RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth, StrokeStyle strokeStyle)


 
Parameters
------------




|  |  |
| --- | --- |
| brush | The [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush.htm) brush used to paint the line's stroke.  |
| point0 | A [SharpDX.Vector2](sharpdx_vector2.htm) which determines the start point of the line, in device-independent pixels.  |
| point1 | A [SharpDX.Vector2](sharpdx_vector2.htm) which determines the end point of the line, in device-independent pixels.  |
| strokeStyle | The [SharpDX.Direct2D1.StrokeStyle](sharpdx_direct2d1_strokestyle.htm) to paint, or null to paint a solid line. |
| strokeWidth | A value greater than or equal to 0.0f that specifies the width of the stroke. If this parameter isn't specified, it defaults to 1.0f. The stroke is centered on the line. |






 
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
 
 
 



