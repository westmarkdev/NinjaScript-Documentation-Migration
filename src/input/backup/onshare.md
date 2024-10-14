










 


OnShare()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onshare.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
OnShare() | [Previous page](onauthorizeaccount.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


This method is called when the user clicks OK on the Share window in NinjaTrader. This method can also be called by Alerts and general NinjaScript objects.



Method Return Value
-------------------


This method does not return a value


 


Parameters
----------




|  |  |
| --- | --- |
| text | The message being sent to the social network or other Share provider. This is what appears in the textbox of the Share window |
| imageFilePath | Optional path to screenshot or other image to be sent to the social network or other Share provider |




Syntax
------




|  |
| --- |
| You must override the method in your Share Service with the following syntax.
 
public override void OnShare(string text, string imageFilePath)
{
 
} |



 


Examples
--------




| ns |
| --- |
| public override void OnShare(string text, string imgFilePath)
{
 // place your share service logic here
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
 
 
 



