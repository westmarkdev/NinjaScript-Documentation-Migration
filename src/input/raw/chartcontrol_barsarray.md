










 


BarsArray







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_barsarray.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarsArray | [Previous page](barmarginleft.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Provides a collection of [ChartBars](chartbars.htm) objects currently configured on the chart. 



Property Value
--------------


An [ObservableCollection](https://msdn.microsoft.com/en-us/library/ms668604(v=vs.110).aspx) of ChartBars objects



Syntax
------


<chartcontrol>.BarsArray



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Instantiate a new <chartcontrol>.BarsArray collection
   System.Collections.ObjectModel.ObservableCollection<chartbars> myChartBars = chartControl.BarsArray;
 
   // Print the number of bars in each Bars object within the <chartcontrol>.BarsArray collection
   foreach(ChartBars bars in myChartBars)
   {
       Print(bars.Bars.Count);
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
 
 
 



</chartcontrol></chartbars></chartcontrol></chartcontrol>