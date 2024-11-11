---
title: IgnoresSnapping
pathName: ignoressnapping
parent: drawing_tools
status: imported
section: references
---

## Definition  

Determines if the drawing tool chart anchor's will use the chart's Snap Mode mouse coordinates.

## Property Value

A bool value which when true the drawing tool ignores snapping; otherwise false. Default is set to false.

## Syntax

**IgnoresSnapping**

## Examples

```csharp

protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          IgnoresSnapping = true; // Set this to true to receive non-snapped mouse coordinates
     }
     else if (State == State.Configure)
     {

     }
}
```
