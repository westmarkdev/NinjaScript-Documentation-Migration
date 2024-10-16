---
title: "ForceRefresh()"
pathName: forcerefresh
---

## Definition

Resets an internal marker used to determine if the chart visuals need to re-render.

[ChartControl](chartcontrol) runs a timed event every 250ms to determine the chart needs to be updated. If it does, the [OnRender()](onrender) method is called. Under normal circumstances, the marker used to call OnRender() will be reset after the following conditions:

- [OnBarUpdate()](onbarupdate) event
- [OnConnectionStatusUpdate()](onconnectionstatusupdate) event
- User clicks on the chart
- Drawing object(s) have been removed from the chart
- Strategy enabled/disabled on chart
- ChartTrader enabled/disabled

In most cases, the conditions listed above should be satisfactory for rendering standard and custom chart objects; however, for more advanced programming concepts, there may be other situations you run into which would NOT force the chart to refresh (e.g., a user interacting with a custom control). In these special cases, you can use the ForceRefresh() method to re-queue the render event.

{% callout type="note" %}
As the chart is optimized on a timer, calling ForceRefresh() will NOT immediately trigger a render event. Calling ForceRefresh() simply re-queues the render event to trigger during the next timed event. In other words, it may take up to 250ms for the render event to function.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
ForceRefresh()
```

{% callout type="warning" %}
Excessive calls to ForceRefresh() and OnRender() can carry an impact on general application performance. You should only call ForceRefresh() if the chart truly needs to be visually updated. It is NOT recommended to invalidate the chart control directly as this could cause issues with threading which result in deadlocks.
{% /callout %}

## Method Parameters

This method does not accept any parameters.

## Examples

```csharp
DateTime lastTimeCalled = DateTime.MinValue;

private void MyCustomMethod()
{
    // if it has been longer than one second since the last time
    // this method was called update the chart visually
    if (Core.Globals.Now.Subtract(lastTimeCalled).Seconds >= 1)
    {
        ForceRefresh();
        lastTimeCalled = Core.Globals.Now;
    }
}
```
