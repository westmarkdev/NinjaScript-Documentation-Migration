










 


MarketPosition







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?position_marketposition.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Position](position.htm) &gt;
MarketPosition | [Previous page](position_instrument.htm)
[Return to chapter overview](position.htm)










Definition
----------


Gets the strategy's current market position


 


Property Value
--------------


MarketPosition.Flat


MarketPosition.Long


MarketPosition.Short



Syntax
------


Position.MarketPosition  

 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{ 
     // If not flat print our open PnL
     if (Position.MarketPosition != MarketPosition.Flat) 
         Print("Open PnL: " + Position.GetUnrealizedProfitLoss(PerformanceUnit.Points, Close[0]));
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
 
 
 



