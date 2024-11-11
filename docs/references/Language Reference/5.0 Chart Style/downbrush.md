---
title: DownBrush
pathName: downbrush
parent: chart_style
status: imported
section: references
---

## Definition

A **Brush** object used to determine the color to paint the down bars for the ChartStyle.

{% callout type="note" %}

This Windows Presentation Forms (WPF) implementation of the Brush class is not directly used to paint bars on the chart. Instead it is converted to a SharpDX Brush in the **DownBrushDX** property. This property is used to capture user input for changing brush colors.

{% /callout %}

## Property Value

A **WPF** Brush object used to paint the down bars.

## Syntax

**DownBrush**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        // Set a new name for the DownBrush property
        SetPropertyName("DownBrush", "DecliningBrush");
    }
}
```
