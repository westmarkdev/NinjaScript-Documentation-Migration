










 


ToTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?totime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
ToTime() | [Previous page](today.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Calculates an integer value representing a time.


 




|  |
| --- |
| Note:  Integer representation of time is in the format Hmmss where 7:30 AM would be 73000 and 2:15:12 PM would be 141512.  |



 


 


Method Return Value
-------------------


An int value representing a time structure


 


Syntax
ToTime(DateTime time)
ToTime(int hour, int minute, int second)
---------------------------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| time | A DateTime structure to calculate Note:  See also the [Time](time.htm) property |
| hour | An int value representing the hour used for the input |
| minute | An int value representing the minute used for the input |
| second | An int value representing the second used for the input |



 


 




|  |
| --- |
| Tip:  NinjaScript uses the .NET DateTime structure which can be complicated for novice programmers. If you are familiar with C# you can directly use DateTime structure properties and methods for date and time comparisons otherwise use this method and the [ToDay()](today.htm) method. |



 


 


Examples
--------




| ns |
| --- |
| // Only trade between 7:45 AM and 1:45 PM
if (ToTime(Time[0]) &gt;= 74500 &amp;&amp; ToTime(Time[0]) &lt;= 134500)
{
     // Strategy logic goes here
} |



 





|  |
| --- |
| ns |
| //store start time as an int variable to be compared
int startTime = ToTime(9, 30, 00); // 93000
 
//only trade after 9:30AM
if (ToTime(Time[0]) &gt;= startTime)
{
     // Strategy logic goes here
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
 
 
 



