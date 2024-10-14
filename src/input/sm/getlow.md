










 


GetLow()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getlow.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetLow() | [Previous page](gethigh.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the low price at the selected bar index value.


 


Method Return Value
-------------------


A double value that represents the low price at the desired bar index.



Syntax
------


Bars.GetLow(int index)


 


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
   // loop through only the rendered bars on the chart
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the low price at the selected bar index value
     double lowPrice = Bars.GetLow(barIndex);
     Print("Bar #" + barIndex + " low price is " + lowPrice);
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
 
 
 



