---
title: CleanUp()
pathName: nttabpage_cleanup
parent: nttabpage
section: references
status: changed
---

## Definition

Unregisters LinkControls (**IInstrumentProvider**) and calls **Cleanup()** on **ICleanable** controls on the **NTTabPage**. Override this to, e.g., unsubscribe from events or perform any other cleanup operations when the tab is closed.

{% callout type="note" %}

When overriding **Cleanup()**, it is strongly recommended when you call **base.Cleanup()** which ensures any link controls are also unregistered. The base implementation will also handle cleaning up any controls which implement **ICleanable**: **AccountSelector**, **AtmStrategySelector**, **InstrumentSelector**, **IntervalSelector**, **TifSelector**.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**public override void Cleanup()**

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
