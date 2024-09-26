










 


GetPreviousTradingDayEnd()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getprevioustradingdayend.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [TradingHours](tradinghours.htm) &gt;
GetPreviousTradingDayEnd() | [Previous page](tradinghoursget.htm)
[Return to chapter overview](tradinghours.htm)










Definition
----------


Returns the end date and time of the previous trading session regarding the time passed in the methods parameters.


 


Method Return Value
-------------------


A DateTime structure representing the previous trading days end date and time


 


Syntax
------


GetPreviousTradingDayEnd(DateTime timeLocal)


 




|  |
| --- |
| Warning:  This method is resource intensive and should ONLY be reserved for situations when calculations would be limited to a few specific use cases.  For example, calling this method for each bar in the OnBarUpdate() method would NOT be recommended.  |



 


 
Parameters
------------




|  |  |
| --- | --- |
| timeLocal | An DateTime structure which is used to calculate the current trading day |




 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   if (Bars.IsFirstBarOfSession)
   {
     DateTime previousEndDate = TradingHours.GetPreviousTradingDayEnd(Time[0]);
 
     Print(string.Format("The current bars date is {0} - the previous trading session ended on {1}", Time[0], previousEndDate));
   }
   //Output:  The current bars date is 2/18/2015 12:35:00 PM - the previous trading session ended on 2/17/2015 3:15:00 PM
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
 
 
 



