










 


RearmAlert()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rearmalert.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
RearmAlert() | [Previous page](printto.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Rearms an alert created via the [Alert()](alert.htm) method.  


 




|  |
| --- |
| Note:  A NinjaScript generated alert by may need to be rearmed after the alert is triggered depending on the Alert() methods rearmSeconds parameter. |



 


 


Method Return Value
-------------------


This method does not return a value.



Syntax
------


RearmAlert(string id)


 


Parameters
----------




|  |  |
| --- | --- |
| id | A unique string id representing an alert id to rearm |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   //rearms "myAlert" on each new trading session
   if(Bars.IsFirstBarOfSession)
     RearmAlert("myAlert");
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
 
 
 



