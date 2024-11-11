---
title: Other Uses for an AddOn
pathName: other_uses_for_an_addon
parent: educational_resources
section: guides
status: imported
---

## Modifying Existing NinjaTrader Windows

To modify an existing type of NinjaTrader window (for example, to add a button to all charts), you will first need to obtain a reference to each individual window of that type that is open. This can be done by overriding the **OnWindowCreated()** method, then declaring an object of the Type of the window you are looking for, and finally assigning the object a reference to the Window passed into the method:

```csharp
// OnWindowCreated() will be called any time a new NTWindow is created. It will be called in the thread of that window
protected override void OnWindowCreated(Window window)
{
   // Declare a Chart object and instantiate it to the Window passed into the method
   Gui.Chart.Chart myChart = window as Gui.Chart.Chart;
    
   // Use this check to return if the calling Window is not of the Type you are looking for
   if (myChart == null)
       return;
}
```

If you are unsure of the Type name for a particular type of window, you can open an instance of that window then run the code below, which will print the Type to the Output Window:

```csharp
protected override void OnWindowCreated(Window window)
{
   // Print the Type of any open windows, for future reference
   Print(window.ToString());
}
```

Once you've obtained a reference to a window, you can then directly manipulate the WPF grids, controls, and other elements to customize its user interface or functionality. For example, if your goal was to add a new button to Chart Trader on all charts, you could use your reference to Chart objects to first locate their attached Chart Trader instances, then place a custom-defined button directly into the WPF grid used to lay out buttons in Chart Trader. Since this code would run within **OnWindowCreated()**, it would be applied to every Chart Trader instance that is open. You would not be changing the format used to create Chart Traders in the first place, but would rather be detecting every open instance and adding the buttons into them. This is an important distinction to make, because this approach requires that you also remove the elements you've added when each window is destroyed.

```csharp
// Declare a Chart, ChartTrader, and UI elements to add to Chart Trader
Gui.Chart.Chart myChart;
Gui.Chart.ChartTrader chartTrader;
Button sampleButton;
Grid myGrid;
Grid mainGrid;
 
protected override void OnWindowCreated(Window window)
{
   // Instantiate myChart by assigning a reference to the calling Window
   myChart = window as Gui.Chart.Chart;
 
   if (myChart == null)
   {
       return;
   }
 
   //find chart trader from myChart's Chart Control by its Automation ID: "ChartWindowChartTrader"
   chartTrader = Window.GetWindow(myChart.ActiveChartControl.Parent).FindFirst("ChartWindowChartTraderControl") as Gui.Chart.ChartTrader;
 
   if (chartTrader == null)
   {
       return;
   }
 
   // Instantiate sampleButton
   sampleButton = new Button
   {
       Content = "Sample Button",
       Style = System.Windows.Application.Current.TryFindResource("Button") as Style
   };
 
   // Attach a custom event handler to the .Click event
   sampleButton.Click += SampleButton_Click;
 
   // Set a custom AutomationId for the button, so that it can be referenced elsewhere the same way we found Chart Trader
   System.Windows.Automation.AutomationProperties.SetAutomationId(sampleButton, "SampleButton");
 
   //this is the main chart trader grid where the default buttons and controls reside
   mainGrid = chartTrader.FindName("grdMain") as Grid;
 
   // Return if Chart Trader is null
   if (mainGrid == null)
   {
       return;
   }
 
   // by default, there will be 7 rows in Chart Trader, we need to add a new row for the new button
   if (mainGrid.RowDefinitions.Count <= 7)
       mainGrid.RowDefinitions.Add(new RowDefinition());
 
   //define a new grid, and add our button to that grid
   myGrid = new Grid();
   myGrid.Children.Add(sampleButton);
 
   //set my grid to the new row 
   Grid.SetRow(myGrid, 8);
 
   //finally, add our grid to the main grid
   mainGrid.Children.Add(myGrid);
}
 
private void SampleButton_Click(object sender, RoutedEventArgs e)
{
   Print("Sample Button Clicked");
}
```

Since we are dynamically adding elements to open windows, it is important to clean up any unused resources and detach any event handlers when the affected windows are destroyed. You can use the same approach as shown above to obtain a reference to each affected window within the **OnWindowDestroyed()** method:

```csharp
protected override void OnWindowDestroyed(Window window)
{
   // Return if there is no button, or if the destroyed window is not a chart
   if(sampleButton == null || !(window is Gui.Chart.Chart))
   {
       return;
   }
 
   // Detach the event handler from the .Click event, remove the grid, and nullify the button
   sampleButton.Click -= SampleButton_Click;
   mainGrid.Children.Remove(myGrid);
   sampleButton = null;
}
```

Below is another example of adding elements into chart windows. In this example, we add a new panel to the top of all chart windows, then take all existing chart content and move it into a row beneath the panel we've just added:

```csharp
protected override void OnWindowCreated(Window window)
{
   // Obtain a reference to any chart that triggered OnWindowCreated
   Chart Window = window as Chart;
    
   // Instantiate a grid to hold a reference to the content of the chart window
   Grid mainWindowGrid = Window.Content as Grid;
    
   // Add existing row definition for existing row if it is not present
   if (mainWindowGrid.RowDefinitions.Count == 0)
   {
       mainWindowGrid.RowDefinitions.Add(new RowDefinition());
   }
                
   // Instantiate a RowDefinition and set its height
   RowDefinition row = new RowDefinition();
   row.Height = new GridLength(PanelLength);
    
   // Insert the new row into the chart's main window grid
   mainWindowGrid.RowDefinitions.Insert(0, row);
    
   //Move Existing Elements down one row, since our new content will take the top row
   foreach (UIElement element in mainWindowGrid.Children)
   {
       element.SetValue(Grid.RowProperty, (int)element.GetValue(Grid.RowProperty) + 1);
   }
    
   //Create the Top Panel grid and add it to our newly defined row
   Grid Panel = new Grid();
   Panel.SetValue(Grid.RowProperty, 0);
   mainWindowGrid.Children.Add(Panel);
 
   //Create a sample text block and add it to the Top/Bottom Panel Grid.
   TextBlock TextBlock = new TextBlock();
   TextBlock.Text = PanelDirection.ToString() + " Panel (" + PanelLocation.ToString() + ") Sample Text Block";
   TextBlock.Foreground = Brushes.Red;
   TextBlock.SetValue(Grid.RowProperty, 0);
   Panel.Children.Add(TextBlock);
}
```

## Accessing Account Data

From time to time, you may need to access certain global data, such as account values, order states, position info, etc. In these cases, you can subscribe to an appropriate event using a custom event handler method. Below is a list of a few such events which can be captured:

{% table %}

* Method

* Description

---

* <`account`>.[AccountItemUpdate](accountitemupdate)

* Triggers on account item updates

---

* <`account`>.[ExecutionUpdate](executionupdate)

* Triggers on any execution

---

* <`account`>.[OrderUpdate](orderupdate)

* Triggers on any order state changes

---

* <`account`>.[PositionUpdate](positionupdate)

* Triggers on any position updates

---

{% /table %}

```csharp
// Custom Subscribe() method to refresh subscriptions
private void Subscribe()
{
   if (myAccount != null)
   {
       // Unsubscribe to any prior account subscriptions
       myAccount.AccountItemUpdate -= OnAccountItemUpdate;
       myAccount.ExecutionUpdate -= OnExecutionUpdate;
       myAccount.OrderUpdate -= OnOrderUpdate;
       myAccount.PositionUpdate -= OnPositionUpdate;
 
       // Subscribe to new account subscriptions
       myAccount.AccountItemUpdate   += OnAccountItemUpdate;
       myAccount.ExecutionUpdate     += OnExecutionUpdate;
       myAccount.OrderUpdate         += OnOrderUpdate;
       myAccount.PositionUpdate     += OnPositionUpdate;
   }
}
 
private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
   // Handle account item updates
}
 
private void OnExecutionUpdate(object sender, AccountItemEventArgs e)
{
   // Handle execution updates
}
 
private void OnOrderUpdate(object sender, AccountItemEventArgs e)
{
   // Handle order updates
}
 
private void OnPositionUpdate(object sender, AccountItemEventArgs e)
{
   // Handle position updates
}
```

## Accessing Market Data

Market data can be accessed via a **BarsRequest** object, which can provide real-time or snapshot data for use by your classes. A **BarsRequest** object can be loaded with a series of bar data without the need to actually draw bars on a chart. The **BarsRequest** object can then be accessed via the **BarsUpdateEventArgs** object passed into your event handler via the **BarsRequest's** Update method. The process for using a **BarsRequest** is as follows:

1. Instantiate an **Instrument** object
2. Instantiate and parameterize a **BarsRequest** object
3. Hook the **BarsRequest's** Update event to a custom event handler
4. Call the **BarsRequest's** Request() method
5. Access bars data directly from the **BarsRequest** object within your event handler method

```csharp
// Custom method to perform a BarsRequest
private NinjaTrader.Data.BarsRequest DoBarsRequest(Instrument instrument, int lookBackPeriod)
{
   // Declare a BarsRequest object
   NinjaTrader.Data.BarsRequest barsRequest;
    
   // Request x number of days back of data.
   barsRequest = new NinjaTrader.Data.BarsRequest(instrument, DateTime.Now.AddDays(-lookBackPeriod), DateTime.Now);
 
   // If you wish to request x number of bars back instead you can use this signature:
   // barsRequest = new NinjaTrader.Data.BarsRequest(instrument, lookBackPeriod);
    
 
   // Parameterize the request
   barsRequest.BarsPeriod = new NinjaTrader.Data.BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 60 };
   barsRequest.TradingHours     = NinjaTrader.Data.TradingHours.Get("Default 24 x 7");
    
   // Additional parameters which could be set
   // barsRequest.IsDividendAdjusted      = true;
   // barsRequest.IsResetOnNewTradingDay   = false;
   // barsRequest.IsSplitAdjusted         = true;
   // barsRequest.LookupPolicy            = LookupPolicies.Provider;
   // barsRequest.MergePolicy            = MergePolicy.DoNotMerge;
 
   // Attach event handler for real-time events if you want to process real-time data
   barsRequest.Update     += MyOnBarUpdate;
    
   // Call the Request method on the BarsRequest object to request the bars
   barsRequest.Request(new Action<ninjatrader.data.barsrequest, errorcode,="" string="">((bars, errorCode, errorMessage) =>
   {
       Dispatcher.InvokeAsync(new Action(() =>
       {
           if (errorCode != ErrorCode.NoError)
           {
               // Handle any errors in requesting bars here
               outputBox.Text = string.Format("Error on requesting bars: {0}, {1}", errorCode, errorMessage);
               return;
           }
       }));
   }));
    
   // Return the Bars Request to any callers of this method
   return barsRequest;
}
 
// BarsUpdateEventArgs is provided by the BarsRequest's Update event
private void MyOnBarUpdate(object sender, NinjaTrader.Data.BarsUpdateEventArgs e)
{
   /* Dispatcher.InvokeAsync() is needed for multi-threading considerations. When processing events outside of the UI thread, and we want to
    influence the UI .InvokeAsync() allows us to do so. It can also help prevent the UI thread from locking up on long operations. */
   Dispatcher.InvokeAsync(() =>
   {
       /* Depending on the BarsPeriod type of your barsRequest you can have situations where more than one bar is updated by a single tick
        Be sure to process the full range of updated bars to ensure you did not miss a bar. */
 
       // Process updated bars on each tick
       for (int i = e.MinIndex; i <= e.MaxIndex; i++)
       {
           // Processing every single tick
           outputBox.Text = string.Format("REALTIME BARS{0}Time: {1}{0}Open: {2}{0}High: {3}{0}Low: {4}{0}Close: {5}",
               Environment.NewLine,
               e.BarsSeries.GetTime(i),
               e.BarsSeries.GetOpen(i),
               e.BarsSeries.GetHigh(i),
               e.BarsSeries.GetLow(i),
               e.BarsSeries.GetClose(i));
       }
   });
}
```
