---
title: "PropagateInstrumentChange()"
pathName: /docs/desktop/propagateinstrumentchange
---

## Definition

In an [NTWindow](/docs/desktop/ntwindow), `PropagateInstrumentChange()` sends an Instrument to other windows with the same Instrument Linking color configured.

{% callout type="note" %}
&bull; A public Instrument property must be defined in order to use `PropagateInstrumentChange()`, as in the example below. {% <br> %} 
&bull; For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](/docs/desktop/developing_add_ons).
{% /callout %}

## Example

```csharp
// IInstrumentProvider member. Required if you want to use the instrument link mechanism on an NTWindow.
public Cbi.Instrument Instrument
{
    get { return instrument; }
    set
    {
        // Process logic related to switching instruments, such as:
        // Unsubscribe to subscriptions to old instruments...
        // Subscribe for the new instrument...
        // Change the value displayed in an Instrument Selector in the NTWindow...
        // Update the tab header name on AddOnFramework to be the same name as the new instrument...
        // etc...
        // Send instrument to other windows linked to the same color
        PropagateInstrumentChange(value);
    }
}
```
