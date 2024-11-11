---
title: Entering Calculation Logic
pathName: entering_calculation_logic5
parent: advanced_custom_plot_colors
section: guides
status: review
---

The OnBarUpdate() method is called for each incoming tick or on the close of a bar (user defined) when performing real-time calculations and is called on each bar of a data series when re-calculating the indicator. For example, an indicator would be re-calculated when adding it to an existing chart that has existing price data displayed. Therefore, this is the main method called for indicator calculation and we will use this method to enter the script that will calculate the ROC value.

## Setting Plot Thresholds  

The OnStateChange() method is called once before any bar data is loaded and is used to configure the indicator. The code below is automatically generated by the wizard and added to the OnStateChange() method. It configures the indicator for two plots and one line and sets the parameters.

```csharp
AddLine(Brushes.Black, 0, "ZeroLine");
AddPlot(Brushes.Green, "AboveZero");
AddPlot(Brushes.OrangeRed, "BelowZero");
```

Enter the following code in the OnStateChange() method and below the wizard generated code:

```csharp
// Set the threshold values for each plot
Plots[0].Min = 0;
Plots[1].Max = 0;
```

The concept of setting threshold values is to set when and when not to paint a plot on the chart. In this indicator, we have an "AboveZero" plot with a default color of green which we only want to see when the value of ROC is above zero and a "BelowZero" plot with a default color of OrangeRed which we only want to see when the value of ROC is below zero. In order to make that happen we have to set the threshold values of each plot.

**Plots[0].Min = 0;**

This statement says, in the collection of Plot objects, take the first one (**Plots[0]**) and set its minimum value to zero. This means any value below zero will not display.

**Plots[1].Max = 0;**

This statement says, in the collection of Plot objects, take the second one (**Plots[1]**) and set its maximum value to zero. This means any value above zero will not display.

We now have a simple plot switching mechanism that displays the correct colored line depending on if the value of ROC is above or below zero. In fact, you can take this concept a little bit farther. You can even set different plots style (bar, dot etc..) depending on threshold values.

A quick word about collections. Collections are objects that store a collection of objects, kind of like a container. In this case we are working with a collection of plots. In the above wizard generated code you will notice that we are adding new plots to the "Plots" collection. "AboveZero" was added first and then "BelowZero". This means that we can reference the "AboveZero" plot object through **Plots[0]**. The reason we don't pass in a value of 1 is because collections are zero based indexes. This means the first item has an index of 0, the second time an index of 1 and so forth.

## Completing the Indicator

This indicator is actually quite simple in its implementation. The last thing we need to do is add the calculation code and set the value of ROC to both our plot lines.

Replace the wizard generated code with the following code into the OnBarUpdate() method in the NinjaScript Editor:

```csharp

// Are there enough bars
if (CurrentBar < Period) return;

// Set the plot values
AboveZero[0] = SMA(ROC(Period), Smooth)[0];
BelowZero[0] = SMA(ROC(Period), Smooth)[0];
```

The calculation first checks to ensure there are enough bars to complete the calculation and then sets both plot lines to the ROC value.

The class code in your editor should look identical to the image below. You are now ready to [compile the indicator](compiling) and configure it on a chart.

```csharp

public class CustomROC : Indicator
{
    protected override void OnStateChange()
    {
        if (State == State.SetDefaults)
        {
            Description = @"ROC with custom line color options";
            Name = "CustomROC";
            Calculate = Calculate.OnBarClose;
            IsOverlay = false;
            DisplayInDataBox = true;
            DrawOnPricePanel = true;
            DrawHorizontalGridLines = true;
            DrawVerticalGridLines = true;
            PaintPriceMarkers = true;
            ScaleJustification = NinjaTrader.Gui.Chart.ScaleJustification.Right;
            //Disable this property if your indicator requires custom values that cumulate with each new market data event.
            //See Help Guide for additional information.
            IsSuspendedWhileInactive = true;
            Period = 14;
            Smooth = 3;
            AddLine(Brushes.Black, 0, "ZeroLine");
            AddPlot(Brushes.Green, "AboveZero");
            AddPlot(Brushes.OrangeRed, "BelowZero");
            Plots[0].Min = 0;
            Plots[1].Max = 0;
        }
        else if (State == State.Configure)
        {
        }
    }

    protected override void OnBarUpdate()
    {
        // Are there enough bars
        if (CurrentBar < Period) return;

        // Set the plot values
        AboveZero[0] = SMA(ROC(Period), Smooth)[0];
        BelowZero[0] = SMA(ROC(Period), Smooth)[0];
    }

    #region Properties
    [NinjaScriptProperty]
    [Range(1, int.MaxValue)]
    [Display(Name="Period", Description="Number of periods", Order=1, GroupName="Parameters")]
    public int Period
    { get; set; }

    [NinjaScriptProperty]
    [Range(1, int.MaxValue)]
    [Display(Name="Smooth", Description="Smoothing rate", Order=2, GroupName="Parameters")]
    public int Smooth
    { get; set; }

    [Browsable(false)]
    [XmlIgnore]
    public Series<double> AboveZero
    {
        get { return Values[0]; }
    }

    [Browsable(false)]
    [XmlIgnore]
    public Series<double> BelowZero
    {
        get { return Values[1]; }
    }
    #endregion
}

```