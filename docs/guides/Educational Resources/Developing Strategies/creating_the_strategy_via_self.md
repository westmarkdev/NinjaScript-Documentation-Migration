---
title: Creating the Strategy via Self Programming
pathName: creating_the_strategy_via_self_programming
parent: developing_strategies
section: guides
status: imported
---

If you have not done so already, press the "Unlock Code" button within the wizard to launch the NinjaScript Editor.

The **OnBarUpdate()** method is called for each incoming tick or on the close of a bar (user defined) when performing real-time calculations. Therefore, this is the main method called for strategy calculation and we will use this method to enter the script that checks for entry and exit conditions.

## The Entry and Exit Condition

Enter the code contained within the **OnBarUpdate()** method in the image below into the **OnBarUpdate()** method in the NinjaScript Editor:

```csharp
protected override void OnBarUpdate()
{
    if (CrossAbove(SMA(Fast), SMA(Slow), 1))
        EnterLong();

    if (CrossBelow(SMA(Fast), SMA(Slow), 1))
        EnterShort();
}
```

Translated into English, the code contained within the **OnBarUpdate()** method above reads:

if the fast simple moving average crosses above the slow simple moving average within the last bar, go long

if the fast simple moving average crosses below the slow simple moving average within the last bar, go short

To accomplish this we used the following methods:

* [CrossAbove](crossabove) - Checks for a cross above condition and returns true or false
* [CrossBelow](crossbelow) - Checks for a cross below condition and returns true or false
* [SMA](moving_average_-_simple_sma) - Returns the value of a simple moving average
* [EnterLong](enterlong) - Enters a market order long
* [EnterShort](entershort) - Enters a market order short
