










 


IsResetOnNewTradingDay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isresetonnewtradingday.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
IsResetOnNewTradingDay | [Previous page](islastbarofsession.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Indicates if the bars series is using the [Break EOD](break_at_eod.htm) data series property.  


 


Property Value
--------------


This property returns true if the bars series should reset on a new trading day; otherwise, false.  This property is read-only.


 


Syntax
Bars.IsResetOnNewTradingDay
----------------------------------





|  |
| --- |
| Tip: This property can be helpful in determine on how to amend new bar data when working with a [BarType](bars_type.htm) |





Examples
--------




| ns |
| --- |
| protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
   // create a session iterator to keep track of session related information
   if(SessionIterator == null)
     SessionIterator = new SessionIterator(bars);
 
   // determine if the bars are in a new session
   bool isNewSession = SessionIterator.IsNewSession(time, isBar);
 
   if(isNewSession)
     SessionIterator.GetNextSession(time, isBar);
 
   // If bars are using "Break end of day", add a new bar for next session
   if(bars.IsResetOnNewTradingDay &amp;&amp; isNewSession))
     AddBar(bars, open, high, low, close, time, volume);
   else
   {
     // do something with existing bar values
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
 
 
 



