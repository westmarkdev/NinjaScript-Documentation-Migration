










 


Share()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?share.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
Share() | [Previous page](sendmail.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Sends a message or screen shot to a social network or Share Service.  


 




|  |
| --- |
| Notes:  
1.This method can only be called once the [State](state.htm) has reached State.Realtime.  Calls to this method in any other State will be silently ignored.2.You MUST configure an account with a Share Service provider from the [General Options](general_section.htm) |



 


 


Method Return Value
-------------------


This method does not return a value.



Syntax
------


Share(string serviceName, string message)  

Share(string serviceName, string message, object[] args)  

Share(string serviceName, string message, string screenshotPath)  

Share(string serviceName, string message, string screenshotPath, object[] args)


 


Parameters
----------




|  |  |
| --- | --- |
| serviceName | A string value representing the share service to be used |
| message | A string value representing the text body sent to the social network or other Share providers. Note:  The message is what appears in the text box of the Share window |
| screenshotPath | Optional string path to screenshot or other images sent to the social network or other Share providers |
| args | A generic object[]  array used to designate additional information sent to the share service |



 


 




|  |
| --- |
| Tips:
1.The "args" parameter differs for each share service used.  If you are using a custom developed share adapter, you need to work with the developer of that adapter to understand what the "args" parameter represents for that adapter.2.For the default NinjaTrader share adapters, the "args" array represents the following: 
▪Mail share service:•args[0] = A string representing the email "To" field,•args[1] = A string representing the email "Subject" field 
▪StockTwits share service: •args[0] = An enum representing the "StockTwitsSentiment" parameter |



 


 


Examples
--------




| ns |
| --- |
| // using "args" as the Mail "To" and "Subject" parameters
Share("Gmail", "Test Message", new object[]{ "example@test.com", "Test Subject Line" }); |






 
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
 
 
 



