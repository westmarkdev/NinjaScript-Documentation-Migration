---
title: "CleanUp()"
pathName: /docs/desktop/nttabpage_cleanup
---

## Definition

Unregisters LinkControls ([IInstrumentProvider](/docs/desktop/iintervalprovider_interface) and [IIntervalProvider](/docs/desktop/iintervalprovider_interface)) and calls Cleanup() on ICleanable controls on the NTTabPage. Override this to, e.g., unsubscribe from events or perform any other cleanup operations when the tab is closed.

{% callout type="note" %}
When overriding Cleanup(), it is strongly recommended to call base.Cleanup() which ensures any link controls are also unregistered. The base implementation will also handle cleaning up any controls which implement ICleanable: [AccountSelector](/docs/desktop/accountselector), [AtmStrategySelector](/docs/desktop/atmstrategyselector), [InstrumentSelector](/docs/desktop/instrumentselector), [IntervalSelector](/docs/desktop/intervalselector), [TifSelector](/docs/desktop/tifselector).
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
public override void Cleanup()
{
}
```

## Parameters

This method does not accept any parameters.

## Examples

```csharp
public override void Cleanup()
{
    // unregister from any custom events
    Connection.ConnectionStatusUpdate -= OnConnectionStatusUpdate;

    // a call to base.Cleanup() will loop through the visual tree looking for all ICleanable children
    // i.e., AccountSelector, AtmStrategySelector, InstrumentSelector, IntervalSelector, TifSelector,
    // as well as unregister any link control events
    base.Cleanup();
}
```

