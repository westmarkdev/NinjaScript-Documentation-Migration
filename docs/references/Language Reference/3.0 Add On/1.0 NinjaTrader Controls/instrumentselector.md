---
title: InstrumentSelector
pathName: instrumentselector
parent: controls
section: references
status: imported
---

## Definition

**InstrumentSelector** is a UI element users can interact with for selecting instruments. This can be used with instrument linking between windows.

## Events and Properties

{% table %}

---

* **Cleanup()**
* Disposes of the InstrumentSelector (Note: calling the **[NTTabPage base.Cleanup()](nttabpage_cleanup)** is sufficient to clean up this control)

---

* **Instrument**
* An Instrument representing the selected instrument

---

* **InstrumentChanged**
* Event handler for when the instrument changes on the instrument selector

{% /table }

## Examples

This example demonstrates how to use the instrument selector and properly link its behavior to windows linking.

```csharp
private InstrumentSelector instrumentSelector;
private DependencyObject LoadXAML()
{
    // Note: pageContent (not demonstrated in this example) is the page content of the XAML

    // Find the Instrument selector
    instrumentSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "instrumentSelector") as InstrumentSelector;
    if (instrumentSelector != null)
        instrumentSelector.InstrumentChanged += OnInstrumentChanged;
}

// This method is fired when our instrument selector changes instruments
private void OnInstrumentChanged(object sender, EventArgs e)
{
    Instrument = sender as Cbi.Instrument;
}

// IInstrumentProvider member. Required if you want to use the instrument link mechanism in this Add On window
public Cbi.Instrument Instrument
{
    get { return instrument; }
    set
    {
        instrument = value;
        if (instrumentSelector != null)
            instrumentSelector.Instrument = value;

        // Send instrument to other windows linked to the same color
        PropagateInstrumentChange(value);
    }
}

// NOTE: Don't forget to clean up resources and unsubscribe to events
// Called by TabControl when tab is being removed or window is closed
public override void Cleanup()
{
    // Clean up our resources
    if (instrumentSelector != null)
    {
        instrumentSelector.InstrumentChanged -= OnInstrumentChanged;
    }
    base.Cleanup();

```

```xaml
<page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:accountdata="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui" xmlns:accountperformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui" xmlns:atmstrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui" xmlns:tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">

<grid>
    <grid.columndefinitions>
        <columndefinition width="Auto"></columndefinition>
        <columndefinition width="*"></columndefinition>
    </grid.columndefinitions>
    <tools:instrumentselector grid.column="0" lastusedgroup="MyAddOn" x:name="instrumentSelector"></tools:instrumentselector>
</grid>
</page>
```
