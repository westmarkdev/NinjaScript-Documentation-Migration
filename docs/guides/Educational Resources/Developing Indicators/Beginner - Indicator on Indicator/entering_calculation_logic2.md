---
title: Entering Calculation Logic
pathName: entering_calculation_logic2
parent: beginner_indicator_on_indicator
section: guides
status: review
---

The **OnBarUpdate()** method is called for each incoming tick, or on the close of a bar (if enabled) when performing real-time calculations, and is called on each bar of a **Bars** object when re-calculating the indicator (For example, an indicator would be re-calculated when adding it to an existing chart that has existing price data displayed). This is the main method used for indicator calculations, and we will calculate our core indicator logic (calculating an average of volume) within this method.

## Calculating the Average

NinjaTrader has built in indicators that you can reference in your calculations. Since we are calculating a simple moving average of volume it would make sense for us to use the built in SMA indicator and Volume indicators.

Enter the following code into the **OnBarUpdate()** method in the NinjaScript Editor:

```csharp
// Calculate the volume average
double average = SMA(VOL(), Periods)[0];
```

Here we declared the variable "average" which is of type double. This serves as the temporary storage for the current value of the simple moving average of volume. We then use the simple moving average indicator and pass in the volume indicator as its input, pass in our indicator "Periods" property (a parameter we defined in the wizard) and access the current value "[0]" that we will assign to our variable "average". If we wanted to assign the value one bar ago, we could have used "[1]".

## Final Assignment

Enter the following code into the **OnBarUpdate()** method and below the code snippet you entered above:

```csharp
// Set the calculated value to the plot
MyPlot[0] = average;
```

Here we assign the "average" value to the property that represents the plot data using the '=' assignment operator. We have just finished coding our simple moving average of volume. Your class code should look identical to the code below. You are now ready to [compile the indicator](compiling2) and configure it on a chart.

```csharp
public class VolSMA : Indicator
{
   protected override void OnStateChange()
   {
     if (State == State.SetDefaults)
     {
         Description                     = @"Moving average of volume";
         Name                             = "VolSMA";
         Calculate                         = Calculate.OnBarClose;
         IsOverlay                         = false;
         DisplayInDataBox                 = true;
         DrawOnPricePanel                 = true;
         DrawHorizontalGridLines           = true;
         DrawVerticalGridLines             = true;
         PaintPriceMarkers                 = true;
         ScaleJustification               = NinjaTrader.Gui.Chart.ScaleJustification.Right;
         //Disable this property if your indicator requires custom values that cumulate with each new market data event. 
         //See Help Guide for additional information.
         IsSuspendedWhileInactive         = true;
         Periods                           = 10;
         AddPlot(Brushes.Orange, "MyPlot");
     }
     else if (State == State.Configure)
     {
     }
   }
   protected override void OnBarUpdate()
   {
     // Calculate the volume average
     double average = SMA(VOL(), Periods)[0];
     // Set the calculated value to the plot
     MyPlot[0] = average;
   }
   #region Properties
   [NinjaScriptProperty]
   [Range(1, int.MaxValue)]
   [Display(Name="Periods", Description="Number of periods", Order=1, GroupName="Parameters")]
   public int Periods
   { get; set; }
   [Browsable(false)]
   [XmlIgnore]
    public Series<double> MyPlot
   {
     get { return Values[0]; }
   }
   #endregion
```
