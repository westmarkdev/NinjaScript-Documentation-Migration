---
title: OnAuthorizeAccount()
pathName: onauthorizeaccount
parent: share_service
status: imported
section: references
---

## Definition

If the **IsAuthorizationRequired** property is set to true, this method will be called when the user clicks the Connect button in the Share Services dialogue under Tools -> **Options**. When this method is called, it will allow you to go through the handshake process for authorizing the account to a sharing service. For example, you can obtain user tokens for posting on their behalf to social networks using OAuth authentication.

Documentation on the OAuth handshake process can be found from the official OAuth website: [OAuth](http://oauth.net)

Specific documentation for the authorization process for a particular sharing service can be found on its public API resources located on their website.

## Method Return Value

An asynchronous [Task](https://msdn.microsoft.com/en-us/library/system.threading.tasks.task.aspx)

## Parameters

This method does not require any parameters.

## Syntax

This method is not required to be overridden. You may override the method in your Share Service with the following syntax if needed:

**public override async Task OnAuthorizeAccount()**

## Examples

```csharp
public override async Task OnAuthorizeAccount()
{
   //MyShareServicesToken() is a place holder for an actual API's token method
   string result = await MyShareServicesToken("myToken");

   // result is also a place holder
   if(result == "APIErrorCode123")
   {
     Print("Unable to authorize token");
     return;
   }

   // please see the your API's OUATH documentation for proper handshake usage
   else Print("Success!");
```
