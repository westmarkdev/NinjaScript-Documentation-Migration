










 


RearmAlert()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?alert_rearmalert().htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Alert and Debug Concepts](alert_and_debug_concepts.htm) &gt;
RearmAlert() | [Previous page](alertcallback.htm)
[Return to chapter overview](alert_and_debug_concepts.htm)










Definition
----------


Rearms an existing alert event by the string "id" parameter created via the [AlertCallback()](alertcallback.htm) method.  A NinjaScript generated alert by may need to be rearmed after the alert is triggered depending on the Alert()'s rearmSeconds parameter.


 




|  |
| --- |
| Note:  The NinjaScriptBase has a non-static method implemented with the same name.  Please see the [RearmAlert()](rearmalert.htm) method for Indicator or Strategies. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


NinjaTrader.NinjaScript.Alert.RearmAlert(string id)


 


 
Parameters
------------




|  |  |
| --- | --- |
| id | A unique string id representing an alert id to reset |




 


Examples
--------




| ns |
| --- |
| if (resetCondition) 
{
   NinjaTrader.NinjaScript.Alert.ResetAlertRearmById("someId");
   resetCondition = false;
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
 
 
 



