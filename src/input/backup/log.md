










 


Log()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?log.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
Log() | [Previous page](clearoutputwindow.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Generates a NinjaScript category log event record and associated time stamp which is output to the [Log](log_tab2.htm) tab of the NinjaTrader Control Center / Account Data windows. The Log() method also writes records to the NinjaTrader log file which can be useful for supporting 3rd party code.  


 




|  |
| --- |
| Notes:  
1.Log events do NOT process to the NinjaScript output window.  For temporary logging, please see the [Print()](print.htm) method and [Output window](output.htm).  2.The Log event time stamp represents the user configured Time zone from the Tools &gt; Options &gt; General category.  This setting could be different from the computer system's time zone. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


Log(string message, LogLevel logLevel)


 




|  |
| --- |
| Warning:  Each call to this method creates a log entry which takes memory to keep loaded in the Log tab of the Control Center. Excessive logging can result in huge portions of memory being allocated to display the log messages. Please see the NinjaScript section of the [Performance Tips](performance_tips2.htm) article for more information. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| message | A string value representing the message to be logged |
| logLevel | Sets the message level for the log event.  Different levels are color coded in the NinjaTrader log.
 
•LogLevel.Alert (also generates a pop-up notification window with log message)•LogLevel.Error•LogLevel.Information•LogLevel.Warning |



 



Examples
--------




| ns |
| --- |
| // Generates a log message
Log("This is a log message", LogLevel.Information);
 
// Generates a log message with a notification window
Log("This will generate a pop-up notification window as well", LogLevel.Alert); |






 
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
 
 
 



