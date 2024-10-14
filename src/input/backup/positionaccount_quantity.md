










 


Quantity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?positionaccount_quantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [PositionAccount](positionaccount.htm) &gt;
Quantity | [Previous page](positionaccount_marketposition.htm)
[Return to chapter overview](positionaccount.htm)










Definition
----------


Gets the current account's position size.



Property Value
--------------


An int value representing the account's position size.



Syntax
------


PositionAccount.Quantity   

 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{ 
     // Prints out the current market position
     Print(PositionAccount.MarketPosition.ToString() + " " + PositionAccount.Quantity.ToString());
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
 
 
 



