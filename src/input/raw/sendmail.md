










 


SendMail()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sendmail.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
SendMail() | [Previous page](rearmalert.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Sends an email message through the default email sharing service. 


 




|  |
| --- |
| Notes:  
1.This method can only be called once the [State](state.htm) has reached State.Realtime.  Calls to this method in any other State will be silently ignored (in contrast to the implementation for [AddOns](alert_and_debug_concepts.htm))2.You MUST configure an email account as a default "Mail" Share Service from the [General Options](general_section.htm) |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


SendMail(string to, string subject, string text)


 




|  |
| --- |
| Warning:  If mail is not received, please check the [Log](log_tab2.htm) tab of the control center for any specific errors which could be related to delivering the message.  |



 


 


Parameters
----------




|  |  |
| --- | --- |
| to | The email recipient  |
| subject | Subject line of email |
| text | Message body of email |



 



Examples
--------




| ns |
| --- |
| // Generates an email message
SendMail("customer@winners.com", "Trade Alert", "Buy ES"); |






 
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
 
 
 



