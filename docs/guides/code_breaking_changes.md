---
title: Code Breaking Changes
pathName: code_breaking_changes
parent: 
order: 2
section: guides
status: removed
---

The following document is intended as a high level overview of the **NinjaScript** changes you can expect between **NinjaTrader 7** and **NinjaTrader 8**. For specific information on a particular method or property, you can refer to the dynamically formatted Code Breaking table at the bottom of this page. We recommend using the Filter and Sorting features built into the table, as well checking the Summary column and expanding the Details section of each entry for general information. Referring to the conveniently linked **NinjaTrader 8** and **NinjaTrader 7** documentation will provide specific information on syntax, usage, and examples of any new implementation or element names.

{% callout type="note" %}

Information on this page focuses on supported (documented) **NinjaTrader** methods and properties shared between versions. **NinjaTrader 8** has seen a significant increase in supported **NinjaTrader** code, however if you were using previously undocumented **NinjaTrader 7** methods or properties, they will NOT be covered in this topic. You may be able to find more information on previously undocumented methods and properties in the **NinjaTrader 8 Help Guide**, or our support staff will also be happy to personally point you in the right direction.

{% /callout %}

{% callout type="warning" %}

Critical: If your product uses unsupported (undocumented) elements we strongly urge you to put your scripts through thorough testing to ensure they still behave as expected. There is NO guarantee that previously undocumented method or property behavior has not changed in the new version of **NinjaTrader 8**.

{% /callout %}

For questions or comments, please contact us at **<platformsupport@ninjatrader.com>**.

## Implementation Changes Overview

{% table %}

* Method
* Description

---

* **Initialize()**, **OnStartUp()**, **OnTermination()**
**NinjaTrader 8** has simplified the methods used to set or release various resources during the lifetime of a **NinjaTrader** object to a single **OnStateChange()** method. This single method is guaranteed to be called for every change in State of the object. It is from this method you can monitor the progression of the object throughout its lifetime in order to setup various resources, set properties, or take action the moment State has changed. This method also exposes a **State** variable which can be used in various other methods, such as **OnBarUpdate()**, in order to tell your indicator or strategy to process data depending on the actual State of the object.

---

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     // set the default properties
     Name = "My Indicator";
     Fast = 10;
     Slow = 25;
     IsOverlay = true;
     IsAutoScale = true;
   }
}
```

If you have custom resources that need to be setup before the **NinjaTrader** object is active and processing data, instead of using the **Initialize()** method, you can now set this up once the **OnStateChange()** method has reached **State.Configure** state:

```csharp
protected override void OnStateChange()
{
   if (State == State.Configure)
   {
     // Add a 5 minute Bars object to the strategy
     AddDataSeries(Data.BarsPeriodType.Minute, 5);
     // setup a custom data series
     spread = new Series<double>(this);
     // setup a 20-period EMA indicator
     ema = EMA(20);
     // add indicator to strategy for visual purposes
     AddChartIndicator(ema);
   }
}
```

**NinjaTrader 7** had no concept to detect when your **NinjaTrader** object was transitioning from processing Historical data to processing Real-time data. Now with **NinjaTrader 8**, the **OnStateChange()** method provides a **State.Transition** state which will notify you when this change is about to occur. If your **NinjaTrader 7** indicators or strategies were using custom methods to try to detect this transition, your custom methods may be refactored under this new state:

```csharp
protected override void OnStateChange()
{
   if (State == State.Transition)
   {
     Print("We're going to real-time data...");
     // setup your real-time data resources here
   }
}
```

When your **NinjaTrader** object is shutting down, and you need to clean up any custom device resources, instead of using **OnTermination()**, you should now clean up these resources once the **OnStateChange()** method has reached the **State.Terminated** state:

```csharp
protected override void OnStateChange()
{
   if (State == State.Terminated)
   {
     // release any device resources
     if(myTimer != null)
         myTimer = null;
   }
}
```

**NinjaTrader** previously used a Historical bool property to notify when an indicator or strategy bar was being processed historically or real-time. The **NinjaTrader 8** **OnStateChange()** approach has now introduced a class level variable **State** where you can check for **State.Historical** or **State.Realtime** in any of the other event methods which will allow you to take action depending on the desired state:

```csharp
protected override void OnBarUpdate()
{
   // only process on real-time data
   if (State == State.Historical)
     return;
   else if (State >= State.Realtime)
       // rest of logic
}
```

### Strategies, Orders, and Accounts

Low level access has been provided to allow more flexibility with the information pertaining to trade data.

* **IOrders**, **IExecution**, and **IPosition** interfaces have all been replaced directly with the corresponding object.
* The signatures of the related **NinjaScript** events have changed to match the **NinjaTrader** internal Update events.
* Methods now return and update with the object instance generated, instead of the previously used interface.

{% table %}

* Tip
* Description

---

* Tip: Since **NinjaTrader 8** now exposes the direct Order object, rather than an **IOrder** interface, it is possible to receive null object reference errors if you attempt to access an order object before the entry or exit order method has returned. To prevent these situations, it is recommended to assign your strategies Order variables in the **OnOrderUpdate()** method and match them by their signal name (**order.Name**). Please see the example beginning on line #22 below for demonstration of assigning order objects to private variables.
{% /table %}

```csharp
Order myOrder = null;
protected override void OnBarUpdate()
{
   if (Position.MarketPosition == MarketPosition.Flat && myOrder == null)
     EnterLongLimit(Low[0], "Entry");

   if (myOrder != null)
   {
     Print(myOrder.OrderState);

     if (myOrder.OrderState == OrderState.Cancelled || myOrder.OrderState == OrderState.Filled)
         myOrder = null;
   }
}
```

```csharp
protected override void OnOrderUpdate(Cbi.Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, Cbi.OrderState orderState, DateTime time, Cbi.ErrorCode error, string comment)
{
   // compare the order object created via EnterLongLimit by the signal name
   if (myOrder == null && order.Name == "Entry")
   {
     // assign myOrder to matching order update
     myOrder = order;
   }
}
```

### Data Series

Previously there had been type specific Data Series implementations (e.g., **IntSeries**, **TimeSeries**, **BoolSeries**, etc). Now there just is a template **Series`<t>`** class which could be used generically and even allows support for additional types:

```csharp
Series<double> mySeries = new Series<double>(this);
Series<datetime> myTimeSeries = new Series<datetime>(this);
```

The **DataSeries.Set()** method used to assign Data Series or Plot values has been removed and values can now be stored using a single assignment operator:

```csharp
protected override void OnBarUpdate()
{
   // set public plotting data series close value of current bar
   MyPlot[0] = Close[0];
   // set custom Series<datetime> to time value of current bar
   myTimeSeries[0] = Time[0];
}
```

### Drawing

The **DrawObjects** used in **NinjaTrader** have received a number of changes:

* All **DrawObjects** have been moved to a separate **NinjaScript.DrawingTools** namespace and are properly known as **DrawingTools**.
* Drawing Methods called from indicators or strategies have been moved to a new static partial **Draw** class.
* Drawing Methods have all received a signature change which requires you specify the owner (object) which drew the **DrawingTool** object.
* Drawing Methods no longer return an interface but rather an instance of the **DrawingTool** object itself.
* Drawing Methods now use the **System.Windows.Media.Brushes** class instead of the **System.Drawing.Color** structure.

{% table %}

* Tip
* Description

---

* Tip: **DrawingTools** are now completely unprotected and you can review their source code from the **DrawingTools** folder of the **NinjaScript Editor's** explorer menu.
{% /table %}

{% table %}

* Method
* Description

---

* **// example syntax**
**Draw.Line(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int endBarsAgo, double endY, Brush brush)**
  
**// example usage**
**Draw.Line(this, "tag1", true, 10, Low[0], 0, Brushes.Red);**
{% /table %}

Casting a member of the **DrawObjects[]** collection must be done safely using the "as" keyword, otherwise you may receive exceptions at run time should another instance of the object (e.g., matching tag) exist from another owner:

{% table %}

* Method
* Description

---

* **NinjaScript.DrawingTools.Line myLine = DrawObjects["tag1"] as DrawingTools.Line;**
{% /table %}

**DrawingTools** anchor fields such as "Time" or "Price", etc have been moved to a **ChartAnchor** object owned by the drawing tool, rather than a direct field on the drawing object interface. Please refer to the **NinjaTrader 8** documentation for specific changes for each drawing tool:

{% table %}

* Method
* Description

---

* **double linePrice = myLine.StartAnchor.Price;**
{% /table %}

Objects which previously used **System.Drawing.Font** now uses new **NinjaTrader.Gui.Tools.SimpleFont** class:

{% table %}

* Method
* Description

---

* **Gui.Tools.SimpleFont myFont = new Gui.Tools.SimpleFont("Arial", 12);**
{% /table %}

Properties and other methods/objects which previously **System.Drawing.Color** structure now use the **System.Windows.Media.Brushes** class:

{% table %}

* Method
* Description

---

* **BackBrush = Brushes.Blue;**
{% /table %}

{% callout type="note" %}

For custom Brush objects, it is important to .Freeze() the Brush due to the multi-threaded architecture of **NinjaTrader 8**. Please be sure to review the new information on using **Brushes**.

{% /callout %}

### Namespaces

The **NinjaTrader 7** namespaces **NinjaTrader.Indicator** and **NinjaTrader.Strategy** have been renamed and moved to single **NinjaTrader.NinjaScript** namespace:

```csharp
//This namespace holds indicators in this folder and is required. Do not change it.
namespace NinjaTrader.NinjaScript.Indicators
{
   public class MyCustomIndicator : Indicator
   {
   }
}
  
//This namespace holds Strategies in this folder and is required. Do not change it.
namespace NinjaTrader.NinjaScript.Strategies
{
   public class MyCustomStrategy : Strategy
   {
   }
}
```

### Partial Classes (Porting methods and properties from UserDefinedMethods.cs)

**NinjaTrader 7** used a "UserDefinedMethods" class to define methods to be used across multiple **NinjaScript** indicators or strategies. In **NinjaTrader 8**, these pre-built partial classes have been removed to reduce a number of issues which could result from users sharing their **UserDefinedMethods.cs** files, or overwriting their existing files with copies from a new vendor. Partial classes are now best built manually and saved in the **C:\Users\<user>\Documents\NinjaTrader 8\bin\Custom\AddOns** folder.

{% callout type="warning" %}
Warning: If a partial class is saved in one of the folders used for specific **NinjaScript** objects other than **AddOns** (e.g., Indicators folder), auto-generated **NinjaScript** code may be appended to the end of the class by the **NinjaScript Editor** when compiled, which will cause a compilation error. Saving these files in the **AddOns** folder will ensure they are still accessible and will not generate code which may be cause conflicts.
{% /callout %}

You can use the template below as a starting point to create your partial class. If your partial class needs to inherit from a parent class, you can append the name of your desired parent class after the " : " to change the inheritance.

{% table %}

* Method
* Description

---

* **Note: Methods within your partial classes should be using the "public" modifier.**
{% /table %}

{% table %}

* Partial Class Example Template
* Description

---

```csharp
namespace NinjaTrader.NinjaScript.Indicators
{
   public partial class MyMethods // : parent class to inherit from
   {
       //Sample method which calculates the delta of two prices
       public double calculateDelta(double firstPrice, double secondPrice)
       {
           return Math.Abs(firstPrice - secondPrice);
       }
  
       //Sample method which prints Position information
       public void printPositionInfo(Position position)
       {
           Print(String.Format("{0}: {1} {2} at {3}", position.Instrument, position.Quantity, position.MarketPosition, position.AveragePrice));
       }
   }
}
```

Below is an example of using one of the methods in this partial class from within an Indicator:

{% table %}

* Partial Class Usage

---

```csharp
protected override void OnBarUpdate()
{
   if (CurrentBar < 1) return;
  
   // Use the static calculateDelta method to calculate the difference between the close of each bar

   double delta = MyMethods.calculateDelta(Close[0], Close[1]);

   Print(delta);

```

### Prevention of Redundant Data Loading

In **NinjaTrader 7**, multiple Data Series could be added within a script, such as an indicator, and that script could then be hosted by another script, such as a strategy. While this is still possible in **NinjaTrader 8**, there is a new safeguard in place to prevent redundant data loading in both the hosting script and the hosted indicator.

When hosting an indicator which adds Data Series programmatically, the hosting script must include the same calls to the **AddDataSeries()** method as the hosted script. Without this, an error will result, which reads "A hosted indicator tried to load additional data. All data must first be loaded by the hosting **NinjaScript** in its Configure state." Without this safeguard in place, it would be possible for unnecessarily large amounts of data to be loaded concurrently, as would be the case in a direct call to an indicator method on each **OnBarUpdate()**. By adding the calls to **AddDataSeries()** to the hosting script, you can ensure that the data is loaded when needed. Also, when this is done in the hosting script, all identical calls to **AddDataSeries()** in the hosted script will be ignored, as the data is already available.

* Hosted Indicator Loads Additional Data

```csharp
public class MyCustomIndicator : Indicator
{
   protected override void OnStateChange()
   {
     if (State == State.Configure)
     {
           AddDataSeries("AAPL", BarsPeriodType.Day, 1);
           AddDataSeries("EURUSD", BarsPeriodType.Minute, 15);
       }
   }
}
```

* Hosting Strategy Mirrors AddDataSeries() calls

```csharp
public class MyCustomStrategy : Strategy
{
   // Define a MyCustomIndicator
   MyCustomIndicator myIndicator;
  
   protected override void OnStateChange()

   {

     if (State == State.Configure)

     {

         // Instantiate the MyCustomIndicator and add it to the chart

         myIndicator = MyCustomIndicator();

         AddChartIndicator(myIndicator);

  
         // These calls to AddDataSeries() mirror the calls in the hosted indicator
         AddDataSeries("AAPL", BarsPeriodType.Day, 1);
         AddDataSeries("EURUSD", BarsPeriodType.Minute, 15);

     }

   }

```

### Bars with 0 Volume

In previous versions, the **NinjaTrader** core was designed to replace a tick with a volume of 0 with a volume of 1. This resulted in all ticks having a volume value of at least 1. **NinjaTrader 8** has removed that design policy and will now allow ticks with a volume of 0 to be processed. This policy change may require logic changes to any custom bar types, indicators, or strategies which may have previously assumed volume would always be greater than 0.

### Multi-Series default "Trading Hours" templates

The default behavior in **NinjaTrader 8** will ensure that a bars series added to a script using **AddDataSeries()** will use the same **TradingHours** template as the primary series configured by the user. In contrast, the **NinjaTrader 7** behavior was highly dependent on a number of variables. We have updated this behavior to help with consistencies and synchronization issues between multiple series; however if your script relies on two time frames using different trading hours templates, you may consider using one of the new tradingHours string overloaded used in **AddDataSeries()**:

```csharp
protected override void OnStateChange()
{
   if (State == State.Configure)
   {
     // adds a 1 minute AAPL bars with a default 24/7 session template.
     AddDataSeries("AAPL", new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1 }, "Default 24 x 7");
   }
}
```

### Miscellaneous

All of the **NinjaTrader 7** reference samples posted in our support forum have been updated to demonstrate **NinjaTrader 8** functionality. Please be sure to check the reference sample section to see other undocumented features and concepts which may not have been covered in the help guide:

[Official NinjaScript reference code samples](official-ninjascript-reference-code-samples)

There are several other changes to implementation which are not covered in detail on this overview, please see the code breaking changes table at the bottom of this page which will compare the implementation changes between both versions.
