










 


SharpDX.Direct2D1.LinearGradientBrushProperties







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_lineargradientbrushproperties.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.LinearGradientBrushProperties | [Previous page](sharpdx_direct2d1_lineargradientbrush_startpoint.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Contains the starting point and endpoint of the gradient axis for an [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush.htm). 


(See also [unmanaged API documentationth](msdn.microsoft.com/en-us/library/dd368128.aspx))


 


Syntax
------


struct LinearGradientBrushProperties


   

Constructors




|  |  |
| --- | --- |
| new LinearGradientBrushProperties() | Initializes a new instance of the LinearGradientBrushProperties structure |





Properties




|  |  |
| --- | --- |
| StartPoint | A [SharpDX.Vector2](sharpdx_vector2.htm) representing brush's coordinate space, the starting point of the gradient axis.  |
| EndPoint | A [SharpDX.Vector2](sharpdx_vector2.htm) representing the brush's coordinate space, the endpoint of the gradient axis.
  |






 
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
 
 
 



