---
title: "BarBrush"
pathName: /docs/desktop/barbrush
---

## Definition

Sets the brush used for painting the color of a price bar's body.

## Property Value

A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object that represents the color of this price bar.

{% callout type="tip" %}
To set the price bar color to an empty color which uses the default bar color property, set the BarBrush to null for that bar.
{% /callout %}

## Syntax

BarBrush

{% callout type="warning" %}
You may have up to 65,535 unique BarBrush instances, therefore, using [static predefined brushes](/docs/desktop/working_with_brushes) should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.
{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Sets the bar color to yellow
    BarBrush = Brushes.Yellow;
    // Sets the brush used for the bar color to its default color as defined in the chart properties dialog
    BarBrush = null;
    // Sets the bar color to yellow if the 20 SMA is above the 50 SMA and the closing
    // price is above the 20 SMA (see image below)
    if (SMA(20)[0] > SMA(50)[0] && Close[0] > SMA(20)[0])
        BarBrush = Brushes.Yellow;
}
```

