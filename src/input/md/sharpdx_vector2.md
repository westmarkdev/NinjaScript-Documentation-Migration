










 


SharpDX.Vector2







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_vector2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX](sharpdx.htm) &gt;
SharpDX.Vector2 | [Previous page](sharpdx_size2f.htm)
[Return to chapter overview](sharpdx.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX / Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Represents a two dimensional mathematical vector.


 


Syntax
------


struct Vector2


 




|  |
| --- |
| Tip:  For NinjaScript Development Purposes, you can use the [NinjaTrader.Gui.DxExtensions.ToVector2()](dxextensions_tovector2.htm) helper method to convert a System.Windows.Point structure to a SharpDX.Vector2 used for SharpDX rendering.  |




   

Constructors




|  |  |
| --- | --- |
| Vector2() | Initializes a new instance of the Vector2 struct.  |
| Vector2(float x, float y) | Initializes a new instance of the Vector2 struct using float values for x and y components |





Properties




|  |  |
| --- | --- |
| X | A float for the X component of the vector.  |
| Y | A float for the Y component of the vector.  |






 
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
 
 
 



