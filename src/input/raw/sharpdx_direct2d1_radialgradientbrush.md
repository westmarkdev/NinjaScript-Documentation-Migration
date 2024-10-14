










 


SharpDX.Direct2D1.RadialGradientBrush







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_direct2d1_radialgradientbrush.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.Direct2D1](sharpdx_direct2d1.htm) &gt;
SharpDX.Direct2D1.RadialGradientBrush | [Previous page](sharpdx_direct2d1_pathgeometry_strokecontainspoint.htm)
[Return to chapter overview](sharpdx_direct2d1.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Paints an area with a radial gradient.


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd371529.aspx))


 




|  |
| --- |
| Notes:
1.The RadialGradientBrush is similar to the [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush.htm) in that they both map a collection of gradient stops to a gradient. However, the linear gradient has a start and an end point to define the gradient vector, while the radial gradient uses an ellipse and a gradient origin to define its gradient behavior. To define the position and size of the ellipse, use the [Center](sharpdx_direct2d1_radialgradientbrush_center.htm), [RadiusX](sharpdx_direct2d1_radialgradientbrush_radiusx.htm), and [RadiusY](sharpdx_direct2d1_radialgradientbrush_radiusy.htm) properties to specify the center, x-radius, and y-radius of the ellipse. The gradient origin is the center of the ellipse, unless a gradient offset is specified by using the GradientOriginOffset method.2.The brush maps the gradient stop position 0.0f of the gradient origin, and the position 1.0f is mapped to the ellipse boundary. When the gradient origin is within the ellipse, the contents of the ellipse enclose the entire [0, 1] range of the brush gradient stops. If the gradient origin is outside the bounds of the ellipse, the brush still works, but its gradient is not well-defined.3.The start point and end point are described in the brush space and are mappped to the [render target](sharpdx_direct2d1_rendertarget.htm) when the brush is used. Note the starting and ending coordinates are absolute, not relative to the render target size. A value of (0, 0) maps to the upper-left corner of the render target, while a value of (1, 1) maps just one pixel diagonally away from (0, 0). If there is a nonidentity brush transform or render target transform, the brush ellipse and gradient origin are also transformed.4.It is possible to specify an ellipse that does not completely fill area being painted. When this occurs, the [ExtendMode](sharpdx_direct2d1_gradientstopcollection_extendmode.htm) and setting (specified by the brush [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm)) determines how the remaining area is painted.5.A RadialGradientBrush brush may be used only with the [render target](sharpdx_direct2d1_rendertarget.htm) that created it or with the compatible targets for that render target.6.A RadialGradientBrush is a device-dependent resource: your application should create radial gradient brushes after it initializes the render target with which the brushes will be used, and recreate the brushes whenever the render target needs recreated. Please see the [MSDN Direct2D Resources Overview](https://msdn.microsoft.com/en-us/library/dd756757(v=vs.85).aspx) for more information.7.For convenience, Direct2D provides the [RadialGradientBrushProperties](sharpdx_direct2d1_radialgradientbrushproperties.htm) function for creating new a RadialGradientBrush. |



 


 


Syntax
------


class SolidColorBrush


 




|  |
| --- |
| Tips:  
1.For NinjaScript Development purposes, you can use the [NinjaTrader.Gui.DxExtensions.ToDxBrush()](dxextensions_todxbrush.htm) helper method to convert a System.Windows.Media.LinearGradientBrush to a SharpDX.Direct2D1.LinearGradientBrush 2.General information on Direct2D brushes can be found on the [MSDN Direct2D Brushes Overview](https://msdn.microsoft.com/en-us/library/dd756651(v=vs.85).aspx)   |




 
Constructors
--------------




|  |  |
| --- | --- |
| new RadialGradientBrush([RenderTarget](sharpdx_direct2d1_rendertarget.htm) renderTarget, [RadialGradientBrushProperties](sharpdx_direct2d1_radialgradientbrushproperties.htm) radialGradientBrushProperties, 
[GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm) gradientStopCollection) | Creates an RadialGradientBrush that contains the specified gradient stops and has the specified transform and base opacity. |
| new RadialGradientBrush([RenderTarget](sharpdx_direct2d1_rendertarget.htm) renderTarget, [RadialGradientBrushProperties](sharpdx_direct2d1_radialgradientbrushproperties.htm) radialGradientBrushProperties, [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm) gradientStopCollection) | Creates an RadialGradientBrush that contains the specified gradient stops and has the specified transform and base opacity.  |
| new RadialGradientBrush([RenderTarget](sharpdx_direct2d1_rendertarget.htm) renderTarget, [RadialGradientBrushProperties](sharpdx_direct2d1_radialgradientbrushproperties.htm) radialGradientBrushProperties, [BrushProperties](sharpdx_direct2d1_brushproperties.htm) brushProperties, [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm) gradientStopCollection) | Creates an RadialGradientBrush that contains the specified gradient stops and has the specified transform and base opacity.  |
| new RadialGradientBrush([RenderTarget](sharpdx_direct2d1_rendertarget.htm) renderTarget, [RadialGradientBrushProperties](sharpdx_direct2d1_radialgradientbrushproperties.htm) radialGradientBrushProperties, Nullable&lt;[BrushProperties](sharpdx_direct2d1_brushproperties.htm)&gt; brushProperties, [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm) gradientStopCollection) | Creates an RadialGradientBrush that contains the specified gradient stops and has the specified transform and base opacity.  |





Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Center](sharpdx_direct2d1_radialgradientbrush_center.htm) | Retrieves or sets the center of the gradient ellipse.  |
| [Dispose()](sharpdx_disposebase_dispose.htm) | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [IsDisposed](sharpdx_disposebase_isdisposed.htm) | Gets a value indicating whether this instance is disposed. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [GradientOriginOffset](sharpdx_direct2d1_radialgradientbrush_gradientoriginoffset.htm) | Retrieves or sets the offset of the gradient origin relative to the gradient ellipse's center.  |
| [GradientStopCollection](sharpdx_direct2d1_radialgradientbrush_gradientstopcollection.htm) | Retrieves the [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.htm) associated with this radial gradient brush object. |
| [Opacity](sharpdx_direct2d1_brush_opacity.htm) | Gets or sets the degree of opacity of this brush.
 (Inherited from [Brush](sharpdx_direct2d1_brush.htm).) |
| [RadiusX](sharpdx_direct2d1_radialgradientbrush_radiusx.htm) | Retrieves or sets the x-radius of the gradient ellipse.  |
| [RadiusY](sharpdx_direct2d1_radialgradientbrush_radiusy.htm) | Retrieves or sets the y-radius of the gradient ellipse.  |
| [Transform](sharpdx_direct2d1_brush_transform.htm) | Gets or sets the transform applied to this brush.
 (Inherited from [Brush](sharpdx_direct2d1_brush.htm).) |






 
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
 
 
 



