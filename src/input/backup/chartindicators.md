










 


ChartIndicators







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartindicators.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
ChartIndicators | [Previous page](barssinceexitexecution.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Contains a collection of Indicators which have been added to the strategy instance using [AddChartIndicator()](addchartindicator.htm).



Property Value
--------------


An [Indicator](indicator.htm) object


 


Syntax
ChartIndicators[int index]
---------------------------------


 



Examples
--------




| ns |
| --- |
| if (State == State.DataLoaded)
{
   AddChartIndicator(SMA(20));
   
   // Set the plots color for the added indicator 
   ChartIndicators[0].Plots[0].Brush = Brushes.Blue;
   
   // Set the added indicator to panel 1 (specified index needs to be &gt;= 1)
   ChartIndicators[0].Panel = 1;
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
 
 
 



