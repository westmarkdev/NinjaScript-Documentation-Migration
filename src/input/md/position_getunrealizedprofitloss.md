










 


GetUnrealizedProfitLoss()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?position_getunrealizedprofitloss.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Position](position.htm) &gt;
GetUnrealizedProfitLoss() | [Previous page](position_averageprice.htm)
[Return to chapter overview](position.htm)










Definition
----------


Calculates the unrealized PnL for the strategy position.



Method Return Value
-------------------


A double value representing the unrealized PnL.



Syntax
------


Position.GetUnrealizedProfitLoss(PerformanceUnit unit, [double price])


 




|  |
| --- |
| Note: 
•If no double argument is provided in the call, the current (real-time) Last price will be substituted in. In case Tools &gt; Options &gt; Trading &gt; 'Use last price for Pnl' is unchecked or the instrument type is Forex / CFD the bid (for a long position) / ask (for a short position) would be used as a substitute. •For back-testing a double price to compare against should be provided like in our example below. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| unit | Possible values:
PerformanceUnit.Currency
PerformanceUnit.Percent
PerformanceUnit.Pips
PerformanceUnit.Points
PerformanceUnit.Ticks |
| price | Optional price passed in used to calculate the PnL such as Close[0]. This value is used as the current price and compared against your entry price for the PnL. |



 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // If not flat print our unrealized PnL
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
 
 
 



