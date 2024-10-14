










 


StrategyBaseConverter Class







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategybaseconverter.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
StrategyBaseConverter Class | [Previous page](stoptargethandling.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


A custom [TypeConverter](https://msdn.microsoft.com/en-us/library/system.componentmodel.typeconverter%28v=vs.110%29.aspx) class handling the designed behavior of a strategy's property descriptor collection.  Use this as a base class for any custom TypeConverter you are applying to a strategy class.


 




|  |
| --- |
| Notes:
•A working NinjaScript demo can be found through the reference sample on "[Using a TypeConverter to Customize Property Grid Behavior](http://ninjatrader.com/support/forum/showthread.php?t=97919)"•When applying the custom converter, you must fully qualify the name (e.g., "NinjaTrader.NinjaScript.Strategies.MyCustomConveter")•Additional TypeConverter information can be found from the [MSDN documentation](https://msdn.microsoft.com/en-us/library/system.componentmodel.typeconverter%28v=vs.110%29.aspx)•See also [TypeConverterAttribute](typeconverterattribute.htm)•For Indicators, see the [IndicatorBaseConverter](indicatorbaseconverter.htm) class |





Relevant base methods
---------------------




|  |  |
| --- | --- |
| [TypeConverter.GetProperties()](https://msdn.microsoft.com/en-us/library/system.componentmodel.typeconverter.getproperties(v=vs.110).aspx) | When overriding GetProperties(), calling base.GetProperties() ensures that all default property grid behavior works as designed |
| [TypeConverter.GetPropertiesSupported()](https://msdn.microsoft.com/en-us/library/system.componentmodel.typeconverter.getpropertiessupported(v=vs.110).aspx) | In your custom converter class, you must override GetPropertiesSupported() and return a value of true in order for your custom type converter to work |



 


 


Syntax
------


public class StrategyBaseConverter : TypeConverter


 




|  |
| --- |
| Warning:  Failure to apply a type of StrategyBaseConverter on an strategy class can result in unpredictable behavior of the standard NinjaTrader WPF property grid.   |



 


 




|  |
| --- |
| Tip: Common strategy functions like Print() are not available to a type converter instance.  To debug a type converter class, you can use the AddOn [Debug Concepts](alert_and_debug_concepts.htm) or [attach to a debugger](visual_studio_debugging.htm) (recommended) |





Examples
--------




| ns |
| --- |
| //This namespace holds Strategies in this folder and is required. Do not change it.
namespace NinjaTrader.NinjaScript.Strategies
{
   // When applying the type converter, you must fully qualify the name
   [TypeConverter("NinjaTrader.NinjaScript.Strategies.MyCustomConveter")]
   public class MyCustomStrategy : Strategy
   {
     protected override void OnStateChange()
     {
         if (State == State.SetDefaults)
         {
           Name                             = "MyCustomStrategy";
         }
     }
 
     protected override void OnBarUpdate()
     {
         //Add your custom strategy logic here.
     }
   }
 
   // custom converter class for strategies
   public class MyCustomConveter : StrategyBaseConverter
   {
     // A general TypeConveter method used for converting types
     public override PropertyDescriptorCollection GetProperties(ITypeDescriptorContext context, object component, Attribute[] attrs)
     {
         // sometimes you may need the strategy instance which actually exists on the grid
         MyCustomStrategy strategy = component as MyCustomStrategy;
 
         // base.GetProperties ensures we have all the properties (and associated property grid editors)
         // NinjaTrader internal logic handles for a given strategy
         PropertyDescriptorCollection propertyDescriptorCollection = base.GetPropertiesSupported(context)
                 ? base.GetProperties(context, component, attrs) : TypeDescriptor.GetProperties(component, attrs);
 
         if (strategy == null || propertyDescriptorCollection == null)
           return propertyDescriptorCollection;
 
         // example of why you may need the instance that exists on the grid....
         if (strategy.EntryHandling == EntryHandling.UniqueEntries)
         {
           // do something in the event a property contains some value...
         }
 
         // Loop all of the properties of the strategy
         foreach (PropertyDescriptor property in propertyDescriptorCollection)
         {
           // do something with a specific property
 
           // cannot call Print() here
           // but you can call the static Output window "Process()"
           NinjaTrader.Code.Output.Process(property.Name, PrintTo.OutputTab1);
         }
 
         // must return the collection after making changes
         return propertyDescriptorCollection;
     }
 
     // Important:  This must return true otherwise the type converter will not be called
     public override bool GetPropertiesSupported(ITypeDescriptorContext context)
     { return true; }
   }
} |






 
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
 
 
 



