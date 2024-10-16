---
title: "IsSuspendedWhileInactive"
pathName: /docs/desktop/issuspendedwhileinactive
---

## Definition

Prevents OnBarUpdate from being raised while the indicators display is not in use. Enabling this property in your indicator helps save CPU cycles while the indicator is suspended and not in use by a user. Once the indicator is in a state that would no longer be considered suspended, the historical OnBarUpdate() events will be triggered allowing the indicator to catch up to current real-time values.

Suspension occurs in the following scenarios:

&bull; Minimized Chart{% <br> %}
&bull; Minimized Market Analyzer{% <br> %}
&bull; Minimized Hot List Analyzer{% <br> %}
&bull; Minimized SuperDOM{% <br> %}
&bull; Background tabs of above features are considered "minimized"{% <br> %}
&bull; Inactive workspaces in the background

{% callout type="note" %}
Since events in OnBarUpdate() will not be processed while the indicator is suspended, internal NinjaScript functions such as [Alert()](/docs/desktop/alert), [PlaySound()](/docs/desktop/playsound), [Share()](/docs/desktop/share), [Print()](/docs/desktop/print), etc - or any other method that would be used to notify a user of activity will NOT be processed until the indicator is un-suspended.
{% /callout %}

## Scenarios Where Suspension Will Not Occur

The IsSuspendedWhileInactive property will be ignored and real-time events will be processed as normal under the following cases:

&bull; Indicators running in [Automated NinjaScript Strategies](/docs/desktop/running_a_ninjascript_strategy){% <br> %}
&bull; Indicators which have [manually configured alerts](/docs/desktop/alerts_dialog){% <br> %}
&bull; Indicators which have been [manually attached to orders](/docs/desktop/attachingorderstoindicators)

## Property Value

This property returns true if the indicator can take advantage of suspension optimization; otherwise, false. Default set to false.

{% callout type="note" %}
This property is overridden to "true" automatically by the [NinjaScript Code Wizard](/docs/desktop/ns_wizard). You will need to remove the property to return to the default value or manually set it to false to disable this behavior.
{% /callout %}

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](/docs/desktop/onstatechange) method during State.SetDefaults or State.Configure.
{% /callout %}

## Syntax

IsSuspendedWhileInactive

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsSuspendedWhileInactive = true;
    }
}
```
