










 


IncludeTradeHistoryInBacktest







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?includetradehistoryinbacktest.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IncludeTradeHistoryInBacktest | [Previous page](includecommission.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if the strategy will save orders, trades, and execution history. When this property is set to false you will see significant memory savings at the expense of having access to the detailed trading information.


 




|  |
| --- |
| Notes:  
•Since trade information is not stored you will only see entry/exit executions plotted on the chart with no connecting PnL trade lines.•This property is always defaulted to true, except when the strategy is running on the strategy tab. |



 


 


Property Value
--------------


This property returns true if the strategy will include trade history; otherwise, false. Default is set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.Configure (or State.SetDefaults when adding the script from the strategy tab) |



 


 


Syntax
------


IncludeTradeHistoryInBacktest


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Exclude trade history in a backtest to benefit from memory savings
         IncludeTradeHistoryInBacktest = false;
     }
}
 
protected override void OnBarUpdate()
{
   // Stop taking trades after 10 trades have been taken since the strategy was enabled
   if(SystemPerformance.AllTrades.Count &gt;= 10)
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
 
 
 



