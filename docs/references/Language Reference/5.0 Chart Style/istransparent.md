---
title: IsTransparent
pathName: istransparent
parent: chart_style
status: imported
section: references
---

## Definition

Indicates the bars in the ChartStyle are transparent.

## Property Value

A bool which, when true, indicates that the **UpBrush**, **DownBrush**, and **Stroke.Brush** are all set to transparent. Returns false if any of the three are not transparent.

## Syntax

**IsTransparent**

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.Configure)
   {
       //Print a message if the UpBrush, DownBrush, and Stroke.Brush are all transparent
       if (IsTransparent)
           Print("All bars are currently set to transparent");
   }
}

```
