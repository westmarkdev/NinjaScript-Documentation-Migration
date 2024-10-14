










 


AveragePrice







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?positionaccount_averageprice.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [PositionAccount](positionaccount.htm) &gt;
AveragePrice | [Previous page](positionaccount.htm)
[Return to chapter overview](positionaccount.htm)










Definition
----------


Gets the average price of an account position.


 


Property Value
--------------


A double value representing the account position's average price per unit.



Syntax
------


PositionAccount.AveragePrice


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Raise stop loss to breakeven when there is at least 10 ticks in profit
     if (Close[0] &gt;= PositionAccount.AveragePrice + 10 * TickSize)
         ExitLongStopMarket(PositionAccount.Quantity, PositionAccount.AveragePrice);
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
 
 
 



