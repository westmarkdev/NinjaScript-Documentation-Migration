---
title: DrawnBy
pathName: drawnby
parent: drawing_tools
section: references
status: imported
---

## Definition

Represents the **NinjaScript** object which created the drawing object.

## Property Value

The **NinjaScript** object which created the drawing tool; this value will be null if drawn by a user.

## Syntax

**DrawnBy**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{       
    // if the drawing tool was not created by a user, 
    // print the name of the object that it was created       
    if(!IsUserDrawn)
        Print(DrawnBy.Name);
}
```
