










 


IsConfigured







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isconfigured.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
IsConfigured | [Previous page](isauthorizationrequired.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


Sets when the Share Service is correctly configured.  Typically this would be set after the account is authorized, at which point the adapter will allow for the user to share content to the sharing service.     


 




|  |
| --- |
| Note:  It is not required for a Share Service to authorize a user, therefore it is possible to set IsConfigured to true in State.SetDefaults which will bypass any sort of authorization or additional setup that may be needed for the share adapter.   |



 



Property Value
--------------


A bool value when true determines if the Share Adapter is properly configured. 


 


Syntax
------


IsConfigured


 



Examples
--------




| ns |
| --- |
| public override void OnAuthorizeAccount()
{
   //Authorization logic would be here, after success, set IsConfigured to true.
 
   IsConfigured = true;
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
 
 
 



