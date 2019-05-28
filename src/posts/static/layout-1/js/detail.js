 


  $(document).ready(function(){
    $("#py_load_div").hide()
    // highlight code
    hljs.initHighlightingOnLoad();
    // render tooltip

    $(".content-markdown").each(function(){
      var content = $(this).text()
      var markedContent = marked(content)
      $(this).html(markedContent)
      // console.log(markedContent)
      var nodes = markedContent;
      // console.log($('pre'))
      // $('pre').mark("class",{"className": "class"});
      // $('pre').mark("def",{"className": "class"});
      // $('pre').mark("=",{"className": "signs"});

    });
    // $("#popUp").css({"margin-left": "0px", "top": "60px", "background": "rgba(236, 240, 241, 0)", "border":"0", "height": "10"});
    
    
    $(".wmd-preview-title").css('color', 'white')
    setTimeout(myFunction, 2000);
    function myFunction() {
    // alert('Hello');
    var iframe = document.getElementById("ifm");
    document.getElementById("ifm").style.height = iframe.contentWindow.document.getElementById("notebook-container").offsetHeight+100;
    $.scrollIndicator();
    }
    $("#id_content").css({"width": "100%"});//1105px


    // var nodes = document.getElementById('code').childNodes;
  $(document).ready(function(){
    // $('.btn').tipsy();
    
        function clearSelection() {
        var sel;
        if ( (sel = document.selection) && sel.empty ) {
            sel.empty();
        } else {
            if (window.getSelection) {
                window.getSelection().removeAllRanges();
            }
            var activeEl = document.activeElement;
            if (activeEl) {
                var tagName = activeEl.nodeName.toLowerCase();
                if ( tagName == "textarea" || (tagName == "input" && activeEl.type == "text") ) {
                    // Collapse the selection to the end
                    activeEl.selectionStart = activeEl.selectionEnd;
                }
            }
        }
    }
    document.onmouseup = function() {
          window.setTimeout(clearSelection, 0.00001);
    };

    var clipboard = new ClipboardJS(".btn",{
        target:function(trigger){
            (function(){
                if (window.getSelection) {
                  if (window.getSelection().empty) {  // Chrome
                    window.getSelection().empty();
                  } else if (window.getSelection().removeAllRanges) {  // Firefox
                    window.getSelection().removeAllRanges();
                  }
                } else if (document.selection) {  // IE?
                  document.selection.empty();
                }
            })();
            return trigger.parentElement;

        }
    })
    $(".code").hover(function() {
      $(".btn").show();
      $('.btn').tipsy({trigger: 'click'});
      }, function() {
          $(".btn").hide();
    });
    });


    // Render html language
    document.querySelectorAll("code").forEach(function(element) {
    element.innerHTML = element.innerHTML.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
    });

    // append buttons next to the code tags
    function createButton(context, func) {
        function generateButton(){
          var button = document.createElement("button");
          var icon = document.createElement("span");
          button.type = "button";
          icon.className ="far fa-copy";
          button.innerHTML = "<img style = 'width: 100px;height: 55px;' src='https://s3.eu-west-3.amazonaws.com/pythonbots/static/clippy-gray.png'/>"
          button.title = "Copied to clipboard !"
          button.setAttribute("data-clipboard-action","copy");
          button.setAttribute("data-clipboard-target","code");
          button.setAttribute("class","btn");
          button.setAttribute("style","position:absolute;background: #f0f8ff00;border: #deb88700;padding: 1px 8px;margin-left: 55%;margin-top:-5%;overflow:overlay;");
          return button
        }

      var selectPanel = document.getElementById('code');
      document.querySelectorAll("code").forEach(function(element) {
        element.appendChild(generateButton());
        element.classList.add("code");
        });
    }
    createButton(document.selectpanel);

  });
