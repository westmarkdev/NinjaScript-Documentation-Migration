---
title: IsLocked
pathName: islocked
parent: drawing_tools
status: imported
section: references
---

## Definition  

Determines if the drawing tool should be locked in place. This property can be set either manually through the UI or explicitly through code.

## Property Value

A bool value which when true indicates that the drawing tool is locked; otherwise false. Default is set to false.

{% callout type="note" %}

For Drawing tools which are drawn by an indicator or strategy, this property will default to true.

{% /callout %}

## Syntax

**IsLocked**

## Examples

```csharp
public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   if (IsLocked) //if the object is locked, do not attempt to move
     return;
```
