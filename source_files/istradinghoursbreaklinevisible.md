










 


IsTradingHoursBreakLineVisible







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?istradinghoursbreaklinevisible.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IsTradingHoursBreakLineVisible | [Previous page](isinstrategyanalyer.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Plots trading hours break lines on the indicator panel.





|  |
| --- |
| Note:  The indicator panel's parent chart has a similar property 'Plot session break line' which if set to false, will override the indicator's local setting if true. |



 


 


Property Value
--------------


This property returns true if trading hours break lines are plotted on the indicator panel; otherwise, false. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IsTradingHoursBreakLineVisible


 


 


Examples
--------




| ns |
| --- |
|  | protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         IsTradingHoursBreakLineVisible = true;     
         AddPlot(Brushes.Orange, "SMA");
     }
}    |






 
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
 
 
 



