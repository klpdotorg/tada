$(function() {
    $("a[data-toggle='tab']").click(function(e){
        $(".tab-content").css("border-top-color",$(this).css('backgroundColor'));
    });


    $("#menu-toggle").click(function(e) {
          e.preventDefault();
          $("#wrapper").toggleClass("toggled");
    });

    var defaultData = [
    {
        id: 1234,
        text: 'Bangalore',
        href: '#1234',
        tags: ['0'],
        nodes: [
          {
            id: 12341,
            text: 'Bangalore North',
            href: '#12341',
            tags: ['0'],
            nodes: [
              {
                id: 123411,
                text: 'Yelahanka',
                href: '#123411',
                tags: ['0'],
                nodes: [
                    {
                        id: 1234111,
                        text: 'GKLPS Yelahanka',
                        href: '#123411',
                        tags: ['0']
                    },
                    {
                        id: 1234112,
                        text: 'GULPS Yelahanka',
                        href: '#123412',
                        tags: ['0']
                    }
                ]
              },
              {
                id: 123412,
                text: 'Yeshwantpur',
                href: '#123412',
                tags: ['0'],
                nodes: [
                    {
                        id: 1234121,
                        text: 'GKLPS Yeshwantpur',
                        href: '#1234121',
                        tags: ['0']
                    },
                    {
                        id: 1234122,
                        text: 'GULPS Yeshwantpur',
                        href: '#1234122',
                        tags: ['0']
                    }
                ]
              }
            ]
          },
          {
            id: 12342,
            text: 'Bangalore Central',
            href: '12342',
            tags: ['0']
          }
        ]
      },
      {
        id: 1233,
        text: 'Mysore',
        href: '#1233',
        tags: ['0']
      },
      {
        id: 1222,
        text: 'Yadgir',
        href: '#1222',
         tags: ['0']
      },
      {
        id: 1221,
        text: 'Belgaum',
        href: '#1221',
        tags: ['0'],
        nodes: [
          {
            id:12351,
            text: 'Belgaum North',
            href: '#12341',
            tags: ['0'],
            nodes: [
              {
                id:123511,
                text: 'Yelahanka',
                href: '#123411',
                tags: ['0'],
                nodes: [
                    {
                        id:1235111,
                        text: 'GKLPS Yelahanka',
                        href: '#123411',
                        tags: ['0']
                    },
                    {
                        id:1235112,
                        text: 'GULPS Yelahanka',
                        href: '#123412',
                        tags: ['0']
                    }
                ]
              },
              {
                id:123512,
                text: 'Yeshwantpur',
                href: '#123412',
                tags: ['0'],
                nodes: [
                    {
                        id:1235121,
                        text: 'GKLPS Yeshwantpur',
                        href: '#123421',
                        tags: ['0']
                    },
                    {
                        id:1235122,
                        text: 'GULPS Yeshwantpur',
                        href: '#123422',
                        tags: ['0']
                    }
                ]
              }
            ]
          },
          {
            id:12352,
            text: 'Belgaum Central',
            href: '12342',
            tags: ['0']
          }
        ]
      },
    ];
        
    $('#treeview_side').treeview({
        color: "#333333",
        enableLinks: true,
        data: defaultData,
        borderColor: "#f5f5f5",
        backColor: "#f5f5f5"
    });



    var $expandibleTree = $('#treeview-expandible').treeview({
          data: defaultData,
          onNodeCollapsed: function(event, node) {
            $('#expandible-output').prepend('<p>' + node.text + ' was collapsed</p>');
          },
          onNodeExpanded: function (event, node) {
            $('#expandible-output').prepend('<p>' + node.text + ' was expanded</p>');
          }
        });

        var findExpandibleNodess = function() {
          return $expandibleTree.treeview('search', [ $('#input-expand-node').val(), { ignoreCase: false, exactMatch: false } ]);
        };
        var expandibleNodes = findExpandibleNodess();

        // Expand/collapse/toggle nodes
        $('#input-expand-node').on('keyup', function (e) {
          expandibleNodes = findExpandibleNodess();
          $('.expand-node').prop('disabled', !(expandibleNodes.length >= 1));
        });

        $('#btn-expand-node.expand-node').on('click', function (e) {
          var levels = $('#select-expand-node-levels').val();
          $expandibleTree.treeview('expandNode', [ expandibleNodes, { levels: levels, silent: $('#chk-expand-silent').is(':checked') }]);
        });

        $('#btn-collapse-node.expand-node').on('click', function (e) {
          $expandibleTree.treeview('collapseNode', [ expandibleNodes, { silent: $('#chk-expand-silent').is(':checked') }]);
        });

        $('#btn-toggle-expanded.expand-node').on('click', function (e) {
          $expandibleTree.treeview('toggleNodeExpanded', [ expandibleNodes, { silent: $('#chk-expand-silent').is(':checked') }]);
        });

        // Expand/collapse all
        $('#btn-expand-all').on('click', function (e) {
          var levels = $('#select-expand-all-levels').val();
          $expandibleTree.treeview('expandAll', { levels: levels, silent: $('#chk-expand-silent').is(':checked') });
        });

        $('#btn-collapse-all').on('click', function (e) {
          $expandibleTree.treeview('collapseAll', { silent: $('#chk-expand-silent').is(':checked') });
        });

    
        var $disabledTree = $('#treeview-disabled').treeview({
          data: defaultData,
          onNodeDisabled: function(event, node) {
            $('#disabled-output').prepend('<p>' + node.text + ' was disabled</p>');
          },
          onNodeEnabled: function (event, node) {
            $('#disabled-output').prepend('<p>' + node.text + ' was enabled</p>');
          },
          onNodeCollapsed: function(event, node) {
            $('#disabled-output').prepend('<p>' + node.text + ' was collapsed</p>');
          },
          onNodeUnchecked: function (event, node) {
            $('#disabled-output').prepend('<p>' + node.text + ' was unchecked</p>');
          },
          onNodeUnselected: function (event, node) {
            $('#disabled-output').prepend('<p>' + node.text + ' was unselected</p>');
          }
        });

        var findDisabledNodes = function() {
          return $disabledTree.treeview('search', [ $('#input-disable-node').val(), { ignoreCase: false, exactMatch: false } ]);
        };
        var disabledNodes = findDisabledNodes();

        // Expand/collapse/toggle nodes
        $('#input-disable-node').on('keyup', function (e) {
          disabledNodes = findDisabledNodes();
          $('.disable-node').prop('disabled', !(disabledNodes.length >= 1));
        });

        $('#btn-disable-node.disable-node').on('click', function (e) {
          $disabledTree.treeview('disableNode', [ disabledNodes, { silent: $('#chk-disable-silent').is(':checked') }]);
        });

        $('#btn-enable-node.disable-node').on('click', function (e) {
          $disabledTree.treeview('enableNode', [ disabledNodes, { silent: $('#chk-disable-silent').is(':checked') }]);
        });

        $('#btn-toggle-disabled.disable-node').on('click', function (e) {
          $disabledTree.treeview('toggleNodeDisabled', [ disabledNodes, { silent: $('#chk-disable-silent').is(':checked') }]);
        });

        // Expand/collapse all
        $('#btn-disable-all').on('click', function (e) {
          $disabledTree.treeview('disableAll', { silent: $('#chk-disable-silent').is(':checked') });
        });

        $('#btn-enable-all').on('click', function (e) {
          $disabledTree.treeview('enableAll', { silent: $('#chk-disable-silent').is(':checked') });
        });
        /*Expand and select*/
        $('#treeview_side').treeview('expandNode', [ 1, { levels: 2, silent: true } ]);
        $('#treeview_side').treeview('selectNode', [ 3, { silent: true } ]);
});