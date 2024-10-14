










 


Line Class







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?line_class.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddLine()](addline.htm) &gt;
Line Class | [Previous page](arelinesconfigurable.htm)
[Return to chapter overview](addline.htm)










Definition
----------


Objects derived from the Line class are used to characterize how an oscillator line is visually displayed (plotted) on a chart.



 


Properties
----------




|  |  |
| --- | --- |
| Brush | The System.Windows.Media.Brush used to construct the line ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| BrushDX | A [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush.htm) used to actually render the line
 
Note:  To avoid and resolve access violation exceptions, please see Warning and examples remarked below |
| DashStyleDX | A [SharpDX.Direct2D1.DashStyle](sharpdx_direct2d1_strokestyle_dashstyle.htm) used to render the stroke style
 
Note:  To avoid and resolve access violation exceptions, please see Warning and examples remarked below |
| DashStyleHelper | A dashstyle used to construct the stroke. Possible values are:
 
•DashStyleHelper.Dash •DashStyleHelper.DashDot •DashStyleHelper.DashDotDot •DashStyleHelper.Dot •DashStyleHelper.Solid |
| Name | A string representing the name of the line |
| RenderTarget | The [RenderTarget](rendertarget.htm) drawing context used for the line. 
 
Note: This property must be set before accessing a stroke's BrushDX property. Please see Warning and examples remarked below |
| StrokeStyle | A [SharpDX.Direct2D1.StrokeStyle](sharpdx_direct2d1_strokestyle.htm) |
| Value | A double representing the value of the line |
| Width | A float representing the width in pixels |



 


 


Examples
--------


See the [AddLine(](addline.htm)) method for examples.





 
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
 
 
 



