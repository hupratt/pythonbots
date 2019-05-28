    //enable csrf post ajax
    //This function gets cookie with a given name
    function getCookie(name) {
     var cookieValue = null;
     if (document.cookie && document.cookie != '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) == (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
           break;
        }
      }
     }
     return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
     // these HTTP methods do not require CSRF protection
     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
       if (!csrfSafeMethod(settings.type) && !this.crossDomain && 
          (!(/^https:.*/.test(settings.url) || /^https:.*/.test(settings.url)))) {
       // Only send the token to relative URLs i.e. locally.
       xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
       }
     } 
    });

    var clicks = 1;
    var json_final = {};
    function onClick() {
        clicks += 1;
        document.getElementById("fill-classification").innerHTML = "Compute the classification";
        renderredditHTML(json_final);
    };
    function onClick_previous() {
        clicks -= 1;
        document.getElementById("fill-classification").innerHTML = "Compute the classification";
        renderredditHTML(json_final);
    };

    var clicks_com = 0;
    function onClick_com() {
        clicks_com += 1;
        document.getElementById("fill-classification").innerHTML = "Compute the classification";
        renderredditHTML(json_final);
    };
    function onClick_com_previous() {
        clicks_com -= 1;
        document.getElementById("fill-classification").innerHTML = "Compute the classification";
        renderredditHTML(json_final);
    };

    function onClick_class(){
      document.getElementById("fill-classification").innerHTML = post_classification();
    };

  var i = 0;
  

  function post_classification(){
    $(".ajaxProgress_small").show();
    $("#fx-sign").hide();
    var myRequest = new XMLHttpRequest();
    var json_ = {}
    // function that receives the returned data
    var comment = $(".article_comment").children().html()
    json_['content'] = comment;

    myRequest.onreadystatechange = function() {
      if (myRequest.readyState == XMLHttpRequest.DONE) {
        // console.log(myRequest.responseText);
        $(".ajaxProgress_small").hide();
        $("#fx-sign").show();
        // document.getElementById("fill-classification").innerHTML = "";
        // document.getElementById("fill-classification2").innerHTML = "";
        // document.getElementById("fill-classification").insertAdjacentHTML('beforeend',myRequest.responseText);
        // document.getElementById("fill-classification2").insertAdjacentHTML('beforeend',myRequest.responseText);
        alert(myRequest.responseText);
      }
    }
    loc = window.location;
    custom_path="/reddit/"
    var endpoint =  'https://' + loc.host + custom_path + 'classify/';

    myRequest.open('POST', endpoint, true); // visit the endpoint URL in ansync = True mode
    myRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    myRequest.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    myRequest.send(JSON.stringify(json_)); 
  };


  function grab_reddit_article(){
    $(".ajaxProgress").show();
    $("#fx-sign").hide();
    $("#tick").hide();
    var myRequest = new XMLHttpRequest();
    function funcx()
       {
       // your code here
       // break out here if needed
       setTimeout(funcx, 3000);
       }

    myRequest.onreadystatechange = function() {
      if (myRequest.readyState == XMLHttpRequest.DONE) {
          // alert(myRequest.responseText);
          ourData = JSON.parse(myRequest.responseText);
          // alert(ourData[1]['title']);
          json_final = ourData;
          renderredditHTML(ourData);
          $("#tick").show();
          funcx();
          $("#tick").hide();
          $("#fx-sign").show();
          // return renderHTML(ourData);
      }
    }
    loc = window.location;
    custom_path="/reddit/"
    var endpoint =  'https://' + loc.host + custom_path + 'random-reddit-article/';
    
    myRequest.open('GET', endpoint, true);
    myRequest.send(); 
  };




  var i = 0;

  function grab_new_quote(){
    document.getElementById("fill-quote").innerHTML = "";
    document.getElementById("fill-author").innerHTML = "";
    $(".ajaxProgress").show();
    var myRequest = new XMLHttpRequest();
    myRequest.onreadystatechange = function() {
      if (myRequest.readyState == XMLHttpRequest.DONE) {
        // alert(myRequest.responseText);
        ourData = JSON.parse(myRequest.responseText);
        renderHTML(ourData);
      }
    }
    loc = window.location;
    custom_path="/quote/"
    var endpoint =  'https://' + loc.host + custom_path + 'random-movie-quote/';
    myRequest.open('GET', endpoint, true);
    myRequest.send(); 
  };

  function grab_famous_quote(){
    document.getElementById("fill-famous-quote").innerHTML = "";
    document.getElementById("fill-famous-author").innerHTML = "";
    $(".ajaxProgress").show();
    var myRequest = new XMLHttpRequest();
    myRequest.onreadystatechange = function() {
      if (myRequest.readyState == XMLHttpRequest.DONE) {
          // alert(myRequest.responseText);
          ourData = JSON.parse(myRequest.responseText);
          // alert(ourData);
          renderfamousHTML(ourData);
          // return renderHTML(ourData);
      }
    }
    loc = window.location;
    custom_path="/quote/"
    var endpoint =  'https://' + loc.host + custom_path + 'random-famous-quote/';
    myRequest.open('GET', endpoint, true);
    myRequest.send(); 
  };


  function renderredditHTML(data){

    document.getElementById("fill-article").innerHTML = "";
    document.getElementById("fill-article-date").innerHTML = "";
    document.getElementById("fill-article-comments").innerHTML = "";
    document.getElementById("fill-article-likes").innerHTML = "";
    $(".article_comment").empty();

    document.getElementById("fill-article2").innerHTML = "";
    document.getElementById("fill-article-date2").innerHTML = "";
    document.getElementById("fill-article-comments2").innerHTML = "";
    document.getElementById("fill-article-likes2").innerHTML = "";
    $(".article_comment2").empty();

    if (i == 0){ // var prevents from adding the same elem over and over
    $(".ajaxProgress").hide();

      for(var index in data) {
        // console.log(index, data[index]);
        var dic = data[index];
        if (index == clicks){

        for (var index in dic) {
          var dic2 = dic[index];
          if(index=='title'){
            document.getElementById("fill-article").insertAdjacentHTML('beforeend',dic['title']);
            document.getElementById("fill-article2").insertAdjacentHTML('beforeend',dic['title']);
          }

          if(index=='article_url'){
            document.getElementById("fill-article").setAttribute("href",dic['article_url']);
            document.getElementById("fill-article2").setAttribute("href",dic['article_url']);

          // console.log(dic['article_url']);
          }

          if(index=='date'){
            document.getElementById("fill-article-date").insertAdjacentHTML('beforeend','Published on '+dic['date']);
            document.getElementById("fill-article-date2").insertAdjacentHTML('beforeend','Published on '+dic['date']);
          }
          if(index=='score'){
            document.getElementById("fill-article-likes").insertAdjacentHTML('beforeend','Likes: '+dic['score']);
            document.getElementById("fill-article-likes2").insertAdjacentHTML('beforeend','Likes: '+dic['score']);

          }
          var newDiv = document.createElement("div");
          newDiv.setAttribute('class', 'article_comment'); 
          var newDiv2 = document.createElement("div");
          newDiv2.setAttribute('class', 'article_comment2'); 
          // console.log(index, dic[index]);
            if(index=='comments'){
              for (var index in dic2) {
                var dic3 = dic2[index];
                // console.log(index, clicks_com);
                if (clicks_com == index) {
                // console.log(index, dic2[index]);
                  // console.log(dic3['comment']);
                  var createA = document.createElement('a');
                  var createAText = document.createTextNode(dic3['comment']);
                  createA.setAttribute('href', dic3['comment_url']);
                  createA.setAttribute('style', " width:85%; color:black;font-size: 100%;");
                  createA.appendChild(createAText);
                  newDiv.appendChild(createA);  


                  var createA2 = document.createElement('a');
                  var createAText2 = document.createTextNode(dic3['comment']);
                  createA2.setAttribute('href', dic3['comment_url']);
                  createA2.setAttribute('style', "width:85%; color:black;font-size: 150%;");
                  createA2.appendChild(createAText2);
                  newDiv2.appendChild(createA2);  

                  var currentDiv = document.getElementById("fill-article-comments");
                  var currentDiv2 = document.getElementById("fill-article-comments2");

                  currentDiv.parentNode.insertBefore(newDiv, currentDiv); 
                  currentDiv2.parentNode.insertBefore(newDiv2, currentDiv2); 

                }
              }
            }
          }          
        }
      }
    }
  };

  function renderHTML(data){
    if (i == 0){ // var prevents from adding the same elem over and over
    $(".ajaxProgress").hide();
      for(var index in data) {
        // console.log(index, data[index]);
        var dic = data[index];
        var j = 0
        for (var index in dic) {
          if (j == 0){ // var prevents print out duplicates of the same quote
          // console.log(index, dic[index]);
          document.getElementById("fill-quote").insertAdjacentHTML('beforeend',dic['quote']);
          document.getElementById("fill-author").insertAdjacentHTML('beforeend',dic['author']);
          document.getElementById("fill-picture").setAttribute("src",dic['picture_url']);
          j ++}
        }
      }
    }
  };
  function renderfamousHTML(data){
    if (i == 0){ // var prevents from adding the same elem over and over
    $(".ajaxProgress").hide();

      for(var index in data) {
        // console.log(index, data[index]);
        var dic = data[index];
        var j = 0
        for (var index in dic) {
          if (j == 0){ // var prevents print out duplicates of the same quote
          // console.log(index, dic[index]);
            document.getElementById("fill-famous-quote").insertAdjacentHTML('beforeend',dic['quote']);
            document.getElementById("fill-famous-author").insertAdjacentHTML('beforeend',dic['author']);
            j ++
          }
        }
      }
    }
  };


  $(document).ready(function(){
    $("#py_load_div").hide();
    var i = 0;
    $(".single-post").hover(function() {
      $(this).addClass("big");
      }, function() {
          $(this).addClass("norm");
    });
    $(".pan").click(function (){
      if (i == 0){grab_new_quote();}
      i++;
      $("#blank-picture").click(function (){grab_new_quote();});
    });
    var j = 0;
    $(".reddit-pannel").click(function (){
      if (j == 0){grab_reddit_article();j++;} //$("#expand").click(function (){grab_reddit_article_prime();});
    });
    var k = 0;
    $(".famous-pannel").click(function (){
      if (k == 0){grab_famous_quote();}
      k++;
    });

    $(".modal-body-title").hover(function() {
      $("#modal-body-title").addClass("show");
      $("#modal-body-title2").addClass("show");
      }, function() {
          $("#modal-body-title").removeClass("show");
          $("#modal-body-title2").removeClass("show");
    });
    $(".modal-body-comments").hover(function() {
      $("#modal-body-comments").addClass("show");
      $("#modal-body-comments2").addClass("show");
      }, function() {
          $("#modal-body-comments").removeClass("show");
          $("#modal-body-comments2").removeClass("show");
    });
    // $("button[id^='flagstrap-drop-down']").attr('style','height:5%; width:79%; left:7%');
    // $("ul[id^='flagstrap-drop-down']").attr('style','top: -60px;');



  });


