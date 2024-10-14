










 


ApplyTo()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?simplefont_applyto.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SimpleFont](simplefont_class.htm) &gt;
ApplyTo() | [Previous page](simplefont_class.htm)
[Return to chapter overview](simplefont_class.htm)










Definition
----------


Applies a custom [SimpleFont](simplefont_class.htm) object's properties (family, size, and style) to a [Windows Control](https://msdn.microsoft.com/en-us/library/system.windows.controls.control(v=vs.110).aspx)



Method Return Value
-------------------


This method does not return a value.
------------------------------------


 


Syntax
------


<simplefont>.ApplyTo(DependencyObject target)


 




|  |  |
| --- | --- |
| target | The [DependencyObject](https://msdn.microsoft.com/en-us/library/system.windows.dependencyobject(v=vs.110).aspx) to apply the SimpleFont object |



 


 


Examples
--------




| ns |
| --- |
| // Define the custom button control object
System.Windows.Controls.Button myButton = new System.Windows.Controls.Button
{
   Name = "myButton",
   Content = "Buy",
   Foreground = Brushes.White,
   Background = Brushes.Green,
};
 
// Create a custom SimpleFont object and then apply it to the button
SimpleFont myFont = new SimpleFont("Consolas", 22);
 
myFont.ApplyTo(myButton); |






 
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
 
 
 



</simplefont>