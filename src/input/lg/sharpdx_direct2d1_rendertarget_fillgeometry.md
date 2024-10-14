










 


SharpDX.Direct2D1.RenderTarget.FillGeometry()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_rendertarget_fillgeometry.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt; [RenderTarget](sharpdx_direct2d1_rendertarget.htm) &gt;
SharpDX.Direct2D1.RenderTarget.FillGeometry() | [Previous page](sharpdx_direct2d1_rendertarget_fillellipse.htm)
[Return to chapter overview](sharpdx_direct2d1_rendertarget.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Paints the interior of the specified geometry.


(See also [unamanged API documentation](http://msdn.microsoft.com/en-us/library/dd371933.aspx))


 




|  |
| --- |
| Note:  
1.If the opacityBrush parameter is not null, the alpha value of each pixel of the mapped opacityBrush is used to determine the resulting opacity of each corresponding pixel of the geometry. Only the alpha value of each color in the brush is used for this processing; all other color information is ignored. The alpha value specified by the brush is multiplied by the alpha value of the geometry after the geometry has been painted by brush.  2.This method doesn't return an error code if it fails. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


RenderTarget.FillGeometry(Geometry geometry, Brush brush)  

RenderTarget.FillGeometry(Geometry geometry, Brush brush, Brush opacityBrush)


 
Parameters
------------




|  |  |
| --- | --- |
| brush | The [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush.htm) used to paint the geometry's interior. |
| geometry | The [SharpDX.Direct2D1.Geometry](sharpdx_direct2d1_pathgeometry.htm) to paint. |
| opacityBrush | The [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush.htm) opacity mask to apply to the geometry, or null for no opacity mask. For more information, see the note section above |






 
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
 
 
 



