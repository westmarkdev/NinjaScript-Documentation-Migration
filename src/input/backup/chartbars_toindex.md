﻿










 


ToIndex







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_toindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
ToIndex | [Previous page](chartbars_tochartstring().htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


An index value representing the last bar rendered on the chart.  See also [FromIndex](chartbars_fromindex.htm).


 




|  |
| --- |
| Note:  This value is NOT the last value that exists on the [ChartBars](chartbars.htm), but rather the last bar index that is within the viewable range of the chart canvas area.  This value changes as the user interacts with the [ChartControl](chartcontrol.htm) time-scale (x-axis). |



 



Property Value
--------------


An int representing the last bar index painted on the chart


 


Syntax
------


ChartBars.ToIndex



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if (ChartBars != null)
   {
     // loop through all of the viewable range of the chart
     for (int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
     {
         // print the High value for each index within the viewable range
         Print(High.GetValueAt(barIndex));
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
 
 
 


