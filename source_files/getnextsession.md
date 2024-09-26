










 


GetNextSession()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getnextsession.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
GetNextSession() | [Previous page](calculatetradingday.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Calculates the next available session relative to the "timeLocal" value used in the method's input.


 




|  |
| --- |
| Note:  This method needs to be used before you can accurately determine various session properties such as [ActualSessionBegin](actualsessionbegin.htm) or [ActualTradingDayEndLocal](actualtradingdayendlocal.htm), etc.   |



 


Property Value
--------------


A bool value when true indicates the method was able to successfully calculate the next trading session; otherwise false.


 




|  |
| --- |
| Warning:  This method is resource intensive and should ONLY be reserved for situations when calculations would be limited to a few specific use cases.  For example, calling this method for each bar in the OnBarUpdate() method would NOT be recommended.  |



 


 


Parameters
----------




|  |  |
| --- | --- |
| timeLocal | The DateTime value used to calculate the next trading day. |
| includesEndTimeStamp | A bool determining if a timestamp of <n>:00 should fall into the current session. (e.g., used for time based intraday series such as minute or second). |





Syntax
------


<sessioniterator>.GetNextSession(DateTime timeLocal, bool includesEndTimeStamp);




Example
-------




| ns Getting Next Session of the Primary Bars Object |
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
   }
} |



 


 




| ns Getting Next Session of a Secondary Time Series |
| --- |
| SessionIterator rthSessionIterator;
 
protected override void OnStateChange()
{
   if (State == State.Configure)
   {
     // add a 1440 minute bar using the RTH hours
     AddDataSeries(Instrument.FullName, new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1440 }, "CME US Index Futures RTH");
   }
 
   else if (State == State.Historical)
   {
     // store a session iterator built from the secondary (RTH) bars
     rthSessionIterator = new SessionIterator(BarsArray[1]);
   }
}
 
protected override void OnBarUpdate()
{
   // on the primary bars session, find the next trading session for the RTH bars
   if (Bars.IsFirstBarOfSession)
   {
     // use the current bar time to calculate the next RTH session
     rthSessionIterator.GetNextSession(Time[0], true);
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
 
 
 



</sessioniterator></n>