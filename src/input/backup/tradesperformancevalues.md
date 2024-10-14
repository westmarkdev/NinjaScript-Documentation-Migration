










 


TradesPerformanceValues







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradesperformancevalues.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
TradesPerformanceValues | [Previous page](winningtrades.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Performance values of a [collection](tradecollection.htm) of [Trade](trade.htm) objects.


 


•Currency and Point based calculations are per trade 

•Percent based calculations are per traded unit 

 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AverageEtd](averageetd.htm) | A double value representing avg end trade draw down |
| [AverageMae](averagemae.htm) | A double value representing avg maximum adverse excursion |
| [AverageMfe](averagemfe.htm) | A double value representing avg maximum favorable excursion |
| [AverageProfit](averageprofit.htm) | A double value representing avg profit |
| [CumProfit](cumprofit.htm) | A double value representing cumulative profit (percent is compounded) |
| [Drawdown](drawdown.htm) | A double value representing draw down |
| [LargestLoser](largestloser.htm) | A double value representing largest loss |
| [LargestWinner](largestwinner.htm) | A double value representing largest gain |
| [ProfitPerMonth](profitpermonth.htm) | A double value representing profit per month always as a percent |
| [StdDev](stddev.htm) | A double value representing standard deviation on a per unit basis |
| [Turnaround](turnaround.htm) | A double value representing the turnaround |
| [Ulcer](ulcer.htm) | A double value representing the Ulcer value |



 


 


Examples
--------





| ns |
| --- |
| protected override void OnBarUpdate()
{
     // If the profit on real-time trades is &gt; $1000 stop trading
     if (SystemPerformance.RealTimeTrades.TradesPerformance.Currency.CumProfit &gt; 1000)
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
 
 
 



