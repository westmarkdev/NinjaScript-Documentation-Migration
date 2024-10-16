---
title: "OnRender()"
pathName: /docs/desktop/onrender
---

## Definition

Used to draw custom content to a Market Analyzer Column, such as a graph.

## This method is called during the following conditions:

- The Market Analyzer is scrolled

- The user changes the Market Analyzer's properties through the Properties menu

- The Market Analyzer first loads (e.g. restoring from a workspace)

- The height / width of the Market Analyzer window changes

- A user re-sizes the content area by dragging the splitter between the columns

{% callout type="note" %}
While similar to a Chart Indicator's [OnRender()](/docs/desktop/onrender) method, the Market Analyzer Column uses the [WPF Drawing Context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) class, rather than the SharpDX library used for [chart rendering](/docs/desktop/rendering). Concepts between these two methods are guaranteed to be different.
{% /callout %}

## Method Return Value

This method does not return a value.

### Syntax

You must override the method in your Market Analyzer column with the following syntax:

```csharp
protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| dc | The [drawing context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) for the column |
| renderSize | The rendering size for the column |

{% callout type="tip" %}
In order to force OnRender() to be called under a specific condition, call the [OnPropertyChanged()](/docs/desktop/onpropertychanged) method which will force the entire column to repaint. This approach should be used instead of calling OnRender() directly.
{% /callout %}

## Examples

```csharp
protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)
{
// Rendering logic for our Market Analyzer column
}
```
