---
title: TifSelector
pathName: tifselector
parent: controls
section: references
status: imported
---

## Definition

**TifSelector** can be used as a UI element users can interact with for selecting TIF.

## Events and Properties

{% table %}

---

* **Cleanup()** | Disposes of the **TifSelector** (Note: calling the [NTTabPage base.Cleanup()](nttabpage_cleanup) is sufficient to clean up this control)

---

* **SelectedTif** | A **TimeInForce** representing the selected TIF  
	- Possible values:  
	- **TimeInForce.Day**  
	- **TimeInForce.Gtc**  
	- **TimeInForce.Gtd**  
	- **TimeInForce.Ioc**  
	- **TimeInForce.Opg**

---

* **SelectionChanged** | Event handler for when the selected ATM strategy has changed
{% /table %}

## Examples

This example demonstrates how to use the **TIF selector** and properly link its behavior with the quantity up/down and TIF selectors.

```csharp
private QuantityUpDown                  qudSelector;

private TifSelector                     tifSelector;

private AtmStrategy.AtmStrategySelector atmStrategySelector;

private DependencyObject LoadXAML()

{

    // Note: pageContent (not demonstrated in this example) is the page content of the XAML

    // Find the Quantity Up-Down selector

    qudSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "qudSelector") as QuantityUpDown;

    // Find the TIF selector

    tifSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "tifSelector") as TifSelector;

    // Be sure to bind our account selector to our TIF selector to ensure proper functionality

    tifSelector.SetBinding(TifSelector.AccountProperty, new Binding { Source = accountSelector,  
         Path = new PropertyPath("SelectedAccount") });

    // When our TIF selector's selection changes

    tifSelector.SelectionChanged += (o, args) =>

    {

        // Change the selected TIF in the ATM strategy too

        if (atmStrategySelector.SelectedAtmStrategy != null)

              atmStrategySelector.SelectedAtmStrategy.TimeInForce = tifSelector.SelectedTif;

    };

    // Find ATM Strategy selector and attach event handler

    atmStrategySelector = LogicalTreeHelper.FindLogicalNode(pageContent, "atmStrategySelector") as AtmStrategy.AtmStrategySelector;

    atmStrategySelector.Id = Guid.NewGuid().ToString("N");

    if (atmStrategySelector != null)

         atmStrategySelector.CustomPropertiesChanged += OnAtmCustomPropertiesChanged;

    // Be sure to bind our account selector to our ATM strategy selector to ensure proper functionality

    atmStrategySelector.SetBinding(AtmStrategy.AtmStrategySelector.AccountProperty,

        new Binding { Source = accountSelector, Path = new PropertyPath("SelectedAccount") });

    // When our ATM selector's selection changes

    atmStrategySelector.SelectionChanged += (o, args) =>

    {

        if (atmStrategySelector.SelectedItem == null)

              return;

        if (args.AddedItems.Count > 0)

         {

              // Change the selected TIF in our TIF selector too

              AtmStrategy selectedAtmStrategy = args.AddedItems[0] as AtmStrategy;

              if (selectedAtmStrategy != null)

                   tifSelector.SelectedTif = selectedAtmStrategy.TimeInForce;

         }

 };

}

private void OnAtmCustomPropertiesChanged(object sender, NinjaScript.AtmStrategy.CustomPropertiesChangedEventArgs args)

{

    // Adjust our TIF and Quantity selectors to the new ATM strategy values

    tifSelector.SelectedTif = args.NewTif;

    qudSelector.Value = args.NewQuantity;

}

// NOTE: Don't forget to clean up resources and unsubscribe to events

// Called by TabControl when tab is being removed or window is closed

public override void Cleanup()

{

  // Clean up our resources  
    base.Cleanup();

}
```

```xaml
<Page        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"

 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"

 xmlns:Tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui"

 xmlns:AccountPerformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui"

 xmlns:AccountData="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui"

 xmlns:AtmStrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui">

<Grid>

    <Grid.ColumnDefinitions>

         <ColumnDefinition Width="Auto"/>

         <ColumnDefinition Width="Auto"/>

         <ColumnDefinition Width="*"/>

    </Grid.ColumnDefinitions>

    <Tools:QuantityUpDown x:Name="qudSelector" Value="1" Grid.Column="0"/>

    <Tools:TifSelector x:Name="tifSelector" Grid.Column="1"/>

    <AtmStrategy:AtmStrategySelector x:Name="atmStrategySelector" LinkedQuantity="{Binding Value,

    ElementName=qudSelector, Mode=OneWay}" Grid.Column="2"/>

</Grid>
```
