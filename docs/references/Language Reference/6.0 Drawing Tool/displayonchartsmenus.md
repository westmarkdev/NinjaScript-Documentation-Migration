---
title: DisplayOnChartsMenus
pathName: displayonchartsmenus
parent: drawing_tools
status: imported
section: references
---

## Definition

Determines if the drawing tool displays in the chart's drawing tool menus.

## Property Value

A bool value, when true the drawing tool will be created on the chart's drawing tool menu; otherwise false. Default value is true.

## Syntax

**DisplayOnChartsMenus**

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name                 = @"My Drawing Tool";
     DisplayOnChartsMenus = true;
   }
}
```
