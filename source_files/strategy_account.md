










 


Account







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategy_account.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Account | [Previous page](strategy.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Represents the real-world or simulation Account configured for the strategy.


 


Property Value
--------------


An [Account](account_class.htm) object configured for the strategy



Syntax
------


Account



Examples
--------




| ns |
| --- |
| //Displays text on chart indicating what account the strategy is applied to
Draw.TextFixed(this, "tag1", "Strategy is applied to " + Account.Name, TextPosition.BottomRight); |






 
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
 
 
 



