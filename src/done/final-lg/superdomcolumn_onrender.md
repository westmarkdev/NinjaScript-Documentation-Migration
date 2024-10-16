---
title: "OnRender()"
pathName: superdomcolumn_onrender
---

## Definition

Used to draw custom content to the SuperDOM Column, such as a Grid.

## This method is called during the following conditions

- The SuperDOM is centered (either automatically or when the user presses the Center button)
- The SuperDOM is scrolled
- All accounts are disconnected
- A simulation account is reset
- A position is updated
- The user changes the SuperDOM's properties through the Properties menu
- The SuperDOM first loads (e.g. restoring from a workspace)
- The user changes the PnL display unit by clicking on the Position display
- The height/width of the SuperDOM window changes
- A user resizes the content area by dragging the splitter between price ladder and the columns

{% callout type="note" %}
While similar to a Chart Indicator's [OnRender()](onrender) method, the SuperDOM Column uses [WPF Drawing Context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) class, rather than the SharpDX library used for [chart rendering](rendering). Concepts between these two methods are guaranteed to be different.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your SuperDOM column with the following syntax:

```csharp
protected override void OnRender(DrawingContext dc, double renderWidth)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| dc | The [drawing context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) for the column |
| renderWidth | The rendering width for the column |

{% callout type="tip" %}
In order to force OnRender() to be called under a specific condition, call the [OnPropertyChanged()](onpropertychanged) method which will force the entire column to repaint. This approach should be used instead of calling OnRender() directly.
{% /callout %}

## Examples

```csharp
protected override void OnRender(DrawingContext dc, double renderWidth)
{
// Rendering logic for our column
}
```
