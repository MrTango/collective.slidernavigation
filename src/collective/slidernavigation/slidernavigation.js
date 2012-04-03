jq(document).ready(function() {
  jq("ul#slidernav-tabs").tabs("#slidernav-panes > div", {
    effect: 'fade',
    event: 'mouseover',
    rotate: true,
  });

  var api = jq("#slidernav-tabs").data("tabs");

  function load_pane_content(event, index) {
    if(index == undefined){
      var index = api.getIndex();
    }
    // get the pane to be opened
    var pane = api.getPanes().eq(index);
    api.click(index);
    // only load once:
    if (!pane.hasClass("loaded")) {
      // we use the rel tag to get the load url
      pane.load(api.getTabs().eq(index).attr("rel")).addClass("loaded");
    }
  }
 
  // load initial tab:
  var tabindex = 0;
  load_pane_content(0, tabindex);

  // bind event handler to tabs
  jq("ul#slidernav-tabs").bind("mouseover load", load_pane_content);
   
});
