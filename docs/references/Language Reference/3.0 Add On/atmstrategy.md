---
title: AtmStrategy
pathName: atmstrategy
parent: add_on
section: references
status: review
---

AtmStrategy contains properties and methods used to manage [ATM Strategies](advanced_trade_management_atm). When working with an [AtmStrategySelector](atmstrategyselector), selected objects can be case to AtmStrategy to obtain or change their properties.

{% callout type="note" %}

1. For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons)
2. For more information on working with the ATM strategies programmatically in general, please see the [Using ATM Strategies](using_atm_strategies) section.
{% /callout %}

## Example

```csharp
// Using AtmStrategy to handle user selections in an ATM Strategy Selector
myAtmStrategySelector.SelectionChanged += (o, args) =>
{
   if (myAtmStrategySelector.SelectedItem == null)
       return;
   if (args.AddedItems.Count > 0)
   {
       // Change the selected TIF in a TIF selector based on what is selected in the ATM Strategy Selector
       NinjaTrader.NinjaScript.AtmStrategy selectedAtmStrategy = args.AddedItems[0] as NinjaTrader.NinjaScript.AtmStrategy;
       if (selectedAtmStrategy != null)
       {
           myTifSelector.SelectedTif = selectedAtmStrategy.TimeInForce;
       }
   }
};
```
