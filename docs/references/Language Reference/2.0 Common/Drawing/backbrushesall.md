---
title: BackBrushesAll
pathName: backbrushesall
parent: drawing
section: references
status: review
---

## Definition

A collection of historical brushes used for the background colors for all chart panels.

## Property Value

A brush series type object. Accessing this property via an index value [int barsAgo] returns a **Brush** object representing the color of the background color on the referenced bar for all chart panels.

## Syntax

**BackBrushesAll**  

**BackBrushesAll[int barsAgo]**

{% callout type="warning" %}

You may have up to 65,535 unique BackBrushAll instances, therefore, using **static predefined brushes** should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    // Sets the color of the background on the current bar as blue on all chart panels.
    BackBrushesAll[0] = Brushes.Blue;

    // Sets the color of the background on the previous bar as orange on all chart panels.
    BackBrushesAll[1] = Brushes.Orange;
}
```
