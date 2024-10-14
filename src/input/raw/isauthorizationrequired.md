










 


UseOAuth
========






| --- | --- |
| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isauthorizationrequired.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
UseOAuth  | [Previous page](icon.htm)
[Next page](isconfigured.htm) |










Definition
----------


If this property is set to true, a Connect button will appear in the dialogue for configuring the adapter that will call [OnAuthorizeAccount()](onauthorizeaccount.htm) when the user clicks it.



Property Value
--------------


A bool value determining if the OnAuthorizeAccount() method should be called in order to authorize the account to the social service.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults |



 


Syntax
------


UseOAuth


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{         
   if (State == State.SetDefaults)
   {
      UseOAuth   = true;
   }
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
 
 
 



