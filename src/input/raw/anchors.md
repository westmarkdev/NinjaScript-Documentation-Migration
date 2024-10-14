










 


Anchors







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?anchors.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
Anchors | [Previous page](addpastedoffset.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Returns a custom collection of ChartAnchors which will represent various points of the drawing tool.  


 




|  |
| --- |
| Note:  You must declare this property with the chart anchors used in the drawing tool which you plan on using for iteration.  Doing so will expose a simple enumerator which will allow you to to iterate over the chart anchors in which have been defined in this interface. |



 


 


Property Value
--------------


A virtual [IEnumerable](https://msdn.microsoft.com/en-us/library/9eekhta0%28v=vs.110%29.aspx) interface consisting of [ChartAnchors](chartanchor.htm)


 


Syntax
------


You must override this property using the following syntax:


public override IEnumerable<chartanchor> Anchors   

{   

     

}



Examples
--------




| ns |
| --- |
| //defines the chart anchors used for the drawing tool
public ChartAnchor      StartAnchor    { get; set; }
public ChartAnchor      MiddleAnchor   { get; set; }
public ChartAnchor      EndAnchor      { get; set; }
 
//create a collection of chart anchors used for a simple iteration
public override IEnumerable<chartanchor> Anchors 
{ 
   get 
   { 
     return new[] { StartAnchor, MiddleAnchor, EndAnchor }; 
   } 
}
 
//setup our chart anchor instances and assign a display name to each
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
      
      Name                  = "My Drawing Tool";
 
      StartAnchor           = new ChartAnchor();
      MiddleAnchor          = new ChartAnchor();
      EndAnchor             = new ChartAnchor();
 
      StartAnchor.DisplayName    = "My Start Anchor";
      MiddleAnchor.DisplayName   = "My Middle Anchor";
      EndAnchor.DisplayName      = "My End Anchor";
         
   }
}
 
//for each render pass, print out the display name of the chart anchors
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{   
   foreach (ChartAnchor anchor in Anchors)
   {
      Print(anchor.DisplayName);
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
 
 
 



</chartanchor></chartanchor>