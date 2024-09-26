










 


IsNewSession()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isnewsession.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SessionIterator](sessioniterator.htm) &gt;
IsNewSession() | [Previous page](isinsession.htm)
[Return to chapter overview](sessioniterator.htm)










Definition
----------


Indicates a specified time is greater than the [ActualSessionEnd](actualsessionend.htm) property on the configured Trading Hours template.


 


Property Value
--------------


A bool value when true indicates the specified time is later than ActualSessionEnd; otherwise false.


 


 


Parameters
----------




|  |  |
| --- | --- |
| time | The DateTime value used to compare |
| includesEndTimeStamp | A bool determining if a timestamp of <n>:00 should fall into the current session. (e.g., used for time based intraday series such as minute or second). |



 


 


Syntax
------


<sessioniterator>.IsNewSession(DateTime time, bool includesEndTimeStamp)


 



Example
-------




| ns |
| --- |
| bool takeTrades;
 
protected override void OnBarUpdate()
{
   // Switch a bool named takeTrades to false when IsNewSession() returns true. 
   if (Bars.SessionIterator.IsNewSession(DateTime.Now, true)) ;
   {
       Alert("EOS", Priority.Medium, String.Format("New session beginning. Waiting until {0} to begin trading again"), " ", 5, Brushes.Black, Brushes.White);
       takeTrades = false;
   }
 
   // Set the bool back to true on the first bar of the new session
   if (Bars.IsFirstBarOfSession)
       takeTrades = true;
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