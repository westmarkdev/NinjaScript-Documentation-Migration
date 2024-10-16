---
title: "Position"
pathName: /docs/desktop/position
---

## Definition

Represents position-related information that pertains to an instance of a strategy.

{% callout type="tip" %}
• For multi-instrument scripts, please see the [Positions](/docs/desktop/positions) object which holds an array of all instrument positions managed by the strategy's account.  
• For a real-world Account Position, please see [PositionAccount](/docs/desktop/positionaccount).
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| Account | An [Account](/docs/desktop/account_class) object which corresponds to the position |
| [AveragePrice](/docs/desktop/position_averageprice) | Gets the average entry price of the strategy position |
| [GetUnrealizedProfitLoss()](/docs/desktop/position_getunrealizedprofitloss) | Gets the unrealized PnL |
| [Instrument](/docs/desktop/position_instrument) | An [Instrument](/docs/desktop/instrument) value representing the instrument of an order |
| [MarketPosition](/docs/desktop/position_marketposition) | Gets the current market position {% <br> %} Possible values: {% <br> %} MarketPosition.Flat{% <br> %} MarketPosition.Long{% <br> %} MarketPosition.Short |
| [Quantity](/docs/desktop/position_quantity) | Gets the current position size |
| ToString() | A string representation of a position |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average entry price
    Print("The average entry price is " + Position.AveragePrice);
}
```
