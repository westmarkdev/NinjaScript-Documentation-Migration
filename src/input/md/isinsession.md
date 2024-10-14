










 


IsInSession()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isinsession.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
IsInSession() | [Previous page](gettradingdayendlocal.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Indicates a specified date is within the bounds of the current session, according to the configured Trading Hours template.


 




|  |
| --- |
| Note:  Additionally this method will internally trigger a [GetNextSession()](getnextsession.htm) call to calculate the next available session relative to the "timeLocal" value used in the method's input. |



 


Property Value
--------------


A bool value when true indicates the specified time is within the current trading session; otherwise false.


 


Parameters
----------




|  |  |
| --- | --- |
| timeLocal | The DateTime value used to calculate the next trading day. |
| includesEndTimeStamp | A bool determining if a timestamp of <n>:00 should fall into the current session. (e.g., used for time based intraday series such as minute or second). |
| isIntraDay | A bool determining if IsInSession() considers the time of day (when true) or only the date (when false) |



 


 


Syntax
------


<sessioniterator>.IsInSession(DateTime timeLocal, bool includesEndTimeStamp, bool isIntraDay)


 



Example
-------




| ns |
| --- |
| private SessionIterator sessionIterator;
 
protected override void OnStateChange()
{
   if (State == State.Historical)
   {
       //stores the sessions once bars are ready, but before OnBarUpdate is called
       sessionIterator = new SessionIterator(Bars);
   }
}
 
protected override void OnBarUpdate()
{
   // Only place an order if the time three hours from now will still be within the current session
   if (sessionIterator.IsInSession(DateTime.Now.AddHours(3), true, true) /* &amp;&amp; additional conditions here */)
       EnterLongStopMarket(CurrentDayOHL().High[0] + TickSize);
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
 
 
 



</sessioniterator></n>