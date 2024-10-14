










 


OnAuthorizeAccount()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onauthorizeaccount.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
OnAuthorizeAccount() | [Previous page](isimageattachmentsupported.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


If the [IsAuthorizationRequired](isauthorizationrequired.htm) property is set to true, this method will be called when the user clicks the Connect button in the Share Services dialogue under Tools -&gt; [Options](options.htm).  When this method is called, it will allow you go through the handshake process for authorizing the account to a sharing service.  For example, you can obtain user tokens for posting on their behalf to social networks using OAuth authentication.   


 


Documentation on the OAuth handshake process can be found from the official OAuth website: <http: code="" oauth.net=""></http:> 


 


Specific documentation for the authorization process for a particular sharing service can be found on it's public API resources located on their website.  



Method Return Value
-------------------


An asynchronous [Task](https://msdn.microsoft.com/en-us/library/system.threading.tasks.task.aspx)


 


Parameters
----------


This method does not require any parameters



Syntax
------


This method is not required to be overridden.  You may override the method in your Share Service with the following syntax if needed:


 


public override async Task OnAuthorizeAccount()  

{  

   

}


 


Examples
--------




| ns |
| --- |
| public override async Task OnAuthorizeAccount()
{
   //MyShareServicesToken() is a place holder for an actual API's token method
   string result = await MyShareServicesToken("myToken");
   
   // result is also a place holder
   if(result == "APIErrorCode123")
   {
     Print("Unable to authorize token");
     return;
   }
   
   // please see the your API's OUATH documenation for proper handshake usage
   else Print("Success!");
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
 
 
 



