---
title: Entering Strategy Logic
pathName: entering_strategy_logic
parent: developing_strategies
section: guides
status: imported
---

## Using the **OnStateChange()** Method to Configure the Strategy

The **OnStateChange()** method is called once prior to running a strategy and can be used to set properties or call methods in preparation for running a strategy.

Enter the code contained within the **OnStateChange()** method in the image below into the **OnStateChange()** method when we are in the State.DataLoaded state in the NinjaScript Editor.

   {
     Description                               = @"RSI with a Stop Loss and Profit Target";
     Name                                     = "RSIwithStopAndTarget";
     Calculate                                 = Calculate.OnBarClose;
     EntriesPerDirection                       = 1;
     EntryHandling                             = EntryHandling.AllEntries;
     IsExitOnSessionCloseStrategy             = true;
     ExitOnSessionCloseSeconds                 = 30;
     IsFillLimitOnTouch                       = false;
     MaximumBarsLookBack                       = MaximumBarsLookBack.TwoHundredFiftySix;
     OrderFillResolution                       = OrderFillResolution.Standard;
     Slippage                                 = 0;
     StartBehavior                             = StartBehavior.WaitUntilFlat;
     TimeInForce                               = TimeInForce.Gtc;
     TraceOrders                               = false;
     RealtimeErrorHandling                     = RealtimeErrorHandling.StopCancelClose;
     StopTargetHandling                       = StopTargetHandling.PerEntryExecution;
     BarsRequiredToTrade                       = 20;
     // Disable this property for performance gains in Strategy Analyzer optimizations
     // See the Help Guide for additional information
     IsInstantiatedOnEachOptimizationIteration = true;
     RSIPeriod                                 = 14;
     RSISmooth                                 = 3;
     ProfitTarget                             = 12;
     StopLoss                                 = 6;
   }
   else if (State == State.DataLoaded)
   {
     AddChartIndicator(RSI(RSIPeriod, RSISmooth));

     SetStopLoss(CalculationMode.Ticks, StopLoss);
     SetProfitTarget(CalculationMode.Ticks, ProfitTarget);
   }
}

```

For more information on the strategy properties added in State.SetDefaults, please see our complete [Strategy](strategy) documentation.

The **AddChartIndicator()** method is called and the **RSI()** indicator method is passed in which will automatically plot this indicator on a chart when the strategy runs.

The method signature for the **RSI()** indicator is:

```csharp
RSI(int period, int smooth);
```

It is valid to have used the **Add()** method in the following manner:

```csharp
AddChartIndicator(RSI(14, 3));
```

However, instead of hard coding the period value to 14 and the smooth value to 3, we substituted the values for the user defined inputs we defined in the wizard. Calling the **Add()** method in the following manner:

```csharp
AddChartIndicator(RSI(RSIPeriod, RSISmooth));
```

Allows us to change the period and smooth parameters of the embedded RSI indicator in the strategy at run time. This gives us a higher level of flexibility when working with our strategy.

**SetStopLoss()** and **SetProfitTarget()** are called with **CalculationMode.Ticks**. This means that when a position is opened, the strategy will immediately submit a stop and target order with a price that is calculated based on the **StopLoss** and **ProfitTarget** parameters passed in offset from the positions average entry price.

## Using the **OnBarUpdate()** Method for the Core Strategy Logic

The **OnBarUpdate()** method is called for each incoming tick or on the close of a bar (user defined) when performing real-time calculations. Therefore, this is the main method called for strategy calculation and we will use this method to enter the script that check for entry and exit conditions.

Enter the code contained within the **OnBarUpdate()** method in the image below into the **OnBarUpdate()** method in the NinjaScript Editor:

```csharp
protected override void OnBarUpdate()
{
   if (CurrentBar < RSIPeriod)
     return;
   
   if(CrossAbove(RSI(RSIPeriod, RSISmooth), 20, 1))
     EnterLong();
}
```

Since our strategy exit logic has already been set up in the **OnStateChange()** method above, we only need to focus on expressing our entry logic. The strategy entry logic is very straight forward and can be translated to English:

if we have not seen the number of bars specified by the user defined input "RSIPeriod" then do not go any further

if **RSI** crosses above a value of 20 within the last bar, go long

To accomplish this we used the following methods and properties:

**CurrentBar** - A value representing the current bar being processed (think of a chart where the left most bar would be equal to one)

**CrossAbove()** - Checks for a cross above condition and returns true or false

**RSI()** - Returns the value of the RSI indicator

**EnterLong()** - Enters a market order long
