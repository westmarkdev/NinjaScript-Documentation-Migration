










 


AlertCallback()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?alertcallback.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Alert and Debug Concepts](alert_and_debug_concepts.htm) &gt;
AlertCallback() | [Previous page](alert_and_debug_concepts.htm)
[Return to chapter overview](alert_and_debug_concepts.htm)










Definition
----------


Creates an alert event to be raised specified by a string "id" and a corresponding .wav file will be played matching the "soundLocation" parameter. Once an alert has triggered, its message is reflected in the "Alerts Log" window based on the background and foreground brushes provided in the callback.   


 




|  |
| --- |
| Notes:  
1.If the AlertCallback() method is called again with the same string "id" parameter before the provided "rearmSeconds" duration has passed, the alert event will be reset based on the new "rearmSeconds" parameter provided.  Doing so could consequently cause an alert to be reset inadvertently, in which case you should pass a "rearmSeconds" parameter of "0" to ensure the specified alert event is always raised.2.The AlertCallback() method is the same core function used by the simpler [Alert()](alert.htm) method which can alternatively be used with NinjaScript indicators and strategies.  The AlertCallback() was exposed for use with Add-ons or other more advance use cases.  3.Providing a "rearmSeconds"  parameter greater than "0" will add the matching alert id to a rearmed state, which only allows the alert to be reissued after the specified time interval in seconds has lapsed.  You can reset an alert's rearm parameter by using the [ResetAlertRearmById()](alert_rearmalert().htm). |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


NinjaTrader.NinjaScript.Alert.AlertCallback(Instrument instrument, object source, string id, DateTime time, Priority priority, string message, string soundLocation, Brush backBrush, Brush foreBrush, int rearmSeconds)





|  |
| --- |
| Warning:  An "id" parameter MUST  be provided otherwise a null argument exception will be generated |



 


 


Parameters
----------




|  |  |
| --- | --- |
| instrument | An [Instrument](instrument.htm) object associated with the alert.   |
| source | A generic object type which created the alert (e.g. "this") |
| id | A string representing a unique id for the alert |
| time | The DateTime representing the time associated with the alert |
| priority | Sets the precedence of the alert in relation to other alerts.
 
Any one of the following values:
 
Priority.High
Priority.Low
Priority.Medium |
| message | A string representing the Alert message |
| soundLocation | A string representing the absolute file path of the .wav file to play.   |
| backBrush | Sets the background color of the Alerts window row for this alert when triggered ([reference](http://msdn.microsoft.com/en-us/library/system.drawing.color_members(v=vs.90).aspx)) |
| foreBrush | Sets the foreground color of the Alerts window row for this alert when triggered ([reference](http://msdn.microsoft.com/en-us/library/system.drawing.color_members(v=vs.90).aspx)) |
| rearmSeconds | An int which sets the number of seconds an alert will rearm.
 
Note: If the same alert (identified by the id parameter) is called within a time window of the time of last alert + rearmSeconds, the alert will be ignored. |



 


 




|  |
| --- |
| Tips: You can obtain the default NinjaTrader installation directory to access the sounds folder by using NinjaTrader.Core.Globals.InstallDir property.  Please see the example below for usage. |



 


 


Examples
--------




| ns |
| --- |
| NinjaTrader.NinjaScript.Alert.AlertCallback(NinjaTrader.Cbi.Instrument.GetInstrument("MSFT"), this, "someId", NinjaTrader.Core.Globals.Now, Priority.High, "message", NinjaTrader.Core.Globals.InstallDir+@"\sounds\Alert1.wav", new SolidColorBrush(Colors.Blue), new SolidColorBrush(Colors.White), 0); |






 
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
 
 
 



