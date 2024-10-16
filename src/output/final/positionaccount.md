---
title: "PositionAccount"
pathName: /docs/desktop/positionaccount
---

## Definition

Represents position related information that pertains to real-world account (live or simulation).

{% callout type="tip" %}
• For multi-instrument scripts, please see the [PositionsAccount](/docs/desktop/positionsaccount) object which holds an array of all instrument positions managed by the strategy's account.  
• For a Strategy Position, please see [Position](/docs/desktop/position).
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| Account | An [Account](/docs/desktop/account_class) object which corresponds to the position |
| [AveragePrice](/docs/desktop/position_averageprice) | Gets the average entry price of the account position |
| [GetUnrealizedProfitLoss()](/docs/desktop/position_getunrealizedprofitloss) | Gets the unrealized PnL for the account |
| [Instrument](/docs/desktop/position_instrument) | An [Instrument](/docs/desktop/instrument) value representing the instrument of an order |
| [MarketPosition](/docs/desktop/position_marketposition) | Gets the current market position of the account  Possible values: {% <br> %} &bull; MarketPosition.Flat {% <br> %} &bull; MarketPosition.Long {% <br> %} &bull; MarketPosition.Short |
| [Quantity](/docs/desktop/position_quantity) | Gets the current account position size |
| ToString() | A string representation of an account position |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average entry price
    Print("The average entry price is " + PositionAccount.AveragePrice);
}
```

