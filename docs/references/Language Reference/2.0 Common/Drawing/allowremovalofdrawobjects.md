---
title: AllowRemovalOfDrawObjects
pathName: allowremovalofdrawobjects
parent: drawing
section: references
status: review
---

## Definition

Determines if programmatically drawn **DrawObjects** are allowed to remove manually from the chart

### Property Value

When set to true, the draw objects from the indicator or strategy can be deleted from the chart manually by a user. If false, draw objects from the indicator or strategy can only be removed from the chart if the script removes the drawing object, or the script is terminates. Default set to false.

### Syntax

**AllowRemovalOfDrawObjects**

### Examples

```csharp
protected override void OnStateChange()
{
     Add(new Plot(Brushes.Orange, "SMA"));
     AllowRemovalOfDrawObjects = true; // Draw objects can be removed separately from the script
}
```
