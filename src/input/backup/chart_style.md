










 


Chart Style







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chart_style.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Chart Style | [Previous page](updatebar.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Chart Styles can be used on charts to present bars information in a different visual representation. The methods and properties covered in this section are unique to custom Chart Style development. Following is an index of properties and methods documented for Chart Styles.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [BarWidth](barwidth.htm) | The painted width of a ChartStyle bar |
| [BarWidthUI](barwidthui.htm) | The Bar width value which displays on the UI |
| [ChartStyleType](chartstyletype.htm) | Defines a unique identifier value used to register a custom ChartStyle |
| [DownBrush](downbrush.htm) | A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the down bars for the ChartStyle |
| [DownBrushDX](downbrushdx.htm) | A [SharpDX.Brush](sharpdx_direct2d1_brush.htm) object used to paint the down bars for the ChartStyle |
| [GetBarPaintWidth()](getbarpaintwidth.htm) | Returns the painted width of the chart bar |
| [IsTransparent](istransparent.htm) | Indicates the bars in the ChartStyle are transparent |
| [OnRender()](chartstyle_onrender.htm) | An event driven method used to render content to a ChartStyle |
| [SetPropertyName()](setpropertyname.htm) | Sets a default property name to a custom string to be displayed on the UI |
| [TransformBrush()](transformbrush.htm) | Scales a non-solid color brush used for rendering the chart style to properly display in NinjaTrader |
| [UpBrush](upbrush.htm) | A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the up bars for the ChartStyle |
| [UpBrushDX](upbrushdx.htm) | A [SharpDX.Brush](sharpdx_direct2d1_brush.htm) object used to paint the up bars for the ChartStyle |






 
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
 
 
 



