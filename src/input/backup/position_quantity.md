










 


Quantity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?position_quantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Position](position.htm) &gt;
Quantity | [Previous page](position_marketposition.htm)
[Return to chapter overview](position.htm)










Definition
----------


Gets the strategy's current position size.



Property Value
--------------


An int value representing the position size.



Syntax
------


Position.Quantity   

 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{ 
     // Prints out the current market position
     Print(Position.MarketPosition.ToString() + " " + Position.Quantity.ToString());
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
 
 
 



