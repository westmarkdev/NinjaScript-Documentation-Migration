










 


GetBar()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetBar() | [Previous page](getask.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the first bar that matches the time stamp of the "time" parameter provided.  


 




|  |
| --- |
| Note:  If the time parameter provided is older than the first bar in the series, a bar index of 0 is returned. If the time stamp is newer than the last bar in the series, the last absolute bar index is returned. |





Method Return Value
-------------------


An int value representing an absolute bar index value.


 


Syntax
Bars.GetBar(DateTime time)
---------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| time | Time stamp to be converted to an absolute bar index |



 


 


Examples
--------




| ns |
| --- |
| // Check that its past 9:45 AM
if (ToTime(Time[0]) &gt;= ToTime(9, 45, 00))
{
   // Calculate the bars ago value for the 9 AM bar for the current day
   int barsAgo = CurrentBar - Bars.GetBar(new DateTime(2006, 12, 18, 9, 0, 0));
 
   // Print out the 9 AM bar closing price
   Print("The close price on the 9 AM bar was: " + Close[barsAgo].ToString());
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
 
 
 



