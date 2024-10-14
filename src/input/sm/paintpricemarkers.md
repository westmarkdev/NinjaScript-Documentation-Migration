










 


PaintPriceMarkers







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?paintpricemarkers.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
PaintPriceMarkers | [Previous page](issuspendedwhileinactive.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


If true, any indicator plot values display price markers in the y-axis.


 


Property Value
--------------


This property returns true if the indicator plot values display in the y-axis; otherwise, false. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


PaintPriceMarkers


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         PaintPriceMarkers = true; // Indicator plots values display in the y-axis     
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
 
 
 



