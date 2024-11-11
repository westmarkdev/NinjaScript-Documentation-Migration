---
section: references
title: RemoveDrawObjects()
pathName: removedrawobjects
parent: drawing
status: review
---

## Definition

Removes all draw objects originating from the indicator or strategy from the chart.

{% callout type="note" %}

This method will ONLY remove DrawObjects which were created by a NinjaScript object. User drawn objects CANNOT be removed from via NinjaScript.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**RemoveDrawObjects()**

## Examples

```csharp
// Removes all draw objects
RemoveDrawObjects();
```
