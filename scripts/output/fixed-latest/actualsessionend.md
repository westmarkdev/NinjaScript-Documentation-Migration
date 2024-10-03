










 


ActualSessionEnd







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?actualsessionend.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
ActualSessionEnd | [Previous page](actualsessionbegin.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Obtains the session's end date and end time converted to the user's configured Time Zone.


 




|  |
| --- |
| Note:  In order to obtain historical ActualSessionEnd information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object. |





Property Value
--------------


A DateTime structure that represents end of a trading session.


 


Syntax
------


<sessioniterator>.ActualSessionEnd



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
 
     Print("The current session end time is " + sessionIterator.ActualSessionEnd);
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