










 


TradesPerformance







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradesperformance.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt;
TradesPerformance | [Previous page](losingtrades.htm)
[Return to chapter overview](tradecollection.htm)










Definition
----------


Performance profile of a [collection](tradecollection.htm) of [Trade](trade.htm) objects.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AverageBarsInTrade](averagebarsintrade.htm) | A double value representing the average number of bars per trade |
| [AverageEntryEfficiency](averageentryefficiency.htm) | A double value representing the average entry efficiency |
| [AverageExitEfficiency](averageexitefficiency.htm) | A double value representing the average exit efficiency |
| [AverageTimeInMarket](averagetimeinmarket.htm) | A [TimeSpan](http://msdn.microsoft.com/en-us/library/system.timespan.aspx) value representing quantity-weighted average duration of a trade |
| [AverageTotalEfficiency](averagetotalefficiency.htm) | A double value representing the average total efficiency |
| [TotalCommission](totalcommission.htm) | A double value representing the total commission |
| [Currency](currency.htm) | Gets a [TradesPerformanceValues](tradesperformancevalues.htm) object in currency |
| [GrossLoss](grossloss.htm) | A double value representing the gross loss |
| [GrossProfit](grossprofit.htm) | A double value representing the gross profit |
| [LongestFlatPeriod](longestflatperiod.htm) | A [TimeSpan](http://msdn2.microsoft.com/en-us/library/system.timespan.aspx) value representing longest duration of being flat |
| [MaxConsecutiveLoser](maxconsecutiveloser.htm) | An int value representing the maximum number of consecutive losses seen |
| [MaxConsecutiveWinner](maxconsecutivewinner.htm) | An int value representing the maximum number of consecutive winners seen |
| [MaxTime2Recover](maxtimetorecover.htm) | A [TimeSpan](http://msdn2.microsoft.com/en-us/library/system.timespan.aspx) value representing maximum time to recover from a draw down |
| [MonthlyStdDev](monthlystddev.htm) | A double value representing the monthly standard deviation |
| [MonthlyUlcer](monthlyulcer.htm) | A double value representing the monthly Ulcer index |
| [NetProfit](netprofit.htm) | A double value representing the net profit |
| [Percent](percent.htm) | Gets a [TradesPerformanceValues](tradesperformancevalues.htm) object in percent |
| [PerformanceMetrics](performancemetrics.htm) | An array of custom NinjaScript performance metrics |
| [Pips](pips.htm) | Gets a [TradesPerformanceValues](tradesperformancevalues.htm) object in pips |
| [Points](points.htm) | Gets a [TradesPerformanceValues](tradesperformancevalues.htm) object in points |
| [ProfitFactor](profitfactor.htm) | A double value representing the profit factor |
| [R2](rsquared.htm) | A double value representing the R-squared value |
| [RiskFreeReturn](riskfreereturn.htm) | A double value representing the risk free return rate |
| [SharpeRatio](sharperatio.htm) | A double value representing the Sharpe Ratio |
| [SortinoRatio](sortinoratio.htm) | A double value representing the Sortino Ratio |
| [Ticks](ticks.htm) | Gets a [TradesPerformanceValues](tradesperformancevalues.htm) object in ticks |
| [TotalQuantity](totalquantity.htm) | An int value representing the total quantity |
| [TotalSlippage](totalslippage.htm) | An double value representing the total slippage. This is presented in points, I.E. 0.25 for 1 execution on E-mini S&amp;P 500 Futures. |
| [TradesCount](tradescount.htm) | An int value representing the trades count |
| [TradesPerDay](tradesperday.htm) | An int value representing the avg trades per day |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
    // Only trade if you have less than 5 consecutive losers in a row
    if (SystemPerformance.RealTimeTrades.TradesPerformance.MaxConsecutiveLoser &lt; 5)
    {
        // Trade logic here
    }
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
 
 
 



