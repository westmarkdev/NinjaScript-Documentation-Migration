---
title: "Share Service"
pathName: /docs/desktop/share_service
---

Custom Share Services can be developed in order to enable users to share content from the NinjaTrader application to various websites and social media networks via the [Sharing Services](/docs/desktop/sharing_content) dialog. NinjaTrader comes pre-configured with Share Services for an Email adapter and Test message via email adapter; however, a custom adapter can be developed for any website, forum, or social media network by following their public API documentation and guidelines.

## In this section

|  |  |
| --- | --- |
| [CharacterLimit](/docs/desktop/characterlimit) | Determines the maximum number of characters the social network allows. |
| [CharactersReservedPerMedia](/docs/desktop/charactersreservedpermedia) | Sets the number of characters allowed when attaching an image to ensure that character count is properly calculated. |
| [Icon](/docs/desktop/icon) | The shape which displays within the Share window when sharing content. |
| [UseOAuth](/docs/desktop/isauthorizationrequired) | If this property is set to true, a Connect button will appear in the dialogue for configuring the adapter that will call [OnAuthorizeAccount()](/docs/desktop/onauthorizeaccount) when the user clicks it. |
| [IsConfigured](/docs/desktop/isconfigured) | Sets when the Share Service is correctly configured. |
| [IsDefault](/docs/desktop/isdefault) | Sets the default Share Service used when the type of sharing service is selected (email for example). |
| [IsImageAttachmentSupported](/docs/desktop/isimageattachmentsupported) | Determines if the Share Service will allow for images as attachments. |
| [OnAuthorizeAccount()](/docs/desktop/onauthorizeaccount) | If the [UseOAuth](/docs/desktop/isauthorizationrequired) property is set to true, this method will be called when the user clicks the Connect button in the Share Services dialogue under Tools -> [Options](/docs/desktop/options). |
| [OnShare()](/docs/desktop/onshare) | This method is called when the user clicks OK on the Share window in NinjaTrader. This method can also be called by Alerts and general NinjaScript objects. |
| [Signature](/docs/desktop/signature) | Sets the text appended to the end of the user's message. |

