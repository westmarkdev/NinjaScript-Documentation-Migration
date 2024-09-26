










 


ActualTradingDayEndLocal







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?actualtradingdayendlocal.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
ActualTradingDayEndLocal | [Previous page](actualsessionend.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Returns the session's End-Of-Day (EOD) in the user's configured timezone.


 




|  |
| --- |
| Note:  In order to obtain historical ActualTradingDayEndLocal information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object. |





Property Value
--------------


A DateTime structure that represents end of a trading day (EOD).


 


Syntax
------


<sessioniterator>.ActualTradingDayEndLocal



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
 
     Print("The current session end of day is " + sessionIterator.ActualTradingDayEndLocal);
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