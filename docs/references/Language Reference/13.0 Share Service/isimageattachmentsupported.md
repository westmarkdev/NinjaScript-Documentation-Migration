---
title: IsImageAttachmentSupported
pathName: isimageattachmentsupported
parent: share_service
status: imported
section: references
---

## Definition

Determines if the Share Service will allow for images as attachments.

## Property Value

A bool value when false, screenshots will be unable to be sent to the social network.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**IsImageAttachmentSupported**

## Examples

```csharp
protected override void OnStateChange()
{         
   if (State == State.SetDefaults)
   {
      IsImageAttachmentSupported = false;
   }
}
```
