jq(document).ready(function() {
  jq("ul#slidernav-tabs").tabs("#slidernav-panes > div", {
    effect: 'fade',
    event: 'mouseover',
    rotate: true,
  });

  var api = jq("#slidernav-tabs").data("tabs");

  function load_pane_content(event, index) {
    // get the pane to be opened
    if(index == undefined){
      var index = api.getIndex();
    }
    console.log(index);
    var pane = api.getPanes().eq(index);
    api.click(index);
    if (!pane.hasClass("loaded")) {
      pane.load(api.getTabs().eq(index).attr("rel")).addClass("loaded");
    }
  }
  
  load_pane_content(0, 2);
  jq("ul#slidernav-tabs").bind("mouseover load", load_pane_content);
   
});
