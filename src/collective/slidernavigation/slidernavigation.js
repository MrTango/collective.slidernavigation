jq(document).ready(function() {
  jq("ul#slidernav-tabs").tabs("#slidernav-panes > div", {
    effect: 'ajax',
    event: 'mouseover',
  });
});
