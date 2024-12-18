﻿










 


SharpDX.Direct2D1.LinearGradientBrush.StartPoint







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_lineargradientbrush_startpoint.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt; [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush.htm) &gt;
SharpDX.Direct2D1.LinearGradientBrush.StartPoint | [Previous page](sharpdx_direct2d1_lineargradientbrush_gradientstopcollection.htm)
[Return to chapter overview](sharpdx_direct2d1_lineargradientbrush.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Retrieves the starting coordinates of the linear gradient. 


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd371497.aspx))


 




|  |
| --- |
| Note:  The start point and end point are described in the brush's space and are mapped to the render target when the brush is used. If there is a non-identity brush transform or render target transform, the brush's start point and end point are also transformed. |





Property Value
--------------


A [SharpDX.Vector2](sharpdx_vector2.htm) representing the starting two-dimensional coordinates of the linear gradient, in the brush's coordinate space.


 


Syntax
------


<lineargradientbrush>.StartPoint





 
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
 
 
 



</lineargradientbrush>