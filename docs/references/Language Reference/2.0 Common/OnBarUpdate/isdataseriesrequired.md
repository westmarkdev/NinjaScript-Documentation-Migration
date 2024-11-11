---
title: IsDataSeriesRequired
pathName: isdataseriesrequired
parent: onbarupdate
section: references
status: review
---

## Definition

Determines if a Data Series is required for calculating this **NinjaScript** object. When set to false, data series related properties will not be displayed on the UI when configuring.

{% callout type="note" %}

When set to false, methods and properties which are dependent on Bars will NOT be used. This means you will not receive any calls to **OnBarUpdate()** or be able to access historical bar prices.

{% /callout %}

## Property Value

This property returns true if the **NinjaScript** requires a Data Series; otherwise, false. Default value is true.

{% callout type="warning" %}

Warning: This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**IsDataSeriesRequired**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsDataSeriesRequired = false;
    }
}
```
