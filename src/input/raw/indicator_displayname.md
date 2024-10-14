










 


DisplayName







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?indicator_displayname.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
DisplayName | [Previous page](description.htm)
[Return to chapter overview](common.htm)










Definition
----------


Determines the text display on the chart panel.  This is also listed in the UI as the "Label" which can be manually changed (if not overridden).  The default behavior of this property will include the NinjaScript type Name along with its input and data series parameters.  However this behavior can be overridden if desired.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





|  |
| --- |
| Note:  For modifying the string which is used in the list of available indicators, please see the [Name](name.htm) property. |



 


Property Value
--------------


A virtual string.  This property is read-only.


 


Syntax
------


DisplayName


 


You may choose to override this property using the following syntax:


 


public override string DisplayName  

{  

   get { }  

}


 



Examples
--------




| ns Printing the default DisplayName which displays on the chart label |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Example Indicator";                    
   }      
}
 
 
protected override void OnBarUpdate()
{
   Print(DisplayName);   //Output:  Example Indicator(ES 03-15 (1 Minute))
} |



 


 




| ns Overriding the DisplayName to customize the chart label |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Example Indicator";                    
   }      
}
 
public override string DisplayName
{
   get { return "My Custom Display " + Name; }
}
 
protected override void OnBarUpdate()
{
   Print(DisplayName);   //Output:  My Custom Display Example Indicator
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
 
 
 



