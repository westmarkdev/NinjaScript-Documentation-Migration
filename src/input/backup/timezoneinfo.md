










 


TimeZoneInfo







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?timezoneinfo.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [TradingHours](tradinghours.htm) &gt;
TimeZoneInfo | [Previous page](tradinghours_sessions.htm)
[Return to chapter overview](tradinghours.htm)










Definition
----------


Indicates a time zone that is configured by a Trading Hours template  

 


Property Value
--------------


A [TimeZoneInfo](https://msdn.microsoft.com/en-us/library/system.timezoneinfo(v=vs.110).aspx) object the represents the time zone for a configured Trading Hours template.


 


Syntax
Bars.TradingHours.TimeZoneInfo
-------------------------------------


 


Examples
--------




| ns |
| --- |
| // Print the timezone before printing all sessions
Print(String.Format("All sessions are in {0}", Bars.TradingHours.TimeZoneInfo));
 
// Print details for all sessions in the Trading Hours template
for (int i = 0; i &lt; TradingHours.Sessions.Count; i++)
{
   Print(String.Format("Session {0}: {1} at {2} to {3} at {4}", i, TradingHours.Sessions[i].BeginDay, TradingHours.Sessions[i].BeginTime,
     TradingHours.Sessions[i].EndDay, TradingHours.Sessions[i].EndTime));
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
 
 
 



