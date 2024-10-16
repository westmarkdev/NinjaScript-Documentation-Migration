---
title: "CloseStrategy()"
pathName: /docs/desktop/closestrategy
---

## Definition

Cancels all working orders, closes any existing positions, and finally disables the strategy. This behavior can also be overridden for a given strategy if desired.

{% callout type="note" %}
• If you choose to override this method using custom logic, the default behavior of the CloseStrategy() method will NOT be executed. For this reason, it is suggested to call the base implementation of CloseStrategy() method within the virtual override to ensure that the strategy is terminated as designed, otherwise it is your responsibility to correctly manage any working orders or positions.

• CloseStrategy() will work off the current strategy position and will not factor in any [StartBehavior](/docs/desktop/startbehavior) setting, i.e., calling CloseStrategy() while the script is in a virtual historical position could result in an unwanted position.

• The default CloseStrategy() handling will be applied to all series of a MultiSeries NinjaScript strategy.
{% /callout %}

## Method Return Value

This method does not return a value.

### Syntax

```csharp
CloseStrategy(string signalName)
```

{% callout type="warning" %}
This method can only be called before the [State](/docs/desktop/state) has reached [State.Terminated](/docs/desktop/state) and after the [State](/docs/desktop/state) reaches [State.Realtime](/docs/desktop/state).
{% /callout %}

You may choose to override this method using the following syntax:

```csharp
public override void CloseStrategy(string signalName)
{
}
```

## Parameters

|  |  |
| --- | --- |
| signalName | The signal name which will be used to identify the closing order. If no signal name exists or is null, "Close" will be substituted instead. |

## Examples

### Basic usage of CloseStrategy

```csharp
DateTime StartTime = new DateTime();

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {                
        Name = "ExampleStrategy";  
    }
    else if (State == State.Transition)
        StartTime = Core.Globals.Now;       
}  

protected override void OnBarUpdate()
{
    // if we're still in position 45 minutes after the start time, close strategy
    if (Position.MarketPosition != MarketPosition.Flat && Time[0] >= StartTime.AddMinutes(45))
        CloseStrategy("My Custom Close");
}
```

### Overriding the default CloseStrategy logic

```csharp
public override void CloseStrategy(string signalName)
{
    Print("Executing Custom Close Logic");
    // custom close logic
    // call default close action
    base.CloseStrategy(signalName);
}
```
