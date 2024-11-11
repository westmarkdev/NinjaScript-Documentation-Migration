---
title: StartAtmStrategy()
pathName: startatmstrategy
parent: add_on
section: references
status: review
---

## Definition

**StartAtmStrategy** can be used to submit entry orders with ATM strategies.

## Syntax

**NinjaTrader.NinjaScript.AtmStrategy.StartAtmStrategy**(AtmStrategy atmStrategyTemplate, Order entryOrder)

**NinjaTrader.NinjaScript.AtmStrategy.StartAtmStrategy**(string atmStrategyTemplateName, Order entryOrder)

## Properties

{% table %}

* atmStrategyTemplate
* atmStrategyTemplateName
* entryOrder

---

* An AtmStrategy representing the ATM strategy you wish to use
* A string representing the name of the ATM strategy you wish to use
* An Order representing the entry order
{% /table %}

{% callout type="note" %}
Critical: The "name" argument on the **CreateOrder()** method MUST be named "Entry" for the ATM Strategy to be started successfully.
{% /callout %}

## Examples

```csharp
// Example of starting an ATM strategy from an Add On window. The concept can be carried over
// to any NinjaScript object you may be working on.
public class MyAddOnTab : NTTabPage
{
    private Account account;
    private Order entryOrder;

    public MyAddOnTab()
    {
        // Find our Sim101 account
        lock (Account.All)
            account = Account.All.FirstOrDefault(a => a.Name == "Sim101");

        if (account != null)
        {
            entryOrder = account.CreateOrder(Cbi.Instrument.GetInstrument("AAPL"), OrderAction.Buy, OrderType.Market,
                TimeInForce.Day, 1, 0, 0, string.Empty, "Entry", null);

            // Submits our entry order with the ATM strategy named "myAtmStrategyName"
            **NinjaTrader.NinjaScript.AtmStrategy.StartAtmStrategy**("myAtmStrategyName", entryOrder);
        }
    }

    // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code if building an Add On window.
}
```
