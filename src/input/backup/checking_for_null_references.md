










 


Checking for Null References







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?checking_for_null_references.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
Checking for Null References | [Previous page](adding_indicators_to_strategie.htm)
[Return to chapter overview](tips.htm)










A common object-oriented programming error is not checking for null references on your object variables This will cause an "Object reference not set to an instance of an object" error.


 


For example:


You create a variable that holds an Order object


 




| ns |
| --- |
| private Order entryOrder = null; |



 


But in the OnBarUpdate() method you do not check if this variable as been assigned an Order object, thus when trying to access object properties it fails and yields the "Object reference not set" error since the variable is null.


 




| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (entryOrder.Filled &gt; 0)
         // Do something
} |



 


This will generate an error because you cannot access the object or any of its properties yet. You must always check if an object variable is null before attempting to access the object.


 




| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (entryOrder == null)
     {
         entryOrder = EnterLong();
     }
     else if (entryOrder != null)
     {
         if (entryOrder.Filled &gt; 0)
               // Do something
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
 
 
 



