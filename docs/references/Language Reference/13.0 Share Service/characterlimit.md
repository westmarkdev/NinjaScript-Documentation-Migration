---
title: CharacterLimit
pathName: characterlimit
parent: share_service
status: imported
section: references
---

## Definition

Determines the maximum number of characters the social network allows. Signature, text, and links all contribute to this character count displayed on the share window.

A value of **int.MaxValue** determines no practical limit and will make the character count not appear on the Share window.

## Property Value

A **int** value that represents the maximum number of characters the social network allows.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**CharacterLimit**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        CharacterLimit = 280;
    }
}
```
