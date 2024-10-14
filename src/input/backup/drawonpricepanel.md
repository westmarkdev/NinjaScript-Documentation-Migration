










 


DrawOnPricePanel







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawonpricepanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
DrawOnPricePanel | [Previous page](drawhorizontalgridlines.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


Determines the chart panel the draw objects renders


 


Property Value
--------------


This property returns true if the indicator paints draw objects on the price panel; otherwise when false, draw objects are painted on the actual indicator panel itself. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY be set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults. Dynamically using DrawOnPricePanel in an indicator outside of State.SetDefaults may show issues when working with that indicator through a hosting strategy via [AddChartIndicator()](addchartindicator.htm). |



 


Syntax
------


DrawOnPricePanel


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          DrawOnPricePanel = false; // Draw objects now paint on the indicator panel itself    
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
 
 
 



