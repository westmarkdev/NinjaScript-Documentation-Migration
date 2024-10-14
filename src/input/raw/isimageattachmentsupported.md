










 


IsImageAttachmentSupported







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isimageattachmentsupported.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
IsImageAttachmentSupported | [Previous page](isdefault.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


Determines if the Share Service will allow for images as attachments.



Property Value
--------------


A bool value when false, screenshots will be unable to be sent to the social network.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



  



Syntax
------


IsImageAttachmentSupported


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{         
   if (State == State.SetDefaults)
   {
      IsImageAttachmentSupported   = false;
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
 
 
 



