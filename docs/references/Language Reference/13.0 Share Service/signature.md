---
title: Signature
pathName: signature
parent: share_service
status: imported
section: references
---

## Definition

Sets the text appended to the end of the user's message. It is uneditable by the user, and contributes to the character count of the overall message.

You can set it to an empty string if it does not apply to your adapter. In that case, the Signature label will not appear in the Share window.

## Property Value

A **string** value which is appended to the end of the user's message.

## Syntax

**Signature**

## Examples

```csharp
//example #1**, adds text "This message was sent from NinjaTrader" at the end of the message.
protected override void OnStateChange()
{
   if (State == State.SetDefaults)

   {

      Signature   = "This message was sent from NinjaTrader";

   }

}

```

```csharp
//example #2**, uses an empty string which does not add any additional text to the message
protected override void OnStateChange()
{         
   if (State == State.SetDefaults)
   {
      Signature   = string.Empty;
   }
}
```
