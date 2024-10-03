---

title: code_breaking_changes
pathName: code-breaking-changes
created: Thursday, October 3rd 2024, 11:28:13 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Overview

The following document is intended as a high-level overview of the NinjaScript changes you can expect between NinjaTrader 7 and NinjaTrader 8. For specific information on a particular method or property, you can refer to the dynamically formatted Code Breaking table at the bottom of this page. We recommend using the Filter and Sorting features built into the table, as well checking the Summary column and expanding the Details section of each entry for general information. Referring to the conveniently linked NinjaTrader 8 and NinjaTrader 7 documentation will provide specific information on syntax, usage, and examples of any new implementation or element names.

{% callout type="note" %}  
Note: Information on this page focuses on supported (documented) NinjaTrader methods and properties shared between versions. NinjaTrader 8 has seen a significant increase in supported NinjaTrader code, however, if you were using previously undocumented NinjaTrader 7 methods or properties, they will NOT be covered in this topic. You may be able to find more information on previously undocumented methods and properties in the NinjaTrader 8 Help Guide, or our support staff will also be happy to personally point you in the right direction.  
{% /callout %}

{% callout type="critical" %}  
Critical: If your product uses unsupported (undocumented) elements we strongly urge you to put your scripts through thorough testing to ensure they still behave as expected. There is NO guarantee that previously undocumented method or property behavior has not changed in the new version of NinjaTrader 8.  
{% /callout %}

For questions or comments, please contact us at <platformsupport@ninjatrader.com>

## Implementation Changes Overview

### Initialize(), OnStartUp(), OnTermination()

In NinjaTrader 8, methods for setting or releasing various resources during the lifetime of a NinjaTrader object have been simplified to a single `OnStateChange()` method.

```csharp
protected override void OnStateChange() 
{ 
    if (State == State.SetDefaults) 
    { 
        // set the default properties
        Name = "My Indicator";
        Fast = 10; 
        Slow = 25; 
        IsOverlay = true; 
        IsAutoScale = true; 
    } 
}
```

### Strategies, Orders, and Accounts

Low-level access has been provided to allow more flexibility with trade data information.

{% callout type="tip" %}  
Tip: Since NinjaTrader 8 now exposes the direct Order object, it's possible to receive null object reference errors if you attempt to access an order object before the entry or exit order method has returned. To prevent these situations, it's recommended to assign your strategies Order variables in the `OnOrderUpdate()` method and match them by their signal name (order.Name).  
{% /callout %}

```csharp
Order myOrder = null;

protected override void OnBarUpdate()
{
    if (Position.MarketPosition == MarketPosition.Flat && myOrder == null)
        EnterLongLimit(Low[0], "Entry");

    if (myOrder != null)
    {
        Print(myOrder.OrderState);

        if (myOrder.OrderState == OrderState.Cancelled || myOrder.OrderState == OrderState.Filled)
            myOrder = null;            
    }
}

protected override void OnOrderUpdate(Cbi.Order order, double limitPrice, 
                                      double stopPrice, int quantity, 
                                      int filled, double averageFillPrice, 
                                      Cbi.OrderState orderState, DateTime time, 
                                      Cbi.ErrorCode error, string comment)
{
    // compare the order object created via EnterLongLimit by the signal name
    if (myOrder == null && order.Name == "Entry")
    {
        // assign myOrder to matching order update
        myOrder = order;         
    }
}
```

### Data Series Changes

Now there is just a template `Series<t>` class which can be used generically and allows support for additional types.

```csharp
Series<double> mySeries = new Series<double>(this);
Series<DateTime> myTimeSeries = new Series<DateTime>(this);
```

### Drawing Changes

All DrawObjects have been moved to a separate NinjaScript.DrawingTools namespace and are now properly known as DrawingTools.

```csharp
Draw.Line(this, "tag1", true, 10, Low[0], 0, Brushes.Red);
```

## Code Breaking Table

Below you will find a reference table that lists all of the supported NinjaScript changes between NinjaTrader 7 and NinjaTrader 8.

| Category | Base | NT7 Method/Property | NT8 Method/Property | Summary | Details |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

{% callout type="note" %}  
Note: For a detailed examination of changes and specific implementations, please refer to the code breaking changes table above.  
{% /callout %}
