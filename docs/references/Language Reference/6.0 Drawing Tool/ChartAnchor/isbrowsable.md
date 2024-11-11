---
title: IsBrowsable
pathName: isbrowsable
parent: chartanchor
status: imported
section: references
---

## Definition

Determines if the anchor are visible on the UI. When set to true, the anchors Y and X values can be viewed from the Drawing Objects properties.

## Property Value

A bool value which when true will display the anchor data values from the drawing object properties; otherwise false. Default value is true.

## Syntax

**`<chartanchor>`.IsBrowsable**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          MyAnchor = new ChartAnchor();
          MyAnchor.IsBrowsable = true;
     }
     else if (State == State.Configure)
     {
     }
}
