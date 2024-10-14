










 


IsInstantiatedOnEachOptimizationIteration







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isinstantiatedoneachoptimizationiteration.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
IsInstantiatedOnEachOptimizationIteration | [Previous page](isfilllimitontouch.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines if the strategy should be re-instantiated (re-created) after each optimization run when using the [Strategy Analyzer Optimizer](optimize_a_strategy.htm).  


 


The default behavior is to re-instantiate the strategy for each optimization backtest run. However, the process of re-instantiating a strategy requires more time and computer resources to return results, which could impact the amount of time it takes to run an optimization.  When false, the strategy is re-used to save time and computer resources.  Under this design, internal properties are reset to default values after each iteration, but it is possible that user-defined properties and other custom resources may carry their state over from the previous iteration into a new backtest run.  To take advantage of performance optimizations, developers may need to reset class level variables in the strategy otherwise unexpected results can occur.


 




|  |
| --- |
| Note:  If you choose to take advantage of the performance benefits during strategy optimization by setting the IsInstantiatedOnEachOptimizationIteration property to false, any objects you create in your code MUST be reset during the appropriate State within the [OnStateChange()](onstatechange.htm) method.  Please see the example below on "Manually resetting class level variables to take advantage of Strategy Analyzer optimizer performance benefits".  |



 


 


Property Value
--------------


This property returns true if the strategy is not recycled; otherwise, false. Default set to true.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IsInstantiatedOnEachOptimizationIteration


 




|  |
| --- |
| Tip:  The default NinjaTrader indicators and strategies have been optimized to take advantage of performance optimizations as their resources are setup &gt;= State.Configure.  Please see the default system indicators and strategies for an idea of how you may improve your strategy and indicator performance, or you may also reference the example code below. |



 


 


Examples
--------




| ns Using IsInstantiatedOnEachOptimizationIteration to reset class level variables |
| --- |
| // A custom trades dictionary is created when strategy is instantiated
// since we later set "IsInstantiatedOnEachOptimizationIteration" to true,
// we are guaranteed to start with a new object on each optimization run
private Dictionary<datetime, string=""> myTrades = new Dictionary<datetime, string="">();
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name       = "My Optimization Test 1";
     Description = "Demonstrates using IsInstantiatedOnEachOptimizationIteration to reset a class level variable";
     Fast       = 10;
     Slow       = 25;
 
     // setting to true so our custom trades dictionary is reset on each optimization run (comes with a performance penalty)
     // This is the default behavior.
     IsInstantiatedOnEachOptimizationIteration = true;
   }
 
   else if (State == State.Terminated)
   {
     // Print the number of trades at the end of the optimization
     if (myTrades != null)
     {
         // if we set "IsInstantiatedOnEachOptimizationIteration" to false (so not using the default of true), the values here would be unexpected
         // since the custom trade dictionary was never explicitly reset at the end of each optimization
         Print(myTrades.Count);
     }
   }
}
 
protected override void OnBarUpdate()
{
   if (CurrentBar &lt; BarsRequiredToTrade)
     return;
 
   if (CrossAbove(SMA(Fast), SMA(Slow), 1))
   {
     EnterLong();
     myTrades.Add(Time[0], "long");
 
   }
   else if (CrossBelow(SMA(Fast), SMA(Slow), 1))
   {
     EnterShort();
     myTrades.Add(Time[0], "short");
   }
}
 
[Range(1, int.MaxValue), NinjaScriptProperty]
[Display(Name = "Fast", GroupName = "NinjaScriptStrategyParameters", Order = 0)]
public int Fast
{ get; set; }
 
[Range(1, int.MaxValue), NinjaScriptProperty]
[Display(Name = "Slow", GroupName = "NinjaScriptStrategyParameters", Order = 1)]
public int Slow
{ get; set; } |



 


 




| ns Manually resetting class level variables to take advantage of Strategy Analyzer optimizer performance benefits |
| --- |
| // A custom trades dictionary is declared when strategy is first optimized,
// but not instantiated until later in State.DataLoaded,
private Dictionary<datetime, string=""> myTrades;
 
// examples of other fields which need to be reset
private double myDouble;
private bool myBool;
private DateTime myDateTime;
private Order myOrderObject;
private Brush myBrushObject;
private SMA mySMAIndicator;
private Array myIntArray;
private List<object> myList;
private Series<double> mySeries;
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "My Optimization Test 2";
     Description = "Demonstrates manually resetting a class level variable without re-instantiating the strategy";
     Fast = 10;
     Slow = 25;
      
     // in this case, we do not need to re-instantiate the strategy after each optimization
     // because we are explicitly resetting the custom trade dictionary in State.DataLoaded
     // This design of re-using the strategy instance comes with performance benefits
     IsInstantiatedOnEachOptimizationIteration = false;
   }
   
   else if (State == State.DataLoaded)
   {
     // re-create custom trade dictionary on each optimization run
     // we are guaranteed to start with a new object on each optimization run
     if (myTrades != null)
       myTrades.Clear();
     else
       myTrades = new Dictionary<datetime, string="">();
      
     //Any strategy defaults which are maintained do not need to be reset if they are not mutable as the strategy runs. 
     //Any strategy state that would be mutable after State.SetDefaults needed to be reset for the next run.
     myDouble = double.MinValue;
     myBool = false;
     myDateTime = DateTime.MinValue;
     myOrderObject = null;
     myBrushObject = null;
     mySMAIndicator = SMA(14);
      
     if (myIntArray != null)
         Array.Clear(myIntArray, 0, myIntArray.Length);
     else
         myIntArray = new int[20];
      
     if (myList != null)
         myList.Clear();
     else
         myList = new List<object>();
      
     mySeries = new Series<double>(this);
   }
}
 
protected override void OnBarUpdate()
{
   if (CurrentBar &lt; BarsRequiredToTrade)
     return;
   
   if (CrossAbove(SMA(Fast), SMA(Slow), 1))
   {
     EnterLong();
     myTrades.Add(Time[0], "long");
   
   }
   else if (CrossBelow(SMA(Fast), SMA(Slow), 1))
   {
     EnterShort();
     myTrades.Add(Time[0], "short");
   }
}
 
[Range(1, int.MaxValue), NinjaScriptProperty]
[Display(Name = "Fast", GroupName = "NinjaScriptStrategyParameters", Order = 0)]
public int Fast
{ get; set; }
 
[Range(1, int.MaxValue), NinjaScriptProperty]
[Display(Name = "Slow", GroupName = "NinjaScriptStrategyParameters", Order = 1)]
public int Slow
{ get; set; } |






 
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
 
 
 



</double></object></datetime,></double></object></datetime,></datetime,></datetime,>