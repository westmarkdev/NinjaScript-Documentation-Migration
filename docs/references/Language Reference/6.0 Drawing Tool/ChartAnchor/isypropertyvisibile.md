---
title: IsYPropertyVisibile
pathName: isypropertyvisibile
parent: chartanchor
status: imported
section: references
---

## Definition

Indicates the anchor's Y properties are visible on the UI. When set to true, the Y values can be viewed from the Drawing Objects properties.

## Property Value

A bool value which when true will display the anchor's Y (price) data values from the drawing object properties; otherwise false. Default value is true.

## Syntax

**`<chartanchor>`.IsYPropertyVisibile**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          MyAnchor = new ChartAnchor();
          MyAnchor.IsYPropertyVisibile = true;
     }
     else if (State == State.Configure)
     {

     }
}
```
