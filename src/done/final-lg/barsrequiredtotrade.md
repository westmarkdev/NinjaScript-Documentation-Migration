---
title: "BarsRequiredToTrade"
pathName: barsrequiredtotrade
---

## Definition

The number of historical bars required before the strategy starts processing order methods called in the [OnBarUpdate()](onbarupdate) method. This property is generally set via the UI when starting a strategy.

{% callout type="note" %}
In a multi-series strategy this restriction applies only for the primary Bars object. This means you can run into situations where the primary bars required to trade have been reached, but the additional bars required have not. Should your strategy logic intertwine calculations across different Bars objects please ensure all Bars objects have met the BarsRequiredToTrade requirement before proceeding. This can be done via checks on the [CurrentBars](currentbars) array.
{% /callout %}

## Property Value

An int value representing the number of historical bars. Default value is set to 20.

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](onstatechange) method during State.SetDefaults or State.Configure.
{% /callout %}

## Syntax

```csharp
BarsRequiredToTrade
```

{% callout type="tip" %}
When working with a multi-series strategy, real-time bar update events for a particular Bars object are only received when that Bars object has satisfied the BarsRequiredToTrade requirement. To ensure this requirement is met, please use the CurrentBars array.
{% /callout %}

## Examples

### Setting the default BarsRequiredToTrade value

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         BarsRequiredToTrade = 20;
     }
}
```

### Checking BarsRequiredToTrade against a CurrentBars array

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     BarsRequiredToTrade = 20;
   }
   else if (State == State.Configure)
   {
     // add 30 minute series for calculation logic
     AddDataSeries(BarsPeriodType.Minute, 30);
   }
}

protected override void OnBarUpdate()
{
   // do not process order logic until bars required to trade is met
   // for both primary and 30-minute series have reached their bars required to trade
   if (CurrentBars[0] < BarsRequiredToTrade || CurrentBars[1] < BarsRequiredToTrade)
     return;
   //order logic
}
```
