---
status: double_check
title: UpBrush
parent: chart_style
pathName: upbrush
section: references
lg2m: true
---

## Definition

A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the up bars for the ChartStyle.

{% callout type ="note" %}

This Windows Presentation Forms (WPF) implementation of the Brush class is not directly used to paint bars on the chart. Instead it is converted to a SharpDX Brush in the [UpBrushDX](upbrushdx.md) property. This property is used to capture user input for changing brush colors.

{% /callout }

## Property  Value

A [WPF](https://msdn.microsoft.com/en-us/library/ms754130(v=vs.110).aspx) Brush object used to paint the up bars

## Syntax

**UpBrush**

## Examples

```csharp
protected override void OnStateChange()  
{  
  if (State == State.Configure)  
  {  
      // Set a new name for the UpBrush property  
      SetPropertyName("UpBrush", "AdvancingBrush");  
  }  
}
```
