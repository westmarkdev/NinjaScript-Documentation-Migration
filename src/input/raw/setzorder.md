










 


SetZOrder







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?setzorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
SetZOrder | [Previous page](rendertarget.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Used to assign a unique identifier representing the index in which chart objects are drawn on the chart's Z-axis (front to back ordering). Objects with a higher ZOrder are drawn first.  


 




|  |
| --- |
| Note:  
 
1. To check on which ZOrder index the object gets drawn use the [ZOrder](chart_zorder.htm) property.
2. Assigning specific ZOrder indices to draw at should be done once the [State](onstatechange.htm) has reached State.Historical 
3. If you want to draw your object behind the bars, assign to use index -1 (like in the example below)
4. If you want to draw your object topmost, assign to use index int.MaxValue
5. Any levels in between can be directly assigned, the starting / default levels used by NinjaTrader can be seen [here](chart_zorder.htm).
6. You can see the highest ZOrder currently in a chart with code such our second example below - setting higher values than this value will result in the ZOrder to be set to this value, so this can be thought of as the current 'top'. |



 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


SetZOrder(int DesiredZOrderLevel)


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.Historical)
   {
       // Make sure our object plots behind the chart bars
       SetZOrder(-1);
   }
} |



 


 




| ns |
| --- |
| protected override void OnRender(ChartControl cc, ChartScale cs)
{
   Print(ChartPanel.ChartObjects.Max(co =&gt; co.ZOrder));
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
 
 
 



