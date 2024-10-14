










 


AveragePrice







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?position_averageprice.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Position](position.htm) &gt;
AveragePrice | [Previous page](position.htm)
[Return to chapter overview](position.htm)










Definition
----------


Gets the average price of a strategy position.


 


Property Value
--------------


A double value representing the position's average price per unit.



Syntax
------


Position.AveragePrice


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Raise stop loss to breakeven when there is at least 10 ticks in profit
     if (Close[0] &gt;= Position.AveragePrice + 10 * TickSize)
         ExitLongStopMarket(Position.Quantity, Position.AveragePrice);
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
 
 
 



