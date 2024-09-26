










 


Share Service







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?share_service.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Share Service | [Previous page](performancemetric_values.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Share Services can be developed in order to enable users to share content from the NinjaTrader application to various websites and social media networks via the [Sharing Services](sharing_content.htm) dialog. NinjaTrader comes pre-configured with Share Services for an Email adapter and Test message via email adapter, however a custom adapter can be developed for any website, forum, or social media network by following their public API documentation and guidelines.  


 


In this section
---------------




|  |  |
| --- | --- |
| [CharacterLimit](characterlimit.htm) | Determines the maximum number of characters the social network allows. |
| [CharactersReservedPerMedia](charactersreservedpermedia.htm) | Sets the number of characters allowed when attaching an image to ensure that character count is properly calculated. |
| [Icon](icon.htm) | The shape which displays within the Share window when sharing content. |
| [UseOAuth](isauthorizationrequired.htm) | If this property is set to true, a Connect button will appear in the dialogue for configuring the adapter that will call [OnAuthorizeAccount()](onauthorizeaccount.htm) when the user clicks it. |
| [IsConfigured](isconfigured.htm) | Sets when the Share Service is correctly configured. |
| [IsDefault](isdefault.htm) | Sets the default Share Service used when the type of sharing service is selected (email for example). |
| [IsImageAttachmentSupported](isimageattachmentsupported.htm) | Determines if the Share Service will allow for images as attachments. |
| [OnAuthorizeAccount()](onauthorizeaccount.htm) | If the [UseOAuth](isauthorizationrequired.htm) property is set to true, this method will be called when the user clicks the Connect button in the Share Services dialogue under Tools -&gt; [Options](options.htm). |
| [OnShare()](onshare.htm) | This method is called when the user clicks OK on the Share window in NinjaTrader. This method can also be called by Alerts and general NinjaScript objects. |
| [Signature](signature.htm) | Sets the text appended to the end of the user's message. |






 
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
 
 
 



