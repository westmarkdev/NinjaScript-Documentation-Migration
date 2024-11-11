---
title: BarBrushes
pathName: barbrushes
parent: drawing
section: references
status: review
---

## Definition

A collection of historical brushes used for painting the color of a price bar's body.

## Property Value

A brush series type object. Accessing this property via an index value **int barsAgo** returns a **Brush** object representing the referenced bar's color.

{% callout type="note" %}

This will only return the color of a bar in which an explicit color overwrite was used. Otherwise it will return null.

{% /callout %}

## Syntax

**BarBrushes**

**BarBrushes[int barsAgo]**

{% callout type="warning" %}

You may have up to 65,535 unique BarBrushes instances, therefore, using **static predefined brushes** should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    // Sets the color of the current bar to blue.
    BarBrushes[0] = Brushes.Blue;

    // Sets the color of the previous bar to orange.
    BarBrushes[1] = Brushes.Orange;
}
```
