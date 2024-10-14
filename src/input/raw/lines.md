










 


Lines







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?lines.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddLine()](addline.htm) &gt;
Lines | [Previous page](line_class.htm)
[Return to chapter overview](addline.htm)










Definition
----------


A collection holding all of the Line objects that define the visualization characteristics oscillator lines of the indicator.


 


Property Value
--------------


A collection of Line objects.


 


Syntax
------


Lines[int index]


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Lines are added to the Lines collection in order
         AddLine(Brushes.Gray, 30, "Lower"); // Stored in Lines[0]
         AddLine(Brushes.Gray, 70, "Upper"); // Stored in Lines[1]
     }
}
 
// Dynamically change the upper line's color and thickness based on the indicator value
protected override void OnBarUpdate()
{
   if(Value[0] &gt; 70)
   {
     Lines[1].Brush = Brushes.Blue;
     Lines[1].Width = 3;
   }
   else 
   { 
     Lines[1].Brush = Brushes.Gray; 
     Lines[1].Width = 1; 
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
 
 
 



