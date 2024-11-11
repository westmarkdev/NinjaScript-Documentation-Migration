---
title: UseOAuth
pathName: useoauth
parent: share_service
status: changed
section: references
---

## Definition

If this property is set to true, a Connect button will appear in the dialogue for configuring the adapter that will call **OnAuthorizeAccount()** when the user clicks it.

## Property Value

A bool value determining if the **OnAuthorizeAccount()** method should be called in order to authorize the account to the social service.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults.

{% /callout %}

## Syntax

**UseOAuth**

## Examples

```csharp
protected override void OnStateChange()
{         
   if (State == State.SetDefaults)
   {
      UseOAuth = true;
   }
}
```
