










 


ToDay()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?today.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
ToDay() | [Previous page](ticksize.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Calculates an integer value representing a date.


 




|  |
| --- |
| Note:   Integer representation of day is format as yyyyMMdd where January 8, 2015 would be 20150108.  |



 


 


Method Return Value
-------------------


An int value representing date structure


 


Syntax
ToDay(DateTime time)
---------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| time | A DateTime structure to calculate Note:  See also the [Time](time.htm) property |



 


 




|  |
| --- |
| Tip:  NinjaScript uses the .NET [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structures which can be complicated for novice programmers. If you are familiar with C# you can directly use DateTime structure properties and methods for date and time comparisons otherwise use this method and the [ToTime()](totime.htm) method. |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   // Compare the date of the current bar to September 15, 2014
   if (ToDay(Time[0]) &gt; 20140915)
   {
       // Do something      
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
 
 
 



