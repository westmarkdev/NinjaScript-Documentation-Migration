---
title: OnRender()
pathName: onrender2
parent: market_analyzer_column
section: references
status: imported
---

## Definition

Used to draw custom content to a Market Analyzer Column, such as a graph.

This method is called during the following conditions:

* The Market Analyzer is scrolled
* The user changes the Market Analyzer's properties through the Properties menu
* The Market Analyzer first loads (e.g. restoring from a workspace)
* The height / width of the Market Analyzer window changes
* A user re-sizes the content area by dragging the splitter between the columns

{% callout type="note" %}

While similar to a Chart Indicator's **OnRender()** method, the Market Analyzer Column uses the **WPF Drawing Context** class, rather than the **SharpDX** library used for **chart rendering**. Concepts between these two methods are guaranteed to be different.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your Market Analyzer column with the following syntax:

```csharp
protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)   
{  
}
```

## Method Parameters

{% table %}

* Parameter
* Description

---

* **dc**
* The **drawing context** for the column

---

* **renderSize**
* The rendering size for the column
{% /table %}

{% callout type="note" %}
In order to force **OnRender()** to be called under a specific condition, call the **OnPropertyChanged()** method which will force the entire column to repaint. This approach should be used instead of calling **OnRender()** directly.
{% /callout %}

## Examples

```csharp
protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)
{
   // Rendering logic for our Market Analyzer column
}
```
