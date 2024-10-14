










 


PartialHolidays







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?partialholidays.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [TradingHours](tradinghours.htm) &gt;
PartialHolidays | [Previous page](tradinghours_name.htm)
[Return to chapter overview](tradinghours.htm)










Definition
----------


A collection of partial holidays which are configured for a Trading Hours template. Holidays are days which fall outside of the normal trading schedule, on which data will be excluded. For more information please see the "Understanding trading holidays" section of the [Using the Trading Hours](using_the_trading_hours_window.htm) window.


 


Property Value
--------------


A [Dictionary](https://msdn.microsoft.com/en-us/library/xfhwa508(v=vs.110).aspx) holding a collection of holiday Dates and PartialHoliday objects for each partial holiday.


 




|  |  |
| --- | --- |
| Date | A DateTime representing the trading date of the Trading Hours holiday |
| PartialHoliday | An object containing a DateTime representing the date of the early close or late begin, a description of the partial holiday, and two bool properties, IsEarlyClose and IsLateBegin |



 


Syntax
------


TradingHours.PartialHolidays


 


 


Examples
--------




| ns |
| --- |
| // Print all partial holidays included in the Bars object's Trading Hours template
foreach(KeyValuePair<datetime, partialholiday=""> holiday in TradingHours.PartialHolidays)
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