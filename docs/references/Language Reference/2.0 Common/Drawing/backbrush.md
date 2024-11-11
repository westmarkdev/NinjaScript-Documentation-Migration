---
title: BackBrush
pathName: backbrush
parent: drawing
section: references
status: review
---

## Definition

Sets the brush used for painting the chart panel's background color for the current bar.

{% callout type="note" %}

This property will only set the back color for the panel the indicator is running. To set background color for all panels, please see the [BackBrushAll](backbrushall) property.

{% /callout %}

## Property Value

A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object that represents the color of the current chart bar.

## Syntax

**BackBrush**

{% callout type="warning" %}

You may have up to 65,535 unique **BackBrush** instances, therefore, using [static predefined brushes](working_with_brushes) should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Sets the chart panel back color to pale green
     BackBrush = Brushes.PaleGreen;

     // Sets the back color to to null which will use the default color set in the chart properties dialog window
     BackBrush = null;

     // Sets the back color to maroon when the closing price is less than the 20 period SMA // and to lime green when above (see image below)
     BackBrush = SMA(20)[0] >= Close[0] ? Brushes.Maroon : Brushes.LimeGreen;
}
```

![MAPriceBars](mapricebars.png)