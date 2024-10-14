










 


Alert()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?alert.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
Alert() | [Previous page](alert__debugging_and_sharing.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Generates a visual/audible alert to display in the [Alerts Log](alerts_log.htm) window.


 




|  |
| --- |
| Notes: 
1. This method can only be called once the [State](state.htm) has reached State.Realtime.  Calls to this method in any other State will be silently ignored.2. For add-ons, please see the [AlertCallback()](alertcallback.htm) method |



 


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
Alert(string id, Priority priority, string message, string soundLocation, int rearmSeconds, Brush backBrush, Brush foreColor)
------------------------------------------------------------------------------------------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| id | A string representing a unique id for the alert |
| priority | Sets the precedence of the alert in relation to other alerts
 
Possible values include:
 
Priority.High
Priority.Low
Priority.Medium |
| message | A string representing the Alert message |
| soundLocation | A string representing the absolute file path of the .wav file to play |
| rearmSeconds | An int which sets the number of seconds an alert rearms. Note: If the same alert (identified by the id parameter) is called within a time window of the time of last alert + rearmSeconds, the alert will be ignored |
| backBrush | Sets the background color of the Alerts window row for this alert when triggered ([reference](http://msdn.microsoft.com/en-us/library/system.drawing.color_members(v=vs.90).aspx)) |
| foreBrush | Sets the foreground color of the Alerts window row for this alert when triggered ([reference](http://msdn.microsoft.com/en-us/library/system.drawing.color_members(v=vs.90).aspx)) |



 


 




|  |
| --- |
| Tip: You can obtain the default NinjaTrader installation directory to access the sounds folder by using NinjaTrader.Core.Globals.InstallDir property.  Please see the example below for usage. |



 


 


Example
-------




| ns |
| --- |
| protected override void OnBarUpdate()
{         
   // Generate an alert when the RSI value is greater or equal to 20
   if(RSI(14, 3)[0] &gt;= 20)
     Alert("myAlert", Priority.High, "Reached threshold", NinjaTrader.Core.Globals.InstallDir+@"\sounds\Alert1.wav", 10, Brushes.Black, Brushes.Yellow);                   
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
 
 
 



