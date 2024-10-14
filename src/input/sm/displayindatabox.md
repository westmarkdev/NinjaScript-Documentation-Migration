










 


DisplayInDataBox







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?displayindatabox.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
DisplayInDataBox | [Previous page](barsrequiredtoplot.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


Determines if plot(s) display in the chart data box.


 


Property Value
--------------


This property returns true if the indicator plot(s) values display in the chart data box; otherwise, false. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


DisplayInDataBox



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         DisplayInDataBox = false;   
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
 
 
 



