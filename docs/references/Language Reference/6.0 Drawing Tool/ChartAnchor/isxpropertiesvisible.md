---
title: IsXPropertiesVisible
pathName: isxpropertiesvisible
parent: chartanchor
status: imported
section: references
---

## Definition

Indicates the anchor's X properties are visible on the UI. When set to true, the X values can be viewed from the Drawing Objects properties.

## Property Value

A bool value which when true will display the anchor's X (time) data values from the drawing object properties; otherwise false. Default value is true.

## Syntax

**`<chartanchor>`.IsXPropertiesVisible**

## Examples

```csharp

protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         MyAnchor = new ChartAnchor();
         MyAnchor.IsXPropertiesVisible = true;
     }
     else if (State == State.Configure)
     {

     }
}
```
