










 


IsFirstBarOfSessionByIndex()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isfirstbarofsessionbyindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
IsFirstBarOfSessionByIndex() | [Previous page](isfirstbarofsession.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Indicates if the selected bar index value is the first bar of a trading session.


 


Property Value
--------------


This property returns true if the bar is the first bar of a session; otherwise, false.  This property is read-only.


 


Syntax
Bars.IsFirstBarOfSessionByIndex(int index)
-------------------------------------------------





|  |
| --- |
| Warning:   This property will always return false on non-intraday bar periods (e.g., Day, Month, etc) |



 


 


Parameters
----------




|  |  |
| --- | --- |
| index | An int representing an absolute bar index value |



 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
   //  loop through only the rendered bars on the chart 
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // check if the rendered bar is the first bar of the trading session
     if (Bars.IsFirstBarOfSessionByIndex(barIndex))
     {
         DateTime slotTimeAtBarIndex = chartControl.GetTimeBySlotIndex(barIndex);
         Print(string.Format("Bar index {0} was the first bar of the session at slot time {1}.", barIndex, slotTimeAtBarIndex));
     }
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
 
 
 



