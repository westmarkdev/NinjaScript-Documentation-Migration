---
title: "SetZOrder"
pathName: /docs/desktop/setzorder
---

## Definition

Used to assign a unique identifier representing the index in which chart objects are drawn on the chart's Z-axis (front to back ordering). Objects with a higher ZOrder are drawn first.

{% callout type="note" %}

1. To check on which ZOrder index the object gets drawn use the [ZOrder](/docs/desktop/chart_zorder) property.
2. Assigning specific ZOrder indices to draw at should be done once the [State](/docs/desktop/onstatechange) has reached State.Historical.
3. If you want to draw your object behind the bars, assign to use index -1 (like in the example below).
4. If you want to draw your object topmost, assign to use index int.MaxValue.
5. Any levels in between can be directly assigned, the starting / default levels used by NinjaTrader can be seen [here](/docs/desktop/chart_zorder).
6. You can see the highest ZOrder currently in a chart with code such our second example below - setting higher values than this value will result in the ZOrder to be set to this value, so this can be thought of as the current 'top'.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
SetZOrder(int DesiredZOrderLevel)
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Historical)
    {
        // Make sure our object plots behind the chart bars
        SetZOrder(-1);
    }
}
```

```csharp
protected override void OnRender(ChartControl cc, ChartScale cs)
{
    Print(ChartPanel.ChartObjects.Max(co => co.ZOrder));
}
```
