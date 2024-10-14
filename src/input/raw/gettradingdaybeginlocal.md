










 


GetTradingDayBeginLocal()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?gettradingdaybeginlocal.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
GetTradingDayBeginLocal() | [Previous page](gettradingday.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Converts the trading day begin time from the exchange timezone to local time, and returns a DateTime object in the local timezone. The [ActualTradingDayExchange](actualtradingdayexchange.htm) property can be passed into GetTradingDayBeginLocal() for a quick timezone conversion.


 


Property Value
--------------


A DateTime object representing the exchange-based trading day begin time converted to local time.


 


Syntax
------


<sessioniterator>.GetTradingDayBeginLocal(DateTime tradingDayExchange)



Parameters
----------




|  |  |
| --- | --- |
| tradingDayExchange | The DateTime value used to calculate the trading day. |




Example
-------




| ns |
| --- |
| private SessionIterator sessionIterator;
 
protected override void OnStateChange()
{
   if (State == State.DataLoaded)
   {
     //stores the sessions once bars are ready, but before OnBarUpdate is called
     sessionIterator = new SessionIterator(Bars);
   }
}
 
protected override void OnBarUpdate()
{
   // Only process strategy logic starting three hours after trading begins at the exchange
   if (Core.Globals.Now &gt;= sessionIterator.GetTradingDayBeginLocal(sessionIterator.ActualTradingDayExchange).AddHours(3))
   {
       // Strategy logic here
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