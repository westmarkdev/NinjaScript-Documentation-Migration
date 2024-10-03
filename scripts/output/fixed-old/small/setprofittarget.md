---
path: setprofittarget
title: SetProfitTarget()
---

## Definition

Generates a profit target order with the signal name "Profit target" to exit a position. Profit target orders are real working orders submitted immediately to the market upon receiving an execution from an entry order.

{% callout type="note" %}

- Profit target orders are submitted in real-time on incoming executions from entry orders•Since they are submitted upon receiving an execution, the Set method should be called prior to submitting the associated entry order to ensure an initial level is set.
- A strategy will either generate a target order for each partial fill of an entry order or one order for all fills. See additional information under the [Strategies](options_strategies) tab of the Options dialog window. •If a [stop loss](setstoploss) or [trail stop](settrailstop) order is generated in addition to a profit target order, they are submitted as OCO (one cancels other)
- A profit target order is automatically cancelled if the managing position is closed by another strategy generated exit order
- Should you have multiple Bars objects of the same instrument while using SetProfitTarget() in your strategy, you should only submit orders for this instrument to the first Bars context of that instrument. This is to ensure your order logic is processed correctly and any necessary order amendments are done properly. |

## Syntax

`SetProfitTarget(CalculationMode mode, double value)`

`SetProfitTarget(CalculationMode mode, double value, bool isMIT)`

`SetProfitTarget(string fromEntrySignal, CalculationMode mode, double value)`

`SetProfitTarget(string fromEntrySignal, CalculationMode mode, double value, bool isMIT)`

{% callout type="warning" %}
This method CANNOT be called from the [OnStateChange()](onstatechange) method during State.SetDefaults

{% /callout %}

## Parameters

|  |  |
| --- | --- |
| currency | Sets the profit target amount in currency ($500 profit for example) |
| isMIT | Sets the profit target as a market-if-touched order |
| mode | Determines the manner in which the value parameter is calculated
Possible values are:

|  |  |
| --- | --- |
| CalculationMode.Currency | PnL away from average entry. Calculated by the dollar per tick value for the order quantity used. When this mode is used, [StopTargetHandling](stoptargethandling) will automatically be set to ByStrategyPosition |
| CalculationMode.Percent | Percentage away from the average entry, based on the average entry price.
<br>{% callout type="note" %}Please note in percentage calculation mode a value of 1 is equal to 100%, a value of 0.1 is equal to 10%, and a value of 0.01 will be 1%{% /callout %}
| CalculationMode.Pips | Pips away from average entry. |
| CalculationMode.Price | The absolute price point specified. |
| CalculationMode.Ticks | Ticks away from entry average entry.  |
| value | The value the profit target order is offset from the position entry price (exception is using .Price mode where 'value' will represent the actual price) |
| fromEntrySignal | The entry signal name. This ties the profit target exit to the entry and exits the position quantity represented by the actual entry.  Using an empty string will attach the exit order to all entries. |

{% callout type="note" %}
Tips (also see [Overview](managed_approach)):

- It is suggested to call this method from within the strategy [OnStateChange()](onstatechange) method if your profit target price/offset is static
- You may call this method from within the strategy [OnBarUpdate()](onbarupdate) method should you wish to dynamically change the target price while in an open position •Should you call this method to dynamically change the target price in the strategy [OnBarUpdate()](onbarupdate) method, you should always reset the target price / offset value when your strategy is flat otherwise, the last price/offset value set will be used to generate your profit target order on your next open position
- The signal name generated internally by this method is "Profit target" which can be used with various methods such as [BarsSinceExitExecution()](barssinceexitexecution), or other order concepts which rely on identifying a signal name |

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
    // Submits a profit target order 10 ticks away from the avg entry price
    SetProfitTarget(CalculationMode.Ticks, 10);
    }
}
```