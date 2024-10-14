










 


SharpDX.Direct2D1.RenderTarget







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_rendertarget.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.RenderTarget | [Previous page](sharpdx_direct2d1_radialgradientbrushproperties.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Represents an object that can receive drawing commands. 


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd371766.aspx))


 


Syntax
------


class RenderTarget


 




|  |
| --- |
| Tips:  
1.For NinjaScript Development purposes, [DrawingTools](drawingtool.htm), [ChartStyles](chartstyletype.htm), [Indicators](indicators.htm), and [Strategies](strategy.htm) implement the Chart's [RenderTarget](rendertarget.htm) ready to be used in the OnRender() method2.General information on Direct2D Render Targets can be found on the [MSDN Direct2D Render Targets Overview](https://msdn.microsoft.com/en-us/library/dd756757(v=vs.85).aspx)   |





Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AntialiasMode](sharpdx_direct2d1_rendertarget_antialiasmode.htm) | Retrieves or sets the current antialiasing mode for nontext drawing operations. |
| [DrawEllipse()](sharpdx_direct2d1_rendertarget_drawellipse.htm) | Draws the outline of the specified ellipse using the specified stroke style. |
| [DrawGeometry()](sharpdx_direct2d1_rendertarget_drawgeometry.htm) | Draws the outline of the specified geometry. |
| [DrawLine()](sharpdx_direct2d1_rendertarget_drawline.htm) | Draws a line between the specified points.  |
| [DrawRectangle()](sharpdx_direct2d1_rendertarget_drawrectangle.htm) | Draws the outline of a rectangle that has the specified dimensions. |
| [DrawText()](sharpdx_direct2d1_rendertarget_drawtext.htm) | Draws the specified text using the format information provided by an [SharpDX.DirectWrite.TextFormat](sharpdx_directwrite_textformat.htm) object.  |
| [DrawTextLayout()](sharpdx_direct2d1_rendertarget_drawtextlayout.htm) | Draws the formatted text described by the specified [SharpDX.DirectWrite.TextLayout](sharpdx_directwrite_textlayout.htm) object. |
| [FillEllipse()](sharpdx_direct2d1_rendertarget_fillellipse.htm) | Paints the interior of the specified ellipse. |
| [FillGeometry()](sharpdx_direct2d1_rendertarget_fillgeometry.htm) | Paints the interior of the specified geometry. |
| [FillRectangle()](sharpdx_direct2d1_rendertarget_fillrectangle.htm) | Paints the interior of the specified rectangle.  |
| [IsDisposed](sharpdx_disposebase_isdisposed.htm) | Gets a value indicating whether this instance is disposed.  (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [Transform](sharpdx_direct2d1_rendertarget_transform.htm) | Gets or sets the current transform of the render target. |






 
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
 
 
 



