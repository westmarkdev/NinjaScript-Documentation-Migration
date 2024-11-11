---
title: Entering Calculation Logic
pathName: entering_calculation_logic4
parent: intermediate_historical_custom_series
section: guides
status: review
---

The OnBarUpdate() method is called for each incoming tick or on the close of a bar (user defined) when performing real-time calculations and is called on each bar of a data series when re-calculating the indicator. For example, an indicator would be re-calculated when adding it to an existing chart that has existing price data displayed. Therefore, this is the main method called for indicator calculation and we will use this method to enter the script that will do our calculations.

## Creating the Series`<double>` Object

1. Declare a variable (**MySeries** used in this example) of type **Series`<double>`** that will hold a **Series`<double>`** object within the region "Variables".

2. Create a new **Series`<double>`** object and assign it to the **MySeries** variable within the **OnStateChange()** method.

```csharp
private Series<double> MySeries;
protected override void OnStateChange()
{
 if (State == State.SetDefaults)
 {
   ...
 }
 else if (State == State.DataLoaded)
 {
   MySeries = new Series<double>(this);
 }
}
```

Storing calculations in the DataSeries object  

Now that we have our **Series`<double>`** object we can store double values into it. For this example we will store a simple Close minus Open calculation.

Enter the following code into the **OnBarUpdate()** method:

```csharp
// Calculate the range of the current bar and set the value
MySeries[0] = Close[0] - Open[0];
```

The value of a **Series`<t>`** object will be aligned with the current bar. This means that all **Series`<t>`** objects will be synced with the **CurrentBar** index. It allows you to store A **double** value that corresponds with every bar.

Using **Series`<t>`** values  

With our new **Series`<double>`** object we can continue with further calculations easily. We can now use our **Series`<double>`** object as input to an indicator method such as **SMA** or instead of always writing **Close[0] - Open[0]** we can substitute our **Series`<double>`** object instead as per the example below.

To plot our final calculation we will store the calculation in our plot called **MyPlot**. In the **OnBarUpdate()** method add the following code snippet:

```csharp
// Add the bar's range to the SMA value
MyPlot[0] = SMA[SMAPeriod](0) + MySeries[0];
```

Here we assign the **SMA** + **Series`<double>`** value to the property that represents the plot data using the "=" assignment operator. We have just finished coding our **CustomSeries** example. The class code in your editor should look identical to the below. You are now ready to [compile the indicator](compiling4) and configure it on a chart.

```csharp
public class CustomSeries : Indicator
{
   private Series<double> MySeries;

   protected override void OnStateChange()
   {
     if (State == State.SetDefaults)
     {
         Description                     = @"Stores intermediary calculations without the use of plots";
         Name                             = "CustomSeries";
         Calculate                         = Calculate.OnBarClose;
         IsOverlay                         = false;
         DisplayInDataBox                 = true;
         DrawOnPricePanel                 = true;
         DrawHorizontalGridLines           = true;
         DrawVerticalGridLines             = true;
         PaintPriceMarkers                 = true;
         ScaleJustification                 = NinjaTrader.Gui.Chart.ScaleJustification.Right;
         //Disable this property if your indicator requires custom values that cumulate with each new market data event.
         //See Help Guide for additional information.
         IsSuspendedWhileInactive         = true;
         SMAPeriod                         = 5;
         AddPlot(Brushes.Orange, "MyPlot");
     }
     else if (State == State.Configure)
     {
     }
     else if (State == State.DataLoaded)
     {
         MySeries = new Series<double>(this);
     }
   }

   protected override void OnBarUpdate()
   {
     // Calculate the range of the current bar and set the value
     MySeries[0] = Close[0] - Open[0];

     // Add the bar's range to the SMA value
     MyPlot[0] = SMA[SMAPeriod](0) + MySeries[0];
   }

   #region Properties
   [NinjaScriptProperty]
   [Range(1, int.MaxValue)]
   [Display(Name="SMAPeriod", Description="Simple Moving Average Period", Order=1, GroupName="Parameters")]
   public int SMAPeriod
   { get; set; }

   [Browsable(false)]
   [XmlIgnore]
   public Series<double> MyPlot
   {
     get { return Values[0]; }
   }
   #endregion
}
```
