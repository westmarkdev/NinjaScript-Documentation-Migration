










 


Code Breaking Changes







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?code_breaking_changes.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt;
Code Breaking Changes | [Previous page](ninjascript.htm)
[Return to chapter overview](ninjascript.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









The following document is intended as a high level overview of the NinjaScript changes you can expect between NinjaTrader 7 and NinjaTrader 8.  For specific information on a particular method or property, you can refer to the dynamically formatted Code Breaking table at the bottom of this page.  We recommend using the Filter and Sorting features built into the table, as well checking the Summary column and expanding the Details section of each entry for general information.  Referring to the conveniently linked NinjaTrader 8 and NinjaTrader 7 documentation will provide specific information on syntax, usage, and examples of any new implementation or element names.  


 




|  |
| --- |
| Note:  Information on this page focuses on supported (documented) NinjaTrader methods and properties shared between versions.  NinjaTrader 8 has seen a significant increase in supported NinjaTrader code, however if you were using previously undocumented NinjaTrader 7 methods or properties, they will NOT be covered in this topic.  You may be able to find more information on previously undocumented methods and properties in the NinjaTrader 8 Help Guide, or our support staff will also be happy to personally point you in the right direction. |



 




|  |
| --- |
| Critical:   If your product uses unsupported (undocumented) elements we strongly urge you to put your scripts through thorough testing to ensure they still behave as expected.  There is NO guarantee that previously undocumented method or property behavior has not changed in the new version of NinjaTrader 8. |



 


For questions or comments, please contact us at platformsupport@ninjatrader.com


![tog_minus](tog_minus.gif)        [Implementation Changes Overview](javascript:HMToggle('toggle','ImplementationChangesOverview','ImplementationChangesOverview_ICON'))




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Initialize(), OnStartUp(), OnTermination()
NinjaTrader 8 has simplified the methods used to set or release various resources during the lifetime of a NinjaTrader object to a single [OnStateChange()](onstatechange.htm) method. This single method is guaranteed to be called for every change in State of the object.  It is from this method you can monitor the progression of the object throughout its lifetime in order to setup various resources, set properties, or take action the moment State has changed.  This method also exposes a [State](state.htm) variable which can be used in various other methods, such as OnBarUpdate(), in order to tell your indicator or strategy to process data depending on the actual State of the object.
 
For example, pushing settings to the UI, or setting initial values for public properties can now be done use OnStateChange() when the state has reached State.SetDefaults:
 


| ns |
| --- |
| protected override void OnStateChange() 
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
} |



 
 
If you have custom resources that need to be setup before the NinjaTrader object is active and processing data, instead of using the Initialize() method, you can now set this up once the OnStateChange() method has reached State.Configure state:
 


| ns |
| --- |
| protected override void OnStateChange() 
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
} |



 
 
NinjaTrader 7 had no concept to detect when your NinjaTrader object was transitioning from processing Historical data to processing Real-time data.  Now with NinjaTrader 8, the OnStateChange() method provides a State.Transition state which will notify you when this change is about to occur.  If your NinjaTrader 7 indicators or strategies were using custom methods to try to detect this transition, your custom methods may be refactored under this new state:
 


| ns |
| --- |
| protected override void OnStateChange() 
{ 
   if (State == State.Transition) 
   { 
     Print("We're going to real-time data..."); 
     // setup your real-time data resources here 
   } 
} |



 
 
When your NinjaTrader object is shutting down, and you need clean up any custom device resources, instead of using OnTermination(), you should now clean up these resources once the OnStateChange() method has reached the State.Terminated state:
 


| ns |
| --- |
| protected override void OnStateChange() 
{ 
   if (State == State.Terminated) 
   { 
     // release any device resources 
     if(myTimer != null) 
         myTimer = null; 
   } 
} |



 
NinjaTrader previously used a Historical bool property to notify when an indicator or strategy bar was being processed historically or real-time.  The NinjaTrader 8 OnStateChange() approach has now introduced a class level variable State where you can check for State.Historical or State.Realtime in any of the other event methods which will allow you to take action depending on the desired state:
 


| ns |
| --- |
| protected override void OnBarUpdate() 
{ 
   // only process on real-time data 
   if (State == State.Historical) 
     return; 
 
   else if (State &gt;= State.Realtime)
       // rest of logic
} |



 
Strategies, Orders, and Accounts
Low level access has been provided to allow more flexibility with the information pertaining to trade data.
 
•IOrders, IExecution, and IPosition interfaces have all been replaced directly with the corresponding object•The signatures of the related NinjaScript events have changed to match the NinjaTrader internal Update events•Methods now return and update with the object instance generated, instead of the previously used interface 


|  |
| --- |
| Tip:  Since NinjaTrader 8 now exposes the direct Order object, rather than an IOrder interface, it is possible to receive null object reference errors if you attempt to access an order object before the entry or exit order method has returned.  To prevent these situations, it is recommended to assign your strategies Order variables in the OnOrderUpdate() method and match them by their signal name (order.Name).  Please see the example beginning on line #22 below for demonstration of assigning order objects to private variables.   |



 


| ns |
| --- |
| Order myOrder = null;
 
protected override void OnBarUpdate()
{         
   if (Position.MarketPosition == MarketPosition.Flat &amp;&amp; myOrder == null)
     EnterLongLimit(Low[0], "Entry");
   
   if (myOrder != null)
   {
     Print(myOrder.OrderState);
      
     if (myOrder.OrderState == OrderState.Cancelled || myOrder.OrderState == OrderState.Filled)
         myOrder = null;            
   }
}      
 
protected override void OnOrderUpdate(Cbi.Order order, double limitPrice, double stopPrice, 
   int quantity, int filled, double averageFillPrice, 
   Cbi.OrderState orderState, DateTime time, Cbi.ErrorCode error, string comment)
{      
   // compare the order object created via EnterLongLimit by the signal name
   if (myOrder == null &amp;&amp; order.Name == "Entry")
   {
     // assign myOrder to matching order update
     myOrder = order;         
   }
} |



 
Data Series
Previously there had been type specific Data Series implementations (e.g., IntSeries, TimeSeries, BoolSeries, etc).  Now there just is a template [Series<t>](seriest.htm) class which could be used generically and even allows support for additional types:
 


| ns |
| --- |
| Series<double> mySeries = new Series<double>(this);
Series<datetime> myTimeSeries = new Series<datetime>(this); |



 
The DataSeries.Set() method used to assign Data Series or Plot values has been removed and values can now be stored using a single assignment operator:
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
   // set public plotting data series close value of current bar
   MyPlot[0] = Close[0];
   // set custom Series<datetime> to time value of current bar
   myTimeSeries[0] = Time[0];         
} |



 
Drawing
The DrawObjects used in NinjaTrader have received a number of changes:
 
•All DrawObjects have been moved to a separate NinjaScript.DrawingTools namespace and are properly known as DrawingTools•Drawing Methods called from indicators or strategies have been moved to a new static partial Draw class•Drawing Methods have all received a signature change which requires you specify the owner (object) which drew the DrawingTool object•Drawing Methods no longer returns an interface but rather an instance of the DrawingTool object itself•Drawing Methods now use the [System.Windows.Media.Brushes](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx) class instead of the [System.Drawing.Color](https://msdn.microsoft.com/en-us/library/system.drawing.color(v=vs.110).aspx) structure 


|  |
| --- |
| Tip:  DrawingTools are now completely unprotected and you can review their source code from the DrawingTools folder of the NinjaScript Editor's explorer menu |



 


| ns |
| --- |
| // example syntax
Draw.Line(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int endBarsAgo, double endY, Brush brush)
 
// example usage
Draw.Line(this, "tag1", true, 10, Low[0], 0, Brushes.Red); |



 
Casting a member of the DrawObjects[] collection must be done safely using the "as" keyword, otherwise you may receive exceptions at run time should another instance of the object (e.g., matching tag) exist from another owner:
 


| ns |
| --- |
| NinjaScript.DrawingTools.Line myLine = DrawObjects["tag1"] as DrawingTools.Line; |



 
DrawingTools anchor fields such as "Time" or "Price", etc have been moved to a ChartAnchor object owned by the drawing tool, rather than a direct field on the drawing object interface.  Please refer to the NinjaTrader 8 documentation for specific changes for each drawing tool:
 


| ns |
| --- |
| double linePrice = myLine.StartAnchor.Price; |



 
Objects which previously used System.Drawing.Font now uses new NinjaTrader.Gui.Tools.SimpleFont class:
 


| ns |
| --- |
| Gui.Tools.SimpleFont myFont = new Gui.Tools.SimpleFont("Arial", 12); |



 
Properties and other methods/objects which previously [System.Drawing.Color](https://msdn.microsoft.com/en-us/library/system.drawing.color(v=vs.110).aspx) structure now use the [System.Windows.Media.Brushes](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx) class:
 


| ns |
| --- |
| BackBrush = Brushes.Blue; |



 


|  |
| --- |
| Note:  For custom Brush objects, it is important to .Freeze() the Brush due to the multi-threaded architecture of NinjaTrader 8.  Please be sure to review the new information on using [Brushes](brushes.htm) |



 
Namespaces 
The NinjaTrader 7 namespaces NinjaTrader.Indicator and NinjaTrader.Strategy have been renamed and moved to single NinjaTrader.NinjaScript namespace
 


| ns |
| --- |
| //This namespace holds indicators in this folder and is required. Do not change it.
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
} |



 
Partial Classes (Porting methods and properties from UserDefinedMethods.cs)
NinjaTrader 7 used a "UserDefinedMethods" class to define methods to be used across multiple NinjaScript indicators or strategies. In NinjaTrader 8, these pre-built partial classes have been removed to reduce a number of issues which could result from users sharing their UserDefinedMethods.cs files, or overwriting their existing files with copies from a new vendor. Partial classes are now best built manually and saved in the C:\Users\<user>\Documents\NinjaTrader 8\bin\Custom\AddOns folder.
 


|  |
| --- |
| Warning: If a partial class is saved in one of the folders used for specific NinjaScript objects other than AddOns (e.g., Indicators folder), auto-generated NinjaScript code may be appended to the end of the class by the NinjaScript Editor when compiled, which will cause a compilation error.  Saving these files in the AddOns folder will ensure they are still accessible and will not generate code which may be cause conflicts. |



 
You can use the template below as a starting point to create your partial class. If your partial class needs to inherit from a parent class, you can append the name of your desired parent class after the " : " to change the inheritance.
 


|  |
| --- |
| Note: Methods within your partial classes should be using the "public" modifier. |



 


| ns   Partial Class Example Template |
| --- |
| namespace NinjaTrader.NinjaScript.Indicators
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
} |



 
Below is an example of using one of the methods in this partial class from within an Indicator:
 


| ns  Partial Class Usage |
| --- |
| protected override void OnBarUpdate()
{
   if (CurrentBar &lt; 1) return;
 
   // Use the static calculateDelta method to calculate the difference between the close of each bar
   double delta = MyMethods.calculateDelta(Close[0], Close[1]);
 
   Print(delta);
} |



 


|  |
| --- |
| Tip:  At the time of the Beta implementation, the NinjaScript Editor does NOT include a partial class generator wizard, as it does for core NinjaScript Types such as Drawing Tools, Market Analyzer Columns, or Strategies. However, we are currently tracking a suggestion to implement a wizard for partial classes, under ID # SFT-341.   Please feel free to contact platformsupport@ninjatrader.com if you would like to add your vote for this enhancement. |



 
Prevention of Redundant Data Loading
In NinjaTrader 7, multiple Data Series could be added within a script, such as an indicator, and that script could then be hosted by another script, such as a strategy. While this is still possible in NinjaTrader 8, there is a new safeguard in place to prevent redundant data loading in both the hosting script and the hosted indicator. 
 
When hosting an indicator which adds Data Series programmatically, the hosting script must include the same calls to the AddDataSeries() method as the hosted script. Without this, an error will result, which reads "A hosted indicator tried to load additional data. All data must first be loaded by the hosting NinjaScript in its Configure state." Without this safegaurd in place, it would be possible for unnecessarily large amounts of data to be loaded concurrently, as would be the case in a direct call to an indicator method on each OnBarUpdate(). By adding the calls to AddDataSeries() to the hosting script, you can ensure that the data is loaded when needed. Also, when this is done in the hosting script, all identical calls to AddDataSeries() in the hosted script will be ignored, as the data is already available.
 
The examples below show this in action:
 


| ns  Hosted Indicator Loads Additional Data |
| --- |
| public class MyCustomIndicator : Indicator
{
   protected override void OnStateChange()
   {
     if (State == State.Configure)
     {
           AddDataSeries("AAPL", BarsPeriodType.Day, 1);
           AddDataSeries("EURUSD", BarsPeriodType.Minute, 15);
       }
   }
} |



 


| ns  Hosting Strategy Mirrors AddDataSeries() calls |
| --- |
| public class MyCustomStrategy : Strategy
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
} |



 
Bars with 0 Volume
In previous versions, the NinjaTrader core was designed to replace a tick with a volume of 0 with a volume of 1.  This resulted in all ticks having a volume value of at least 1.  NinjaTrader 8 has removed that design policy and will now allow ticks with a volume of 0 to be processed.  This policy change may require logic changes to any custom bar types, indicators, or strategies which may have previously assumed volume would always be greater than 0.
 
Multi-Series default "Trading Hours" templates
The default behavior in NinjaTrader 8 will ensure that a bars series added to a script using [AddDataSeries()](adddataseries.htm) will use the same "[TradingHours](tradinghours.htm)" template as the primary series configured by the user. In contrast, the NinjaTrader 7 behavior was highly dependent on a number of variables.  We have updated this behavior to help with consistences and synchronization issues between multiple series; however if you your script relies on two times frames using different trading hours templates, you may consider using one of the new tradingHours string overloaded used in [AddDataSeries()](adddataseries.htm):
 


| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.Configure)
   {
     // adds a 1 minute AAPL bars with a default 24/7 session tempalte.
     AddDataSeries("AAPL", new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1 }, "Default 24 x 7");
   }
} |



 
Miscellaneous 
All of the NinjaTrader 7 reference samples posted in our support forum have been updated to demonstrate NinjaTrader 8 functionality.  Please be sure to check the reference sample section to see other undocumented features and concepts which may not have been covered in the help guide:  
 
[Official NinjaScript reference code samples](http://www.ninjatrader.com/support/forum/forumdisplay.php?f=30)
 
There are several other changes to implementation which are not covered in detail on this overview, please see the code breaking changes table at the bottom of this page which will compare the implementation changes between both versions. |



![tog_minus](tog_minus.gif)        [Signature Changes Overview](javascript:HMToggle('toggle','SignatureChangesOverview','SignatureChangesOverview_ICON'))




|  |  |
| --- | --- |
| Signature
A large number of the NinjaTrader methods which were available in NinjaTrader 7 have remained largely the same and should not generate any errors on compilation.  However there are a handful of existing methods signatures which have been updated in NinjaTrader 8 in order to fit within new framework which you would need to be aware of in order to transfer these functions from NinjaTrader 7 to NinjaTrader 8.  In most cases, the fundamental argument type has been restructured, which may result in compile errors depending on the type of object that is being used within the methods signature. 
 


|  |
| --- |
| Tip:  Methods may now have additional signatures which add functionality which was not previously available.  Be sure to check the NinjaTrader 8 documentation which will cover all the available signatures available.   |


 |



![tog_minus](tog_minus.gif)        [Name Changes Overview](javascript:HMToggle('toggle','NameChangesOverview','NameChangesOverview_ICON'))




|  |
| --- |
| Renamed
During the NinjaTrader 8 development process, one of our goals to make sure that our core framework matched various coding standards which have been set out in the industry.  As a result of meeting these coding standards, many NinjaTrader methods and properties needed to been renamed.    While the functionality of these methods and properties remains the same, we chose to rename these variables to follow a semantically context specific naming convention which is generally agreed upon to favor readability.  We feel that the renaming of these properties and methods more explicitly describes the intended function to the developer who may be reviewing code.  The largest number of changes is in response to the name convention of bools, where they now follow a more strict verb-adjective or verb-noun structure.  
 
For an example:
 
•The property FirstTickOfBar may have been hard to distinguish precisely what it represented without having to look up documentation.  In NinjaTrader 8, this property has been renamed to IsFirstTickOfBar, which now gives this property a more readable identifier name when you read this line of code as "is the first tick of bar true?"•Another example is the case of BarsSinceEntry() which was renamed to BarsSinceEntryExecution(), which now specifies that this method is looking for an entry execution.•NinjaTrader 7 sometimes had methods or properties which shared names, but references different data or actions.  For example Add() could have been used in reference to adding DataSeries to a script, adding a Plot, or adding a Line.  To be more specific, NinjaTrader 8 has renamed these to AddDataSeries(), AddPlot(), and AddLine() respectively.  •There may be cases where the property or method name has changed simply because the type of data it interacted with has changed.  (e.g., BarColor vs. BarBrush)•There are other cases where properties may have used unnecessary brevity and was renamed to favor readability (e.g., AvgPrice vs AveragePrice) 
These are just a few examples of the many name changes found in NinjaTrader 8 and some of the rational behind the number of these changes.  For simplicity, you will find a list of all the renamed properties in the table at the bottom of this document by filtering by the "Renamed" keyword. |



 



Code Breaking Table
-------------------


Below you will find a reference table which lists all of the supported NinjaScript changes between NinjaTrader 7 and NinjaTrader 8.


 


 







 /* Formatting function for row details - modify as you need */
 function format(d) {
 // `d` is the original data object for the row
 return '<div align="left" style="background-color: #fcfcfc; border: solid 1px #aab8c6; padding: 10px; border-radius: 8px;">' + d.Details + "</div>";
 }
 $(document).ready(function() {
 var table = $('#CodeChanges').DataTable({
 "order": [[ 3, "asc" ]],
 "bSortClasses": false,
 "ajax": "codebreak.json", // this is the code breaking document
 "columns": [
 { "data": "Category" },
 { "data": "Base" },
 { "data": "NT7 Name" },
 { "data": "NT8 Name"},
 { "data": "Summary" },
 { "data": "Details", "visible": true, "searchable:": false, "sortable": false } 
 
 ],
 "lengthMenu": [[25, 50, 75, 100, -1], [25, 50, 75, 100, "All"]], 
 "aoColumnDefs": [
 {
 "aTargets": [2],
 "mRender": function(data, type, full) {
 if (full["NT7 URL"] === "undefined")
 return data;
 else
 return '<a '"="" +="" href="http://www.ninjatrader.com/support/helpGuides/nt7/index.html?' + full[" nt7="" target="new" url"]="">' + data + '</a>';
 }
 },
 {
 "aTargets": [3],
 "mRender": function(data, type, full) {
 if (full["NT8 URL"] === "undefined")
 return data ;
 else
 return '<a '"="" +="" href="http://www.ninjatrader.com/support/helpGuides/nt8/index.html?' + full[" nt8="" target="new" url"]="">' + data + '</a>';
 }
 },
 {
 "aTargets": [4],
 "mRender": function(data, type, full) {
 if (full["Summary"] === "undefined")
 return "" ;
 else
 return data;
 }
 }, 
 {
 "aTargets": [5],
 "mRender": function (data, type, full) {
 if (full["Details"] != "undefined")
 return '<small><a id="details" style="cursor: pointer;">Details</a></small>' 
 else return '';
 }
 }
 ]
 });
 // Add event listener for opening and closing details
 $('#CodeChanges tbody').on('click', '#details', function () {
 var tr = $(this).closest('tr');
 var row = table.row(tr); 
 if (row.child.isShown()) {
 // This row is already open - close it
 row.child.hide();
 tr.removeClass('shown');
 }
 else {
 // Open this row
 row.child(format(row.data())).show();
 tr.addClass('shown');
 }
 });
 });
 


| Category | Base | NT7 Method/Property | NT8 Method/Property  | Summary |  |
| --- | --- | --- | --- | --- | --- |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 


HMInitToggle('ImplementationChangesOverview\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ImplementationChangesOverview\',\'ImplementationChangesOverview\_ICON\')');
HMInitToggle('ImplementationChangesOverview','hm.type','dropdown','hm.state','0');
HMInitToggle('SignatureChangesOverview\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'SignatureChangesOverview\',\'SignatureChangesOverview\_ICON\')');
HMInitToggle('SignatureChangesOverview','hm.type','dropdown','hm.state','0');
HMInitToggle('NameChangesOverview\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'NameChangesOverview\',\'NameChangesOverview\_ICON\')');
HMInitToggle('NameChangesOverview','hm.type','dropdown','hm.state','0');



</user></datetime></datetime></datetime></double></double></t></double>