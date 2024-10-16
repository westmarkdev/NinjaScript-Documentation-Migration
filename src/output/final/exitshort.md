---
title: "ExitShort()"
pathName: /docs/desktop/exitshort
---

## Definition

Generates a buy to cover market order to exit a short position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
ExitShort()
```

```csharp
ExitShort(int quantity)
```

```csharp
ExitShort(string fromEntrySignal)
```

```csharp
ExitShort(string signalName, string fromEntrySignal)
```

```csharp
ExitShort(int quantity, string signalName, string fromEntrySignal)
```

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](/docs/desktop/advanced_order_handling) concepts:

```csharp
ExitShort(int barsInProgressIndex, int quantity, string signalName, string fromEntrySignal)
```

## Parameters

|  |  |
| --- | --- |
| signalName | User-defined signal name identifying the order generated. Max 50 characters. |
| fromEntrySignal | The entry signal name. This ties the exit to the entry and exits the position quantity represented by the actual entry. {% <br> %} Using an empty string will attach the exit order to all entries. |
| quantity | Entry order quantity. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. {% <br> %} See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;
    // Only enter if at least 10 bars has passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossBelow(SMA(10), SMA(20), 1))
        EnterShort("SMA Cross Entry");
    // Exits position
    if (CrossBelow(SMA(10), SMA(20), 1))
        ExitShort();
}
```

{% callout type="tip" %}
Tips (also see [Overview](/docs/desktop/managed_approach)):

&bull; This method is ignored if a short position does not exist {% <br> %}
&bull; It is helpful to provide a signal name if your strategy has multiple exit points to help identify your exits on a chart {% <br> %}
&bull; You can tie an exit to an entry by providing the entry signal name in the parameter "fromEntrySignal" {% <br> %}
&bull; If you do not specify a quantity, the entire position is exited rendering your strategy flat {% <br> %}
&bull; If you do not specify a "fromEntrySignal" parameter, the entire position is exited rendering your strategy flat.
{% /callout %}
