










 


PositionAccount







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?positionaccount.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
PositionAccount | [Previous page](position_quantity.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Represents position related information that pertains to real-world account (live or simulation).  


 




|  |
| --- |
| Tips:
•For multi-instrument scripts, please see [PositionsAccount](positionsaccount.htm) object which holds an array of all instrument positions managed by the strategy's account•For a Strategy Position, please see [Position](position.htm) |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Account | An [Account](account_class.htm) object which corresponds to the position |
| [AveragePrice](position_averageprice.htm) | Gets the average entry price of the account position |
| [GetUnrealizedProfitLoss()](position_getunrealizedprofitloss.htm) | Gets the unrealized PnL for the account |
| [Instrument](position_instrument.htm) | An [Instrument](instrument.htm) value representing the instrument of an order |
| [MarketPosition](position_marketposition.htm) | Gets the current market position of the account
 
Possible values:
MarketPosition.Flat
MarketPosition.Long
MarketPosition.Short |
| [Quantity](position_quantity.htm) | Gets the current account position size |
| ToString() | A string representation of an account position |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average entry price
     Print("The average entry price is " + PositionAccount.AveragePrice);
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
 
 
 



