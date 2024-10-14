










 


SharpDX.Direct2D1.GeometrySink.AddArc()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_geometrysink_addarc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt; [GeometrySink](sharpdx_direct2d1_geometrysink.htm) &gt;
SharpDX.Direct2D1.GeometrySink.AddArc() | [Previous page](sharpdx_direct2d1_geometrysink.htm)
[Return to chapter overview](sharpdx_direct2d1_geometrysink.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Adds a single arc to the path geometry.


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd742733.aspx))


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


<geometrysink>.AddArc(ArcSegment arc)


 
Parameters
------------




|  |  |
| --- | --- |
| arc | The [SharpDX.Direct2D1.ArcSegment](sharpdx_direct2d1_arcsegment.htm) segment to add to the figure.  |






 
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