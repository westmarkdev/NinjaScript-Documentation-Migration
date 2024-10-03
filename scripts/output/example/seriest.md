---

title: seriest
pathName: series
created: Thursday, October 3rd 2024, 11:26:33 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

A Series<T> is a special generic type of data structure that can be constructed with any chosen data type and holds a series of values equal to the same number of elements as bars in a chart. If you have 200 bars loaded in your chart with a moving average plotted, the moving average itself holds a Series<double> object with 200 historical values of data, one for each bar. Series<double> objects can be used as input data for all [indicator methods](indicators.htm). The Series<T> class implements the ISeries<T> interface.

{% callout type="note" %}  
By default NinjaTrader limits the number of values stored for Series<T> objects to 256 from the current bar being processed. This drastically improves memory performance by not holding onto old values that are generally not needed. Should you need more values than the last 256 please be sure to create the Series<T> object so that it stores all values instead through the use of the [MaximumBarsLookBack](maximumbarslookback.htm) property.  
{% /callout %}

## Constructors

| Constructor | Description |
| --- | --- |
| Series<T>(ninjaScriptBase) | Creates a Series<T> object synchronized to the primary data series of the provided NinjaScript. |
| Series<T>(ninjaScriptBase, maximumBarsLookBack) | Creates a Series<T> object synchronized to the primary data series of the provided NinjaScript. This constructor also allows controlling the Series<T>'s [MaximumBarsLookBack](maximumbarslookback.htm). |
| Series<T>(bars) | Creates a Series<T> object synchronized to the provided [Bars](bars.htm) object; for Multi Time Frame scripts, this could be given from [BarsArray](barsarray.htm). |
| Series<T>(bars, maximumBarsLookBack) | Creates a Series<T> object synchronized to the provided [Bars](bars.htm) object; for Multi Time Frame scripts, this could be given from [BarsArray](barsarray.htm). While this constructor allows controlling the Series<T>'s [MaximumBarsLookBack](maximumbarslookback.htm), it is forced to MaximumBarsLookBack.Infinite. |

## Parameters

| Parameter | Description |
| --- | --- |
| ninjaScriptBase | The NinjaScript object used to create the Series. |
| bars | The [Bars](bars.htm) object used to create the Series. |
| maximumBarsLookBack | A [MaximumBarsLookBack](maximumbarslookback.htm) value used for memory performance. |

## Methods and Properties

| Method/Property | Description |
| --- | --- |
| [GetValueAt()](getvalueat.htm) | Returns the underlying input value at a specified bar index value. |
| [IsValidDataPoint()](isvaliddatapoint.htm) | Determines if the specified input is set at a barsAgo value relative to the current bar. |
| [Reset()](reset.htm) | Resets the internal marker which is used for [IsValidDataPoint()](isvaliddatapoint.htm) back to false. |
| [Count](count.htm) | The total number of bars or data points. |

## Creating Series<T> Objects

When creating custom indicators, Series<double> objects are automatically created for you by calling the [AddPlot()](addplot.htm) method and can be subsequently referenced by the [Value](value.htm) and/or [Values](values.htm) property. However, you may have a requirement to create a Series<T> object to store values that are part of an overall indicator value calculation. This can be done within a custom indicator or strategy.

{% callout type="note" %}  
Custom Series<T> objects will hold the number of values specified by the [MaximumBarsLookBack](maximumbarslookback.htm) property when the custom series object is instantiated.  
{% /callout %}

To create a Series<T> object:

1. Determine the data type of the Series<T> object you wish to create. This could be double, bool, int, string, or any other object type you want.
2. Define a variable of type Series<T> that will hold a Series<T> object. This example will create "myDoubleSeries" as a Series<double>.
3. In the [OnStateChange()](onstatechange.htm) method, in the State.DataLoaded, create a new Series<T> object and assign it to the "myDoubleSeries" variable.

```csharp
private Series<double> myDoubleSeries; // Define a Series<T> variable. In this instance we want it as a double.
private Series<double> mySecondaryDoubleSeries; // Define a Series<T> variable. In this instance we want it as a double.

// Create a Series object and assign it to the variable
protected override void OnStateChange() 
{
    if (State == State.Configure)
    {
        // Add a secondary data series to sync our Secondary Series<double>
        AddDataSeries(BarsPeriodType.Minute, 1);
    }
    else if (State == State.DataLoaded)
    {
        // "this" refers to the NinjaScript object itself. This syncs the Series object to historical data bars.
        // MaximumBarsLookBack determines how many values the Series<double> will have access to.
        myDoubleSeries = new Series<double>(this, MaximumBarsLookBack.Infinite);
        
        // "BarsArray[1]" refers to the first data series added to the script with AddDataSeries.
        mySecondaryDoubleSeries = new Series<double>(BarsArray[1]);
    }
}
```

## Setting Values

You can set the value for the current bar being evaluated by choosing a "barsAgo" value of "0" or, for historical bars, by choosing a "barsAgo" value that represents the number of bars ago that you want the value to be stored at.

```csharp
protected override void OnBarUpdate()
{
    myDoubleSeries[0] = Close[0];
}
```

{% callout type="note" %}  
The "barsAgo" value is only guaranteed to be in sync with the recent current bar during core data event methods, such as OnBarUpdate(), OnMarketUpdate(), and during strategy-related order events such as OnOrderUpdate(), OnExecutionUpdate(), OnPositionUpdate(). For scenarios where you may need to set a value outside of a core data/order event, such as OnRender() or a custom event, you must first synchronize the "barsAgo" pointer via the [TriggerCustomEvent()](triggercustomevent.htm) method.  
{% /callout %}

## Checking for Valid Values

It is possible that you may use a Series<T> object but decide not to set a value for a specific bar. However, you should not try to access a Series<T> value that has not been set. Internally, a dummy value does exist, but you want to check to see if it was a valid value that you set before trying to access it for use in your calculations. Please see [IsValidDataPoint()](isvaliddatapoint.htm) for more information.

{% callout type="warning" %}  
Calling IsValidDataPoint() will only work with a [MaximumBarsLookBackInfinite](maximumbarslookback.htm) series. Attempting to check IsValidDataPoint() on a MaximumBarsLookBack256 series will throw an error. Please check the Log tab of the Control Center.  
{% /callout %}

## Getting Values

You can access Series<T> object values using the syntax Series<T>[int barsAgo] where barsAgo represents the data value n (number of bars ago).

```csharp
protected override void OnBarUpdate()
{
    // Prints the current and last bar value
    Print("The values are " + myDoubleSeries[0] + " " + myDoubleSeries[1]);
}
```

Alternatively, you can access a value at an absolute bar index using the [GetValueAt()](getvalueat.htm) method.

{% callout type="note" %}  
In most cases, you will access the historical price series using a core data event handler such as OnBarUpdate(). For more advanced developers, you may find situations where you wish to access historical price series outside of the core data event methods, such as OnRender(), or your own custom event. In these advanced scenarios, you may run into situations where the "barsAgo" pointer is not in sync with the current bar, and this may result in errors when trying to obtain this information. In those cases, please use the Bars.Get...() methods with the absolute bar index, e.g., [GetValueAt()](getvalueat.htm).  
{% /callout %}

## Methods that Accept ISeries<T> as Arguments

All [indicator methods](indicators.htm) accept ISeries<double> objects as arguments. Carrying from the prior examples, let's print out the 10-period simple moving average of range.

```csharp
protected override void OnBarUpdate()
{
    // Calculate the range of the current bar and set the value
    myDoubleSeries[0] = (High[0] - Low[0]);

    // Print the current 10 period SMA of range
    Print("Value is " + SMA(myDoubleSeries, 10)[0]);         
}
```
