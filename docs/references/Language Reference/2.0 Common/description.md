---
title: Description
pathName: description
parent: common
section: references
status: review
---

## Definition

Text which is used on the UI's information box to be displayed to a user when configuring a **NinjaScript** object.

## Method Return Value

A **string** value representing text used to describe the object.

{% callout type="warning" %}

Warning: This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

Description

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
     Description = @"An indicator used to demonstrate various NinjaScript methods and properties";
   }
}
```
