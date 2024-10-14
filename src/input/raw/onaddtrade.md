










 


OnAddTrade()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onaddtrade.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Performance Metrics](performance_metrics.htm) &gt;
OnAddTrade() | [Previous page](format.htm)
[Return to chapter overview](performance_metrics.htm)










Definition
----------


This method is called as each trade is added. You would add any custom math you wanted to do here.


 




|  |
| --- |
| Note: If your performance metric only needs to iterate through all trades at the end to perform its calculation and does not need to be calculated on each trade then using the [property approach](performancemetric_values.htm) (On demand example) will have less of a performance impact.  |



 


 


Syntax
------


protected override void OnAddTrade(Cbi.[Trade](trade.htm) trade)   

{


   

}



Examples
--------




| ns |
| --- |
| protected override void OnAddTrade(Cbi.Trade trade)
{
     Values[(int)Cbi.PerformanceUnit.Currency] += trade.ProfitCurrency;
     Values[(int)Cbi.PerformanceUnit.Percent]  += trade.ProfitPercent;
     Values[(int)Cbi.PerformanceUnit.Pips]     += trade.ProfitPips;
     Values[(int)Cbi.PerformanceUnit.Points]   += trade.ProfitPoints;
     Values[(int)Cbi.PerformanceUnit.Ticks]    += trade.ProfitTicks;
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
 
 
 



