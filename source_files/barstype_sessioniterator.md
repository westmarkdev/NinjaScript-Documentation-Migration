










 


SessionIterator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barstype_sessioniterator.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
SessionIterator | [Previous page](setpropertyname2.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Provides trading session information to the bars type.  Must be built using the bars object.


 


Property Value
--------------


A [SessionIterator](sessioniterator.htm) object which is used to to calculate trading day/session information.


 


Syntax
------


SessionIterator


 


Examples
--------




| ns |
| --- |
| protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
   // build a session iterator from the bars object being updated
   if (SessionIterator == null)
     SessionIterator = new SessionIterator(bars);
 
   // check if we are in a new trading session based on the trading hours selected by the user
   bool isNewSession = SessionIterator.IsNewSession(time, isBar);
 
   // calculate the new trading day
   if (isNewSession)
     SessionIterator.CalculateTradingDay(time, isBar);
 
   Print(SessionIterator.ActualTradingDayExchange);
 
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
 
 
 



