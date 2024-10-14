










 


GetTrades()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?gettrades.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt;
GetTrades() | [Previous page](eventrades.htm)
[Return to chapter overview](tradecollection.htm)










Definition
----------


Returns a TradeCollection object representing all trades that make up the specified position. 


 


Method Return Value
-------------------


A TradeCollection object.


 


Syntax
<tradecollection>.GetTrades(string instrument, string entrySignalName, int instance)
-------------------------------------------------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| instrument | An instrument name such as "MSFT" |
| entrySignalName | The name of your entry signal |
| instance | The occurrence to check for (1 is the most recent, 2 is the 2nd most recent position, etc...) |



 


   

Examples




| ns |
| --- |
| protected override void OnBarUpdate()
{
     TradeCollection myTrades = SystemPerformance.AllTrades.GetTrades("MSFT", "myEntrySignal", 1);
     Print("The last position was comprised of " + myTrades.Count + " trades.");
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
 
 
 



</tradecollection>