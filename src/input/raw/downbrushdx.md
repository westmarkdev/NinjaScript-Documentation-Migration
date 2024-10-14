










 


DownBrushDX







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?downbrushdx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
DownBrushDX | [Previous page](downbrush.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


A SharpDX [Brush](sharpdx_direct2d1_brush.htm) object used to paint the down bars for the ChartStyle.


 


Property  Value
---------------


A [SharpDX](sharpdx_direct2d1.htm) Brush object used to paint the down bars


 


Syntax
------


DownBrushDX


 


Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)
{
   for (int idx = chartBars.FromIndex; idx &lt;= chartBars.ToIndex; idx++)
       {
           double     closeValue             = bars.GetClose(idx); 
           double     openValue               = bars.GetOpen(idx);
 
           // Set the brush of the current candle to UpBrushDX or DownBrushDX, depending on the 
           // bar direction
           Brush brush = closeValue &gt;= openValue ? UpBrushDX : DownBrushDX;
       }
} |






 
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
 
 
 



