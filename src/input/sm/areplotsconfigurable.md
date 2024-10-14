










 


ArePlotsConfigurable







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?areplotsconfigurable.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddPlot()](addplot.htm) &gt;
ArePlotsConfigurable | [Previous page](addplot.htm)
[Return to chapter overview](addplot.htm)










Definition
----------


Determines if the plot(s) used in an indicator are configurable within the indicator dialog window.


 


Property Value
--------------


A bool which returns true if any indicator plot(s) are configurable; otherwise, false. Default set to true.


 


Syntax
------


ArePlotsConfigurable


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         AddPlot(Brushes.Orange, "SMA");
         ArePlotsConfigurable = false; // Plots are not configurable in the indicator dialog
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
 
 
 



