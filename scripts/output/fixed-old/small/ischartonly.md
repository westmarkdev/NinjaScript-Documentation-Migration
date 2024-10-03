---
path: ischartonly
title: IsChartOnly
---

## Definition

If true, any indicator will be only available for charting usage - indicators with this property enabled would for example not be expected to show if called in a SuperDOM or MarketAnalyzer window.

## Property Value

This property returns true if the indicator can only be used on a chart; otherwise, false. Default set to false.

{% callout type="warning" %}
This property should ONLY bet set from the [OnStateChange()](onstatechange) method during State.SetDefaults or State.Configure

{% /callout %}

## Syntax

`IsChartOnly`

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsChartOnly = true; // Allow the indicator to work in charting environment only
    }
}
```
