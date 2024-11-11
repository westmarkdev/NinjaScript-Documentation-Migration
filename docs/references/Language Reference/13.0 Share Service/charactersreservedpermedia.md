---
title: CharactersReservedPerMedia
pathName: charactersreservedpermedia
parent: share_service
status: imported
section: references
---

## Definition

Sets the number of characters allowed when attaching an image to ensure that character count is properly calculated.

{% callout type="note" %}

Social networks which limit the number of characters for each post, will have a defined number of characters that are reserved when an image or other media is attached.

{% /callout %}

## Property Value

A int value that represents the number of characters reserved when attaching an image or other media.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**CharactersReservedPerMedia**

## Examples

```csharp
protected override void OnStateChange()
{                     
    if (State == State.SetDefaults)
    {
        CharactersReservedPerMedia = 40;
    }
}
```
