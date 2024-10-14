










 


Clone()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?clone.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Clone() | [Previous page](timezoneinfo.htm)
[Return to chapter overview](common.htm)










Definition
----------


Used to override the default NinjaScript Clone() method which is called any time an instance of a NinjaScript object is created.  By default,  the NinjaScript Clone() method will copy all the [Property Info](https://msdn.microsoft.com/en-us/library/system.reflection.propertyinfo%28v=vs.110%29.aspx) and [Browsable Attributes](https://msdn.microsoft.com/en-us/library/system.componentmodel.browsableattribute%28v=vs.110%29.aspx) to the new instance when the object is created (e.g., when an optimization is ran a new instance of the strategy will be created for each iteration).  However it is possible to override this behavior if desired for custom development.  There is no requirement to override the Clone behavior and this method will use the default constructor if not overridden.  


 




|  |
| --- |
| Note:  This method is reserved for advanced developers who would like to change the default behavior when a NinjaScript object is created |



 


 


Method Return Value
-------------------


A [virtual](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) object representing the NinjaScript type.


 


Syntax
------


public override object Clone()


 


 
Parameters
------------


This method does not take any parameters
----------------------------------------



 


Examples
--------




| ns |
| --- |
| public override object Clone()
{
   // custom logic to handle before the base clone
   
   return base.Clone();
 
   // custom logic to hand after the base clone
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
 
 
 



