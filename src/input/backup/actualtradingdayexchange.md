










 


ActualTradingDayExchange







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?actualtradingdayexchange.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
ActualTradingDayExchange | [Previous page](actualtradingdayendlocal.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Obtains the date of a trading session defined by the exchange.


 




|  |
| --- |
| Notes:
1.In order to obtain historical ActualTradingDayExchange information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object.2.The calculated value may differ from the current date as some trading sessions will begin before the actual calender date changes. For example, the "CME US Index Futures ETH" [actual session](accumulation_distribution_adl.htm) started on 3/30/2015 at 5:00PM Central Time, however the actual exchange trading day would be considered 3/31/2015 12:00:00AM |





Property Value
--------------


A DateTime structure that represents the trading day.


 


Syntax
------


<sessioniterator>.ActualTradingDayExchange



Example
-------




| ns |
| --- |
| SessionIterator sessionIterator;
 
protected override void OnStateChange()
{
   if (State == State.Historical)
   {
     sessionIterator = new SessionIterator(Bars);
   }
}
 
protected override void OnBarUpdate()
{
   // on new bars session, find the next trading session
   if (Bars.IsFirstBarOfSession)
   {
     // use the current bar time to calculate the next session
     sessionIterator.GetNextSession(Time[0], true);
 
     Print("The current exchange trading day is " + sessionIterator.ActualTradingDayExchange);
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
 
 
 



</sessioniterator>