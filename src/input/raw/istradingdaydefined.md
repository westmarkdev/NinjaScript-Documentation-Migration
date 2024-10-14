










 


IsTradingDayDefined()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?istradingdaydefined.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
IsTradingDayDefined() | [Previous page](isnewsession.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Indicates a trading day is defined for a specific date.


 


Property Value
--------------


A bool value when true indicates that the date passed in as an argument is defined as a full or partial trading day in the configured Trading Hours template; otherwise false. Also returns false if the specified date is marked as a full-day exchange holiday. 


 


 


Parameters
----------




|  |  |
| --- | --- |
| date | The DateTime value representing the date to check |



 


 


Syntax
------


<sessioniterator>.IsTradingDayDefined(DateTime time);


 



Example
-------




| ns |
| --- |
| DateTime thanksGivingDay = new DateTime(2017, 11, 23);
 
// Determine if the current instrument's exchange is open for trading on Thanksgiving day in 2017
if(Bars.SessionIterator.IsTradingDayDefined(thanksGivingDay))
   Print(String.Format("{0} will be open for trading on Thanksgiving day, {1}", Instrument.MasterInstrument.Name, thanksGivingDay.Date));  |






 
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