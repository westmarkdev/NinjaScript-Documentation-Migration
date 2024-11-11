---
title: IsInHitTest
pathName: isinhittest
parent: rendering
section: references
status: imported
---

## Definition

Indicates a user is currently clicking in the chart panel in which the calling script resides.

{% callout type="note" %}

In addition to the example below, **IsInHitTest** can also be tested directly on chart objects (for example, **myHorizontalLine.IsInHitTest**). In this case, the **IsInHitTest** property of a specific object will refer to the panel in which the calling script resides, even if the calling script resides in a different panel than the object itself.

{% /callout %}

## Property Value

This property returns true to indicate that the chart panel in which the script resides is being clicked on; otherwise, false. Default set to false.

## Syntax

**IsInHitTest**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(IsInHitTest)
   {
       Print("user clicked on object");

       // do something
   }
}

```
