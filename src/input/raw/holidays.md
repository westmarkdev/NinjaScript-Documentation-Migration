










 


Holidays







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?holidays.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [TradingHours](tradinghours.htm) &gt;
Holidays | [Previous page](getprevioustradingdayend.htm)
[Return to chapter overview](tradinghours.htm)










Definition
----------


A collection of full holidays configured for a Trading Hours template. Holidays are days which fall outside of the regular trading schedule.


 




|  |
| --- |
| Note: For more information please see the "Understanding trading holidays" section of the [Using the Trading Hours](using_the_trading_hours_window.htm) window. |



 


 


Property Value
--------------


A [Dictionary](https://msdn.microsoft.com/en-us/library/xfhwa508(v=vs.110).aspx) holding a collection of holiday Dates and Descriptions of each holiday.


 




|  |  |
| --- | --- |
| Date | A DateTime representing the date of the trading hours holiday |
| Description | A string which is used to describe the holiday (e.g., Christmas) |



 


Syntax
------


TradingHours.Holidays


 


 


Examples
--------




| ns |
| --- |
| // Print all holidays included in the Bars object's Trading Hours template
foreach(KeyValuePair<datetime, string=""> holiday in TradingHours.Holidays)
{
   Print(holiday);
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
 
 
 



</datetime,>