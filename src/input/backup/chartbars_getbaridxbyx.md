










 


GetBarIdxByX()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_getbaridxbyx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
GetBarIdxByX() | [Previous page](chartbars_getbaridxbytime.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


Returns the [ChartBars](chartbars.htm) index value at a specified x-coordinate relative to the ChartControl.


 


Method Return Value
-------------------


An int value representing the bar index



Syntax
ChartBars.GetBarIdxByX(ChartControl chartControl, int x)
---------------------------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | The [ChartControl](chartcontrol.htm) object used to determine the chart's time axis |
| x | The x-coordinate used to find a bar index value |





Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // get the users mouse down point and convert to device pixels for DPI accuracy
   int mousePoint = chartControl.MouseDownPoint.X.ConvertToHorizontalPixels(chartControl.PresentationSource);
   
   // convert mouse point to bar index
   int barIdx = ChartBars.GetBarIdxByX(chartControl, mousePoint);
   
   Print("User clicked on Bar #" + barIdx);
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
 
 
 



