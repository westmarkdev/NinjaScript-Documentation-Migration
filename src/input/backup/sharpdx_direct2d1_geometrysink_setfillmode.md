










 


SharpDX.Direct2D1.GeometrySink.SetFillMode()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_geometrysink_setfillmode.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt; [GeometrySink](sharpdx_direct2d1_geometrysink.htm) &gt;
SharpDX.Direct2D1.GeometrySink.SetFillMode() | [Previous page](sharpdx_direct2d1_geometrysink_endfigure.htm)
[Return to chapter overview](sharpdx_direct2d1_geometrysink.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Specifies the method used to determine which points are inside the geometry described by this geometry sink and which points are outside.


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316937.aspx))


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


<geometrysink>.SetFillMode(FillMode fillMode)


 
Parameters
------------




|  |  |
| --- | --- |
| fillMode | The [SharpDX.Direct2D1.FillMode](sharpdx_direct2d1_fillmode.htm) used to determine whether a given point is part of the geometry.  |






 
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
 
 
 



</geometrysink>