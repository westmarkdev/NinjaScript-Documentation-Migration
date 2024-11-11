---
title: BackBrushAll
pathName: backbrushall
parent: drawing
section: references
status: review
---

## Definition

A collection of prior back brushes used for the background colors for all chart panels.

## Property Value

A Brush object that represents the color of the current chart bar.

{% callout type="note" %}

To reset the Chart background color to the default background color property, set the BackBrushAll to null for that bar.

{% /callout %}

## Syntax

BackBrushAll

{% callout type="warning" %}

You may have up to 65,535 unique BackBrushAll instances, therefore, using static predefined brushes should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Sets the back color to pale green
     BackBrushAll = Brushes.PaleGreen;

     // Sets the back color to null to use the default color set in the chart properties dialog window
     BackBrushAll = null;

     // Sets the back color to pink when the closing price is less than the 20 period SMA
     // and to lime green when above (see image below)
     BackBrushAll = SMA(20)[0] >= Close[0] ? Brushes.Pink : Brushes.PaleGreen;
}
```

![MAPriceBars2](mapricebars2.png)
