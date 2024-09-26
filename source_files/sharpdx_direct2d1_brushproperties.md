










 


SharpDX.Direct2D1.BrushProperties







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_brushproperties.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.BrushProperties | [Previous page](sharpdx_direct2d1_brush_transform.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Describes the opacity and transformation of a brush.


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368077.aspx))


 


Syntax
------


struct BrushProperties


   

Constructors




|  |  |
| --- | --- |
| new BrushProperties() | Initializes a new instance of the BrushProperties structure |





Properties




|  |  |
| --- | --- |
| Opacity | A value between 0.0f and 1.0f, inclusive, that specifies the degree of opacity of the brush. |
| Transform | The transformation that is applied to the brush. |






 
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
 
 
 



