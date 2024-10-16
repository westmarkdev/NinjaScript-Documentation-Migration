---
title: "ExitLong()"
pathName: /docs/desktop/exitlong
---

## Definition

Generates a sell market order to exit a long position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
ExitLong()
```

```csharp
ExitLong(int quantity)
```

```csharp
ExitLong(string fromEntrySignal)
```

```csharp
ExitLong(string signalName, string fromEntrySignal)
```

```csharp
ExitLong(int quantity, string signalName, string fromEntrySignal)
```

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](/docs/desktop/advanced_order_handling) concepts:

```csharp
ExitLong(int barsInProgressIndex, int quantity, string signalName, string fromEntrySignal)
```

## Parameters

|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| fromEntrySignal | The entry signal name. This ties the exit to the entry and exits the position quantity represented by the actual entry. {% <br> %} Note: Using an empty string will attach the exit order to all entries. |
| quantity | Entry order quantity. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. {% <br> %} See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Only enter if at least 10 bars has passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
        EnterLong("SMA Cross Entry");

    // Exits position
    if (CrossBelow(SMA(10), SMA(20), 1))
        ExitLong();
}
```

{% callout type="tip" %}
Tips (also see [Overview](/docs/desktop/managed_approach)):

- This method is ignored if a long position does not exist.
- It is helpful to provide a signal name if your strategy has multiple exit points to help identify your exits on a chart.
- You can tie an exit to an entry by providing the entry signal name in the parameter "fromEntrySignal".
- If you do not specify a quantity, the entire position is exited rendering your strategy flat.
- If you do not specify a "fromEntrySignal" parameter, the entire position is exited rendering your strategy flat.
{% /callout %}