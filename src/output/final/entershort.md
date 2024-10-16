---
title: "EnterShort()"
pathName: /docs/desktop/entershort
---

## Definition

Generates a sell short market order to enter a short position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
EnterShort()
```

```csharp
EnterShort(string signalName)
```

```csharp
EnterShort(int quantity)
```

```csharp
EnterShort(int quantity, string signalName)
```

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](/docs/desktop/advanced_order_handling) concepts:

```csharp
EnterShort(int barsInProgressIndex, int quantity, string signalName)
```

{% callout type="note" %}
If using a method signature that does not have the parameter quantity, the order quantity will be taken from the quantity value set in the strategy dialog window when running or backtesting a strategy.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| quantity | Entry order quantity (if 0 is passed in, will be set to 1, except for stocks 100). |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. {% <br> %} See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Only enter if at least 10 bars have passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
        EnterShort("SMA Cross Entry");
}
```
