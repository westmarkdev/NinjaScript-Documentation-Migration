---
title: BackBrushes
pathName: backbrushes
parent: drawing
section: references
status: review
---

## Definition

A collection of prior back brushes used for the background colors of the chart panel.

## Property Value

A brush series type object. Accessing this property via an index value **int barsAgo** returns a **Brush** object representing the color of the background color on the referenced bar.

## Syntax

**BackBrushes**

**BackBrushes[int barsAgo]**

{% callout type="warning" %}

You may have up to 65,535 unique BackBrushes instances, therefore, using [static predefined brushes](working_with_brushes) should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    // Sets the color of the background on the current bar as blue
    BackBrushes[0] = Brushes.Blue;

    // Sets the color of the background on the previous bar as orange
    BackBrushes[1] = Brushes.Orange;
}
```
