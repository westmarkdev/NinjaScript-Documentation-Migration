










 


IsWaitUntilFlat







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iswaituntilflat.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IsWaitUntilFlat | [Previous page](istradinghoursbreaklinevisible.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Indicates the strategy is currently waiting until a flat position is detected before submitting live orders. 


 




|  |
| --- |
| Note: This property would only apply if the strategy [StartBehavior](startbehavior.htm) was set to StartBehavior.WaitUntilFlat or StartBehavior.WaitUntilFlatSynchronizeAccount. |



 


Property Value
--------------


This property returns true if the strategy has detected it is either in a long or short position during [State.Transition](onstatechange.htm); otherwise false.  Default value is set to false.


 


Syntax
------


IsWaitUntilFlat


 



Examples
--------




|  |
| --- |
| ns |
| // If a strategy is waiting for a flat position, return and print a message
if (!IsWaitUntilFlat)
{ 
   Print("This strategy is currently waiting for a flat account position to begin placing trades");
   return;
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
 
 
 



