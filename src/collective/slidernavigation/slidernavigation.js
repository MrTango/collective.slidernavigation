jq(document).ready(function(){
  jq("ul#slidernav-tabs").tabs("#slidernav-panes > div",{
    effect: jq("#slidernav #effect").attr('rel'),
    fadeInSpeed: jq("#slidernav #fade-in-speed").attr('rel'),
    fadeOutSpeed: jq("#slidernav #fade-out-speed").attr('rel'),
    event: 'dblclick',
    initialIndex: 0,
    rotate: true,
  }).slideshow({
    autoplay: Boolean(Number(jq("#slidernav #autoplay").attr('rel'))),
    interval: jq("#slidernav #interval").attr('rel'),
    clickable: false,
  });

  var api = jq("#slidernav-tabs").data("tabs");
  if(api != undefined){
    function load_pane_content(event, index){
      if(index == undefined){
        var index = api.getIndex();
      }
      // get the pane to be opened
      var pane = api.getPanes().eq(index);
      // only load once:
      if (!pane.hasClass("loaded")){
        // we use the rel tag to get the load url
        pane.load(api.getTabs().eq(index).attr("rel")).addClass("loaded");
      }
    }
    
    function pre_load_panes(){
      api.getPanes().each(function(tabindex, tab){
        var pane = api.getPanes().eq(tabindex)
        if(tabindex != 0){
          pane.load(api.getTabs().eq(tabindex).attr("rel")).addClass("loaded").hide();
        }
      });
    }

     
    // bind event handler to tabs
    jq("ul#slidernav-tabs").bind("onBeforeClick load", load_pane_content);

    // load initial tab:
    var tabindex = 0;
    var default_tab = jq("#slidernav-tabs > li a.default").parent();
    if(default_tab.length != 0){
      tabindex = default_tab.index();
    }
    api.click(tabindex);
    load_pane_content(0, tabindex);
    if(Number(jq("#slidernav #autoplay").attr('rel') == 1)){
      pre_load_panes();
    }; 
  }
   
});
