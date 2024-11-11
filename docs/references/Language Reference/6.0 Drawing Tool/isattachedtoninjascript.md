---
title: IsAttachedToNinjaScript
pathName: isattachedtoninjascript
parent: drawing_tools
status: imported
section: references
---

## Definition

Indicates if the drawing tool is currently **attached to** a NinjaScript object (such an indicator or a strategy).

## Property Value

A bool value which when true if the drawing tool is attached to a NinjaScript object; otherwise false. This property is read-only.

## Syntax

IsAttachedToNinjaScript

## Examples

```csharp
public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
    // do not interact if drawn by an indicator or strategy
    if (IsAttachedToNinjaScript)
        return;
}
```
