










 


DisposeBase







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_disposebase.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX](sharpdx.htm) &gt;
DisposeBase | [Previous page](sharpdx_color4.htm)
[Return to chapter overview](sharpdx.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Base class for a [System.IDisposable](https://msdn.microsoft.com/en-us/library/aax125c9) class.


 




|  |
| --- |
| Tip:  For NinjaScript development purposes, the following documented SharpDX objects require [Dispose()](sharpdx_disposebase_dispose.htm) after they are used: 
 
[Brush](sharpdx_direct2d1_brush.htm), [GeometrySink](sharpdx_direct2d1_geometrysink.htm), [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm), [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush.htm), [PathGeometry](sharpdx_direct2d1_pathgeometry.htm), [RadialGradientBrush](sharpdx_direct2d1_radialgradientbrush.htm), [SolidColorBrush](sharpdx_direct2d1_solidcolorbrush.htm), [StrokeStyle](sharpdx_direct2d1_strokestyle.htm), [TextFormat](sharpdx_directwrite_textformat.htm), [TextLayout](sharpdx_directwrite_textlayout.htm)
 
There are other undocumented SharpDX objects which are NOT included in this reference. Please be careful to dispose of any object (SharpDX or otherwise) which implements the IDisposeable interface - NinjaTrader is NOT guaranteed to dispose of these objects for you! |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| IsDisposed | Gets a value indicating whether this instance is disposed.  |
| Dispose() | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Implements [IDisposable.Dispose()](https://msdn.microsoft.com/en-us/library/es4s3w1d)) |






 
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
 
 
 



