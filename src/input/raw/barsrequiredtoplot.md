










 


BarsRequiredToPlot







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsrequiredtoplot.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
BarsRequiredToPlot | [Previous page](plots.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


The number of bars on a chart required before the script plots. By default, the value is 20 bars.





|  |
| --- |
| Note:  This property is NOT the same as a minimum number of bars required to calculate the script values.  OnBarUpdate will always start calculating for the first bar on the chart (CurrentBar 0) |



 


 


Property Value
--------------


An int value that represents the minimum number of bars required.


 


Syntax
------


BarsRequiredToPlot



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          BarsRequiredToPlot = 10; // Do not plot until the 11th bar on the chart
          AddPlot(Brushes.Orange, "SMA");
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
 
 
 



