---

title: ninjascript_best_practices
pathName: ninjascript_best_practices
created: Thursday, October 3rd 2024, 11:29:09 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Overview

There are some best practices to be aware of when developing NinjaScript classes. The following sections present a non-exhaustive list of considerations to keep in mind when designing and implementing your code.

{% callout type="note" %}  
Note: NinjaTrader is multi-threaded and event driven. Always assume that any of the methods you implement in NinjaScript could be called from another thread.  
{% /callout %}

## State Management Practices

### Managing Resources

The [`OnStateChange`](onstatechange.htm) method is called anytime there has been a change of [State](state.htm) and can be used to help you set up, manage, and destroy several types of resources.

#### Setting Default UI Property Grid Values

Reserve `State.SetDefaults` for defaulting any public properties you wish to have exposed on the UI property grid. You should also use this State for setting default desired NinjaScript property behavior which can be overridden from the property grid (e.g., [`Calculate`](calculate.htm), [`IsOverlay`](isoverlay.htm), etc.). For Plots and Lines you wish to configure, [`AddPlot()`](addplot.htm) and [`AddLine()`](addline.htm) should also have their default values set during this State.

| Reason |
| --- |
| Public values of the NinjaScript object in `SetDefaults` are pushed to the UI property grid for an opportunity to change settings of your object. |

#### Best Practice Code Example

```csharp
protected override void OnStateChange()
{
    // These are the values that show up as default on the UI
    if (State == State.SetDefaults)
    {
        Calculate = Calculate.OnPriceChange;
        IsOverlay = false;
        Period = 50;
        AddPlot(Brushes.Blue, "Plot Value");
        AddLine(Brushes.Gray, 100, "Threshold");
    }
}
```

**For public properties you do NOT wish exposed to the UI property grid, set the `Browsable` attribute to false:**

```csharp
[Browsable(false)] // prevents from showing up on the UI property grid
public int Communicator { get; set; }
```

### Calculating Run-Time Object Values

Do not attempt to do advanced calculations or try to access object references in `State.SetDefaults`. This state should be kept as lean as possible, and any calculation logic should be delayed until at least `State.Configure`.

| Reason |
| --- |
| Your object will be called in situations you may not be expecting. You can read more about this subject on [Understanding the life cycle of your NinjaScript objects](understanding_the_lifecycle_of.htm). |

#### Avoid Practice Code Example

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Logic could take longer than desired as the list of indicator names is populated
        for (int i = 0; i <= array.length; i++)
            DoWork(i);
        
        // Possible null reference exception since TickSize is not set yet
        Period = 5 * TickSize;
    }
}
```

#### Best Practice Code Example

```csharp
protected override void OnStateChange()
{
    // Complex operations should be delayed to >= State.Configure
    if (State == State.Configure)
    {
        for (int i = 0; i <= array.length; i++)
            DoWork(i);
    }
    
    // Information related to market data is not available until at least State.DataLoaded
    else if (State == State.DataLoaded)
    {
        Period = 5 * TickSize;
    }
}
```

## Performance Practices

### Referencing Indicator Methods

In general, when calling an Indicator return method, there is some internal caching which occurs by design to help reduce memory consumption.

#### Practice to Avoid

```csharp
// Each time you call the SMA() return method there is a small performance cost
if (Close[0] > SMA(20)[0])
{
    Print(SMA(20)[0]);
    EnterLongLimit(SMA(20)[0]);
    Draw.Dot(this, Time[0].ToString(), false, 0, SMA(20)[0], Brushes.DarkGreen);
}
```

#### Best Practice Code Example

```csharp
private SMA mySma;

protected override void OnStateChange()
{
    // When the indicator begins processing, save an instance of the SMA indicator with the desired input
    if (State == State.Historical)
    {
        mySma = SMA(20);
    }
}

protected override void OnBarUpdate()
{
    // Use the referenced mySMA throughout the lifetime of the script
    if (Close[0] > mySma[0])
    {
        Print(mySma[0]);
        EnterLongLimit(mySma[0]);
        Draw.Dot(this, Time[0].ToString(), false, 0, mySma[0], Brushes.DarkGreen);
    }
}
```

### Miscellaneous Practices

**Floating-point Comparison**

Be aware of floating-point precision problems. It can sometimes be more reliable to check within a certain degree of tolerance, such as the [`TickSize`](ticksize.htm).

#### Practice to Avoid

```csharp
// Depending on how Value[0] was calculated, it could be off by a degree of floating points
if (Value[0] == Close[0])
{
    // do something
}
```

#### Best Practice Code Example

```csharp
// You can avoid these precision issues by rewriting the comparison to evaluate within a certain tolerance.
if (Math.Abs(Value[0] - Close[0]) < TickSize)
{
    // do something
}

// NinjaTrader developed objects use a custom Extension Method
// double.ApproxCompare() which Returns an int based on an Epsilon value:
if (Close[0].ApproxCompare(Value[0]) == 0)
{
    // do something
}
```

This document includes essential best practices when developing with NinjaScript. Adhering to these practices will facilitate better performance, maintainability, and reliability in your NinjaScript implementations.
