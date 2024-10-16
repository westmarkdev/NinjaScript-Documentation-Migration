---
title: "PositionsAccount"
pathName: /docs/desktop/positionsaccount
---

## Definition

Holds an array of [PositionAccount](/docs/desktop/positionaccount) objects that represent positions managed by the strategy's account. This property should only be used when your strategy is executing orders against [multiple instruments](/docs/desktop/multi-time_frame__instruments).

Index value is based on the array of Bars objects added via the [AddDataSeries()](/docs/desktop/adddataseries) method. For example:

First Bars is ES 1 Minute  
Secondary Bars is ES 5 Minute  
Third Bars is NQ 5 Minute  

PositionsAccount[0] == ES position  
PositionsAccount[1] == Always a flat position, ES position will always be PositionsAccount[0]  
PositionsAccount[2] == NQ position  

{% callout type="tip" %}
&bull; For single instrument scripts, please see [PositionAccount](/docs/desktop/positionaccount) object{% <br> %}
&bull; For Strategy Positions, please see [Positions](/docs/desktop/positions)  
{% /callout %}

## Property Value

An array of [PositionAccount](/docs/desktop/positionaccount) objects.

### Syntax

```csharp
PositionsAccount[int index]
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "ExampleStrategy";
    }
    else if (State == State.Configure)
    {
        AddDataSeries("ES 03-15", BarsPeriodType.Minute, 5);
        AddDataSeries("NQ 03-15", BarsPeriodType.Minute, 5);
    }
}

protected override void OnBarUpdate()
{
    Print("ES account position is " + PositionsAccount[0].MarketPosition);
    Print("NQ account position is " + PositionsAccount[2].MarketPosition);
    // Alternative approach. By checking what Bars object is calling the OnBarUpdate()
    // method, we can just use the Position property since its pointing to the correct
    // position.
    if (BarsInProgress == 0)
        Print("ES account position is " + PositionAccount.MarketPosition);
    else if (BarsInProgress == 2)
        Print("NQ account position is " + PositionAccount.MarketPosition);
}
```
