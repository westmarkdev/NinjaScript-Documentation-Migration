










 


DrawVerticalGridLines







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawverticalgridlines.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
DrawVerticalGridLines | [Previous page](drawonpricepanel.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


Plots vertical grid lines on the indicator panel.





|  |
| --- |
| Note:  The indicator panel's parent chart has a similar option 'Grid line - vertical  which if Visible property set to false, will override the indicator's local setting if true. |



 


 


Property Value
--------------


This property returns true if vertical grid lines are plotted on the indicator panel; otherwise, false. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


DrawVerticalGridLines


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         DrawVerticalGridLines = false; // Vertical grid lines will not plot on the indicator panel     
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
 
 
 



